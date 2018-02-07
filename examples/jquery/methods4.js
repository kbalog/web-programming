$(document).ready(function () {
    $(".showlink a").click(function () {
       // hide parent div
       $(this).parent().hide(); 
       // go two levels up, find the element with the "text" class and show it
       $(this).parent().parent().find(".text").slideDown();
    });
    
    $(".hidelink a").click(function () {
       // hide the element two levels up
       $(this).parent().parent().slideUp();
       // show the link three levels up
       $(this).parent().parent().parent().find(".showlink").show();
    });
});
