$(document).ready(function() {
    // Home page div class modifier
    if (window.location.pathname == '/') {
        document.getElementById("nav").classList.add("clear-nav");
        document.getElementsByTagName("main")[0].classList.add("container-background");
    } else {
        document.getElementsByTagName("main")[0].classList.add("container-no-background");
    }

    if ((window.location.pathname == '/login/') || window.location.pathname == '/logout/' || window.location.pathname == '/register/' ) {
        document.getElementsByTagName("footer")[0].classList.add("fixed-bottom");
    }

});