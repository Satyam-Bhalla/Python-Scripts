$(function(){
    $("td.fl").css({
        "display": 'none'
    });
    $("input[name='btnG']").prop('value', 'Search The Web');
    $("input[name='btnG']").addClass("btn btn-primary");
    $("input[name='q']").css({
        'padding' : '5px'
    });
    $("input[name='q']").addClass("form-control");
    $("input[name='btnI']").css('display', 'none');
    $("td[width='25%']").css({
        "width" : 0
    }).hide();
    $(".VBt9Dc, .hp-xpdbox").css({
        "display" : "none"
    });
    $("a.fl").css({
        "display" : "none",
        "padding" : "0 2px 0 2px"
    });
})