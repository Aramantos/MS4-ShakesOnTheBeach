$(document).ready(function () {

    function clipboard() {
        var copyText = document.getElementById("myInput");

        copyText.select();
        copyText.setSelectionRange(0, 99999); /* For mobile devices */

        navigator.clipboard.writeText(copyText.value);
        
        alert("Copied the order number: " + copyText.value);
    }

    $('#collection').click(function() {
        $('#collection').prop("disabled", true);
        $('#delivery-btn').prop("disabled", false);
        $('.delivery').css("display", "none")
        $('.grand-total').css("display", "none")
        $('#payment-form').css("display", "none")
        $('#collection-form').removeClass("d-none")
        $('#collection-form').css("display", "block")
    })
    $('#delivery-btn').click(function() {
        $('#delivery-btn').prop("disabled", true);
        $('#collection').prop("disabled", false);
        $('.delivery').css("display", "block")
        $('.grand-total').css("display", "block")
        $('#collection-form').css("display", "none")
        $('#payment-form').css("display", "block")
    })
});