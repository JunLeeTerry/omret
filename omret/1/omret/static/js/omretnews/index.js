/**
 * Created by terry on 4/14/16.
 */
var notiajax = function (classname,notiid) {
    $(classname).click(function () {
        $.ajax({
            type: "POST",
            url: "/handle_noti/",
            data: {id: notiid},
            dataType: "json",
            success: function (data) {
                if (data.msg == "error") {
                    //alert('error');
                    if (fieldtype == "name")
                        signupname("用户名已存在!");
                    else if (fieldtype == "email")
                        signupname("该邮箱已被注册!");
                    $(classname).poshytip("show");
                    $(classname).closest(".form-group").addClass("has-error");
                }
                else if (data.msg == "success") {
                    $(classname).closest(".form-group").addClass("has-success");

                }
                else if (data.msg == "format error") {
                    signupname("邮箱格式不正确!");
                    $(classname).poshytip("show")
                    $(classname).closest(".form-group").addClass("has-error");
                }
            }
        });
    });
}