$(document).ready(function(){
    $("#getCountry").change(function(){
        var country = $("#getCountry :selected").text();
        console.log(country);
        $.ajax({
            url: "/api/" + country,
            success: function(result){
                var toShow = "<div style='font-size: 18px; color: #102E4A; background: #fff;'>" + "<table class='table' style='width: 500px;'><thead><tr><th colspan=2>Country-Capital<th></tr></thead><tbody><tr><th style='width: 150px;'>Country</th><td>:</td><td style='width: 150px;'>" + country + "</td></tr><tr><th style='width: 150px;'>Capital</th><td>:</td><td style='width: 350px;'>" + result + "</td></tr></tbody></table>" + "</div>";
                $("#data").html(toShow);
            }
        });
    });
});