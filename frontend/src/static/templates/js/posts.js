$(document).ready(function() {
    // todo
    // When page is loaded then replace all post titles with \n with \r\n -> new line
    // <br> because text in p
    var cardTexts = document.getElementsByClassName("card-text");
    for (let i = 0; i <cardTexts.length; i++) {
        var text = cardTexts[i].innerHTML;
        text = text.replace(/\\n/g, '<br>');
        cardTexts[i].innerHTML = text;
    }
});
