(function($){
    $('.game').on('click', function(){
        $('.game-option').text($(this).text());
        $('.link').attr("href",`https://firebase-middleware-2.herokuapp.com/${$(this).text()}`)
    })

})(jQuery);