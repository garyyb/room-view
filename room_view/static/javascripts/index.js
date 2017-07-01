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
                        free_now_tbl.row.add([
                            entry.location,
                            entry.start_time,
                            entry.end_time
                        ]);
                    });
                    free_now_tbl.draw();
                }
            });
        } else {
            free_now_tbl.clear();
        }
    });

    var room_search_tbl = $('#room_search_tbl').DataTable({

    });

    $("#room_search_box").on('input propertychange paste', function() {
        var query = $("#room_search_box").val().replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
        // Display a spinner here.
        setTimeout(function() {
            if ($("#room_search_box").val().replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&') !== query) return;

            if (query.length > 2) {
                $.ajax({
                    url      : '/ajax/roomquery',
                    dataType : 'json',
                    data     : {'query' : query},
                    success  : function (data) {
                        data.classes.forEach(function(entry) {
                            room_search_tbl.row.add([
                                entry.location,
                                entry.start_time,
                                entry.end_time
                            ]);
                        });
                    }
                });

                if (!$("#room_search_collapse").attr("aria-expanded")) {
                    $("#room_search_collapse").collapse();
                }

                room_search_tbl.draw();
            } else if (query.length === 0) {
                room_search_tbl.clear();
            }
        }, 1000);
    });
});