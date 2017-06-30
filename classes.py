'''
Run with 'rm classes.jl; scrapy runspider classes.py -s LOG_ENABLED=False -o classes.jl'  
'''
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "classes"
    start_urls = [
            'http://timetable.unsw.edu.au/2017/subjectSearch.html',
            ]

    def parse(self, response):
        #This rubbish is the path given by chrome debug
        for courses in response.xpath('//table[3]/tr[1]/td/table/tr[7]/td/table/tr[2]/td/table/tr[@class]'):
            href = courses.xpath('./td[1]/a[@href]/@href').extract_first()
            #parse all course offered by that faculty
            yield scrapy.Request(response.urljoin(href), callback=self.parse_course)

    def parse_course(self, response):
        for subjects in response.xpath('//table[3]/tr[1]/td/table/tr[9]/td/table[2]/tr[2]/td/table/tr[@class]'):
            href = subjects.xpath('./td[1]/a[@href]/@href').extract_first()
            #subject code
            print(href);
            #parse all classes for each course
            yield scrapy.Request(response.urljoin(href), callback=self.parse_classes)

    def parse_classes(self, response):
        #If the class has offerings in sem 2 then the info is always in the last table
        tmp = response.xpath('//table[3]/tr[1]/td/table/tr[6]/td/table')[-1]
        for classes in tmp.xpath('./tr/td[@class="formBody"]/table'):

            #check if the offering is actually for sem 2 
            sem = classes.xpath('./tr[2]/td[6]/text()').extract_first()[1]
            if (sem != '2'): break


            if (classes.xpath('./tr[12]/td/text()').extract_first() != None):
                yield {
                        #Course code (e.g. COMP1511)
                        'code': response.xpath('//table[3]/tr[1]/td/table/tr[5]/td/text()').extract_first()[:8],
                        #class location
                        'loc': classes.xpath('./tr[12]/td/table/tr[3]/td[3]/text()').extract_first().split('(')[0],
                        #end time
                        'end': classes.xpath('./tr[12]/td/table/tr[3]/td[2]/text()').extract_first()[8:],
                        #start time
                        'start': classes.xpath('./tr[12]/td/table/tr[3]/td[2]/text()').extract_first()[0:5],
                        #day of week
                        'day': classes.xpath('./tr[12]/td/table/tr[3]/td[1]/text()').extract_first(),
                        #Type of class (e.g. lecture/tutorial etc.)
                        'type': classes.xpath('./tr[4]/td[2]/text()').extract_first(),
                        #4 digit class number (not the course code
                        #'nbr': classes.xpath('./tr[2]/td[2]/text()').extract_first(),
                    }
