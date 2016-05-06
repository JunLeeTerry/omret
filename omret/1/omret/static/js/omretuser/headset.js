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
                //get img base64 and use ajax push to back
                $.ajax({
                    type: "POST",
                    url: "/headupload/",
                    data: {file: img},
                    dataType: "json",
                    success: function (data) {

                    }
                });
            });


        }
    )
});