/**
 * Created by Administrator on 2016/4/16.
 */
function wordTip(dom, maxSize) {
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
        'left':  width - 45,
        'top': top - 22
    });

    $(dom).focusout(function(){
        $('.tip').remove();
    })
}