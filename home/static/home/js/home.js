$(document).ready(function () {
    var hrs = new Date().getHours();

    if (hrs >= 8 && hrs <= 18) {
        $('#open4business').text("We are open for business");
        $('#open-closed').text("Order Now");
    } else {
        $('#open4business').text("Sorry, we are currently closed");
        $('#open-closed').text("Pre-Order");
    }
});