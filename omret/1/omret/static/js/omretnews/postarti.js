/**
 * Created by terry on 4/22/16.
 */
var insertimage = function (url) {
    tinymce.get("omrettinymce").execCommand('mceInsertContent', false, "<img src=" + url + ">");
}

var imageupload = function () {
    $.ajax({
        type: "GET",
        url: "/imageupload/",
        data: {},
        dataType: "json",
        success: function (data) {
            insertimage(data.url);
            $("#insertimageModal").modal('hide');
        }
    });
}