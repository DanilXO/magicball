function getPhrase() {
            $.get('/get-phrase')
                .done(function(data) {
                    $(".textbox").html(data);
                })
                .fail(function() {
                    $(".textbox").html("Прости, мой волшебный сервер временно не работает.");
                });
        }

$(function() {$('.eball').mouseenter(function(){
    getPhrase();
    });
});