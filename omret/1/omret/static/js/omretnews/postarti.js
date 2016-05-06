/**
 * Created by terry on 4/22/16.
 */
var insertimage = function (url) {
    tinymce.get("omrettinymce").execCommand('mceInsertContent', false, "<img src=" + url + ">");

}

/*var imageupload = function () {
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
 }*/


$(function () {
    var uploader = Qiniu.uploader({
        runtimes: 'html5,flash,html4',      // 上传模式,依次退化
        browse_button: 'choosefile_button',         // 上传选择的点选按钮，**必需**
        uptoken_url: '/token/',
        get_new_uptoken: false,             // 设置上传文件的时候是否每次都重新获取新的 uptoken
        // downtoken_url: '/downtoken',
        // Ajax请求downToken的Url，私有空间时使用,JS-SDK 将向该地址POST文件的key和domain,服务端返回的JSON必须包含`url`字段，`url`值为该文件的下载地址
        unique_names: true,              // 默认 false，key 为文件名。若开启该选项，JS-SDK 会为每个文件自动生成key（文件名）
        save_key: true,                  // 默认 false。若在服务端生成 uptoken 的上传策略中指定了 `sava_key`，则开启，SDK在前端将不对key进行任何处理
        domain: 'http://7xt4qr.com1.z0.glb.clouddn.com/',     // bucket 域名，下载资源时用到，**必需**
        //container: 'container',             // 上传区域 DOM ID，默认是 browser_button 的父元素，
        max_file_size: '2mb',             // 最大文件体积限制
        //flash_swf_url: 'path/of/plupload/Moxie.swf',  //引入 flash,相对路径
        max_retries: 3,                     // 上传失败最大重试次数
        dragdrop: false,                     // 开启可拖曳上传
        drop_element: 'container',          // 拖曳上传区域元素的 ID，拖曳文件或文件夹后可触发上传
        chunk_size: '4mb',                  // 分块上传时，每块的体积
        auto_start: true,
        filters: {
            mime_types: [ //只允许上传图片文件
                {title: "Image files", extensions: "jpeg,jpg,bmp,png"},
            ],
            prevent_duplicates: true //不允许选取重复文件
        },
        multi_selection:false,
        init: {
            'FilesAdded': function (up, files) {
                plupload.each(files, function (file) {
                    // 文件添加进队列后,处理相关的事情
                });
            },
            'BeforeUpload': function (up, file) {
                // 每个文件上传前,处理相关的事情

            },
            'UploadProgress': function (up, file) {
                // 每个文件上传时,处理相关的事情
                $("#uploadinfotext").html("上传中...")
            },
            'FileUploaded': function (up, file, info) {
                var domain = up.getOption('domain');
                var res = JSON.parse(info);

                var sourceLink = domain+res.key; //获取上传成功后的文件的Url
                insertimage(sourceLink);
                $("#uploadinfotext").html("上传成功！");
                $("#insertimageModal").modal('hide');
                $("#uploadinfotext").html("图片小于2M");
            },
            'Error': function (up, err, errTip) {
                //上传出错时,处理相关的事情
                $("#uploadinfotext").html(errTip)
            },
            'UploadComplete': function () {
                //队列文件处理完毕后,处理相关的事情
            },
            /*'Key': function (up, file) {
             // 若想在前端对每个文件的key进行个性化处理，可以配置该函数
             // 该配置必须要在 unique_names: false , save_key: false 时才生效

             var key = "";
             // do something with key here
             return key
             }*/
        }
    });
});