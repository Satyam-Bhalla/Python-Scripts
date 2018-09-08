
var checkStatus;
var element = new Image();
element.__defineGetter__('id', function() {
    checkStatus = 'on';
    alert("Warning!!!\nYou are trying to open developer tools.\nYou are logging out...")
});

setInterval(function() {
    checkStatus = 'off';
    console.log(element);
    console.clear();
}, 500)