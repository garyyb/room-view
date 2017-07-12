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
        language    : {
            emptyTable : "Fetching data..."
        }
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
                            "<a href=/location/" + entry.id + ">" + entry.location + "<\a>",
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
        responsive  : true,
        autoWidth   : true,
        columnsDefs : [
            {"name" : "location", "title" : "Location", "targets" : 0},
            {"name" : "start_time", "title" : "Start Time",  "targets" : 1},
            {"name" : "end_time", "title" : "End Time", "targets" : 2}
        ],
        language    : {
            emptyTable : "No results found :("
        }
    });

    $("#room_search_box").keydown(function(e) {
        if (event.which !== 13) return;
        room_search_tbl.clear().draw();

        var query = $("#room_search_box").val().replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');

        var collapser = $("#room_search_collapse");

        if (query.match(/^\s*$/)) {
            room_search_tbl.draw();
            return;
        }

        // Display a spinner here.
        $.ajax({
            url      : '/ajax/roomquery',
            dataType : 'json',
            data     : {'query' : query},
            success  : function (data) {
                data.classes.forEach(function(entry) {
                    console.log(entry.location);
                    room_search_tbl.row.add([
                        "<a href=/location/" + entry.id + ">" + entry.location + "<\a>",
                        entry.start_time,
                        entry.end_time
                    ]);
                    room_search_tbl.draw();
                });
            }
        });

        if (!collapser.attr("aria-expanded")) {
            collapser.collapse();
        }
    });
});