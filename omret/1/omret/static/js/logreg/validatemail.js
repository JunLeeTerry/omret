function getWidthToWindow(proportion){
    return ($(window).width())*proportion;
}
function getHeightToWindow(proportion){
    return ($(window).height())*proportion;
}

function setWidthToWindow(element,proportion){
    element.width=($(window).height())*proportion;
}

function setHeightToWindow(element,proportion){
    element.height=($(window).width())*proportion;
}