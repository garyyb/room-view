/**
 * Created by red on 30-Jun-17.
 */
$(document).ready(function(){
    $("#free_now_btn").onClick(function(e){
        $.ajax({
            url      : '/ajax/freenow',
            dataType : 'json',
            success  : function (data) {

            }
        })
    });
});