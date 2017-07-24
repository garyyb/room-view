
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "classes"
    start_urls = [
            'http://timetable.unsw.edu.au/2017/subjectSearch.html',
            ]

    def parse(self, response):
        print("hi")
        #That rubbish is the path given by chrome debug
        for courses in response.xpath('//table[3]/tr[1]/td/table/tr[7]/td/table/tr[2]/td/table/tr[@class]'):
            href = courses.xpath('./td[1]/a[@href]/@href').extract_first()
            #faculty
            print(href);
            yield scrapy.Request(response.urljoin(href), callback=self.parse_course)

    def parse_course(self, response):
        print("parsing: " + response.xpath('//table[3]/tr[1]/td/table/tr[9]/td/table[1]/tr[3]/td[2]/text()').extract_first())
        for subjects in response.xpath('//table[3]/tr[1]/td/table/tr[9]/td/table[2]/tr[2]/td/table/tr[@class]'):
            href = subjects.xpath('./td[1]/a[@href]/@href').extract_first()
            #subject code
            print(href);
            yield scrapy.Request(response.urljoin(href), callback=self.parse_subject)

    def parse_subject(self, response):
        code = response.xpath('//table[3]/tr[1]/td/table/tr[5]/td/text()').extract_first()[:8]

        #List of all HTML tables on the course site
        tmp = response.xpath('//table[3]/tr[1]/td/table/tr[6]/td/table')

        #Heading of the second last table (the semester 2 entries, if any exist)
        sem = tmp[-2].xpath('./tr[2]/td/text()').extract_first()

        if (sem[10:13]=="TWO"): 
            #the last table contains the semester 2 offerings for the subject
            for offering in tmp[-1].xpath('./tr/td[@class="formBody"]/table'):
                for lesson in offering.xpath('./tr[12]/td/table/tr[@class]'): 
                    info = lesson.xpath('./td/text()').extract()
                    yield {
                        #'nbr': offering.xpath('./tr[2]/td[2]/text()').extract_first(),
                        'loc': info[2].split('(')[0],
                        'end': info[1][8:],
                        'start': info[1][0:5],
                        'day': info[0],
                        'type': offering.xpath('./tr[4]/td[2]/text()').extract_first(),
                        'code': code,
                    }
