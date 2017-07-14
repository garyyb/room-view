/**
 * Created by red on 30-Jun-17.
 */
$(document).ready(function(){
    $.material.init();

    var d = new Date();
    $("#hour-choice").val(d.getHours());
    $("#minute-choice").val(d.getMinutes());

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
    $(free_now_btn).click(function(){
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

    $("#room-choice").change(function(e) {
        $("#room-search-box-collapse").collapse('toggle');
    });

    $("#go").click(function() {
        var collapser = $("#room_search_collapse");
        room_search_tbl.clear().draw();

        var room_choice = $("#room-choice").val();

        var query = "";
        if (room_choice === "specific") {
            query = $("#room-search-box").val();
            query.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
        }

        var building_choice = $("#building-choice").val();

        var building;
        if (building_choice === "Any Building") {
            building = "";
        } else {
            building = building_choice;
        }
        var dt = new Date();

        var hour_choice = $("#hour-choice").val();
        var hour;
        if (hour_choice.length === 0) hour = dt.getHours();
        else hour = hour_choice;

        var minute_choice = $("#minute-choice").val();
        var minute;
        if (minute_choice.length === 0) minute = dt.getMinutes();
        else minute = minute_choice;

        var duration = $("#duration-choice").val();

        // Display a spinner here.
        $.ajax({
            url      : '/ajax/roomquery',
            dataType : 'json',
            data     :
            {
                'query'    : query,
                'building' : building,
                'hour'     : hour,
                'minute'   : minute,
                'duration' : duration
            },
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
