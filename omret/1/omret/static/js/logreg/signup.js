var versignup = function(classname,fieldtype){
    $(classname).blur(function(){
	
	var signupname = function(input_content){
	    $(classname).poshytip({
		className:'tip-violet',
		showOn:'none',
		bgImageFrameSize:9,
		alignTo:'target',
		alignX:'inner-right',
		alignY:'top',
		showTimeout:100,
		content:input_content
	    });
	}

	inputname=$(classname).val();
	//alert(inputname);
	if(inputname == ''){
	    if(fieldtype == "name"){
		signupname("用户名不能为空!");
	    }
	    else if(fieldtype == "email")
		signupname("邮箱不能为空!");
	    $(classname).poshytip("show");
	    $(classname).closest(".form-group").addClass("has-error");
	}
	else{
	    $.ajax({
		type:"POST",
		url:"/ver_signup/",
		data:{name:inputname,type:fieldtype},
		dataType:"json",
		success:function(data){
		    if(data.msg == "error"){
			//alert('error');
			if(fieldtype == "name")
			    signupname("用户名已存在!");
			else if(fieldtype == "email")
			    signupname("该邮箱已被注册!");
			$(classname).poshytip("show");
			$(classname).closest(".form-group").addClass("has-error");
		    }
		    else if (data.msg == "success"){
			$(classname).closest(".form-group").addClass("has-success");
			
		    }
		    else if (data.msg == "format error"){
			signupname("邮箱格式不正确!");
			$(classname).poshytip("show")
			    $(classname).closest(".form-group").addClass("has-error");
		    }
		}
	    });
	}
	$(classname).focus(function(){
	    $(this).poshytip("hide");
	    $(this).closest(".form-group").removeClass("has-error");
	    $(this).closest(".form-group").removeClass("has-success");
	});

    });
    return status;
}

var confirmpassword = function(){
    var classname = "#signup-confirmpassword";
    $(classname).poshytip({
	className:'tip-violet',
	showOn:'none',
	bgImageFrameSize:9,
	alignTo:'target',
	alignX:'inner-right',
	alignY:'top',
	showTimeout:100,
	content:"两次密码不匹配!"
    });
    
    //$("#signup-confirmpassword").focus(function(){$(this).poshytip("show")};)

    $(classname).bind('input propertychange focus',function(){
	pass = $("#signup-password").val();
	conpass = $(classname).val();
	if(conpass == ''){
	    $(classname).closest(".form-group").removeClass("has-success");
	    $(classname).closest(".form-group").removeClass("has-error");
	}
	else{
	    if (conpass == pass){
		$(classname).poshytip("hide");
		$(classname).closest(".form-group").removeClass("has-error");
		$(classname).closest(".form-group").addClass("has-success");
	    }
	    else {
		$(classname).closest(".form-group").addClass("has-error");
		$(classname).poshytip("show");
	    }
	}
    });

    $(classname).blur(function(){
	//alert('test');
	$(this).poshytip("hide");
    });
}
