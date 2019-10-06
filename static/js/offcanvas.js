$(document).ready(function () {
    document.querySelector('#toggle').addEventListener('click', function () {
        UIkit.offcanvas($('#offcanvas-nav-primary')).show();
    });
});