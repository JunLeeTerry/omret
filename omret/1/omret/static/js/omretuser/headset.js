/**
 * Created by terry on 5/3/16.
 */
$(function () {
    var $uploadCrop;

    function readFile(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                croppie.croppie('bind', {
                    url: e.target.result
                });
                //$('.upload-demo').addClass('ready');
            }

            reader.readAsDataURL(input.files[0]);
        }
        else {
            swal("抱歉!您的浏览器不支持FileReader接口，请尝试使用其他浏览器。");
        }
    }

    /*   $uploadCrop = $('#croppiecontainer').croppie({
     viewport: {
     width: 150,
     height: 150,

     },
     });*/

    $('#upload').on('change', function () {
        readFile(this);
    });

    $('.rotate').on('click', function (ev) {
        croppie.croppie('rotate', parseInt($(this).data('deg')));
    });


    // ajax to upload head img
    $('#headsure').click(
        function () {
            croppie.croppie('result', {
                type: 'canvas',
                size: 'viewport',
            }).then(function (img) {
                arr = img.split(',')
                //alert(arr[1])
                //get img base64 and use ajax push to back
                $.ajax({
                    type: "POST",
                    url: "/headupload/",
                    data: {},
                    dataType: "json",
                    success: function (data) {
                        putb64(arr[1],data.url,data.token)
                    }
                });
            });


        }
    )

    function putb64(img,upurl,token) {
        var pic = img;
        var url = upurl;
        //var url = "http://up.qiniu.com/putb64/-1/key/test"
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4) {
                alert(xhr.responseText);
            }
        }
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/octet-stream");
        xhr.setRequestHeader("Authorization","UpToken "+token);
        xhr.send(pic);
    }
});