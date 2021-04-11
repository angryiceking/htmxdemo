$(document).ready(function(e){
    $('.image-modal-trigger').click(function(e){
        $('#login-modal').addClass('is-active')
    })
    
    $(".modal-close").click(function() {
        $("#login-modal").removeClass("is-active");
    });
})
