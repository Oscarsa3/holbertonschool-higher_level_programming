$('#toggle_header').click(() => {
    if ($('header').hasClass('green')) {
        $('header').removeClass('green');
        $('header').addClass('red');
    } else {
        $('header').removeClass('red');
        $('header').addClass('green');
    }
})