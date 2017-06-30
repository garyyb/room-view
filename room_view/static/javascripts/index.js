/**
 * Created by red on 30-Jun-17.
 */
$(document).ready(function(){
    var free_now_tbl = $('#free_now_tbl').DataTable({
        responsive  : true,
        autoWidth   : true,
        columnsDefs : [
            {"name" : "location", "title" : "Location", "targets" : 0},
            {"name" : "start_time", "title" : "Start Time",  "targets" : 1},
            {"name" : "end_time", "title" : "End Time", "targets" : 2}
        ],
    });

    var free_now_btn = $("#free_now_btn");
    $(free_now_btn).click(function(e){
        if (!$("#free_now_tbl_collapse").attr("aria-expanded")) {
            $.ajax({
                url      : '/ajax/freenow',
                dataType : 'json',
                success  : function (data) {
                    // free_now_tbl.rows.add(data.classes).draw();
                    data.classes.forEach(function(entry) {
                        console.log(entry.location);
                        free_now_tbl.row.add([
                            entry.location,
                            entry.start_time,
                            entry.end_time
                        ]);
                    });
                    free_now_tbl.draw();
                }
            })
        } else {
            free_now_tbl.clear();
        }
    });
});