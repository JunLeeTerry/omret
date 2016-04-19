/**
 * Created by Administrator on 2016/4/16.
 */
function wordTip(dom, maxSize) {
    var tip;
    $('.tip').remove();
    if (dom.val().length > maxSize) {
        dom.value = dom.value.substring(0, maxSize);
    }
    var remainSize = maxSize - dom.val().length;
    tip = "<div class='tip'>(" + remainSize + "/" + maxSize + ")</div>";
    $(dom).after(tip);

    //var left = dom.offset().left;
    var top = dom.offset().top;
    var width = dom.width();
    //var height = dom.height();
    $('.tip').css({
        'left': width - 60,
        'top': top  - 8
    });
}