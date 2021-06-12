(function($){
    $('.app').on('click', function(){
        $('.app-option').text($(this).text());
    })
/*
    $('.sample').on('click', function(){
        $(this).select('text');
        document.execCommand('copy');
        $('.sample-copy').text("URL copiada");
    })*/

})(jQuery);