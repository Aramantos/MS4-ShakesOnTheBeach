$(document).ready(function () {
    $('#show-on-hover').hover(function() {
        $('#eye').css("opacity", "1");
    }, function() {
        $('#eye').css("opacity", "0");
    })
    $('#eye').click(function() {
        $('.container').css("display", "none")
        $('.container-fluid').css("display", "none")
        $('#eye').css("display", "none");
        $('#eye-x').css("display", "block");
    })
    $('#eye-x').click(function() {
        $('.container').css("display", "block")
        $('.container-fluid').css("display", "block")
        $('#eye').css("display", "block");
        $('#eye').css("opacity", "0");
        $('#eye-x').css("display", "none");
    })
});