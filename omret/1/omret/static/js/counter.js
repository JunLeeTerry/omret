/**
 * Created by Administrator on 2016/4/16.
 */
function wordTip(){
    if(arguments.length == 2){
        wordTipWithoutPos(arguments[0],arguments[1]);
    }
    else if(arguments.length == 4){
        wordTipWithPos(arguments[0],arguments[1],arguments[2],arguments[3]);
    }
}

function wordTipWithoutPos(dom, maxSize) {
    wordTip(dom, maxSize, 45, 22);

}

function wordTipWithPos(dom, maxSize,x,y) {
    var tip;
    $('.tip').remove();
    if (dom.val().length >= maxSize) {
        dom.val(dom.val().substring(0, maxSize));
    }
    var remainSize = maxSize - dom.val().length;
    tip = "<div class='tip'>(" + remainSize + "/" + maxSize + ")</div>";
    $(dom).after(tip);

    var left = $('.tip').position().left;
    var top = $('.tip').position().top;
    var width = dom.width();
    var height = dom.height();
    $('.tip').css({
        'left':  width - x,
        'top': top - y
    });

    $(dom).focusout(function(){
        $('.tip').remove();
    })
}