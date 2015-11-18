var showprofilealert = function(classname,successInfo,errorInfo){
    change_status = $("#change_status").html();
    switch(change_status){
    case "success":
	showsuccess(classname,successInfo);
	break;
    case "error":
	showerror(classname,errorInfo);
	break;
    case "normal":
	$(classname).empty();
	break;
    }
};

var showsecurityalert = function(classname,successInfo,error1Info,error2Info,error3Info,error4Info){
    change_status = $("#change_status").html();
    switch(change_status){
    case "success":
	showsuccess(classname,successInfo);
	break;
    case "error1":
	showerror(classname,error1Info);
	break;
    case "error2":
	showerror(classname,error2Info);
	break;
    case "error3":
	showerror(classname,error3Info);
	break;
    case "error4":
	showerror(classname,error4Info);
	break;
    case "normal":
	$(classname).empty();
	break;
    }
};


var showerror = function(classname,errorInfo){
    $(classname).append("<div class=\"alert alert-danger alert-dismissible\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>"+errorInfo+"</div>");
};

var showwarning = function(classname,warningInfo){
    $(classname).append("<div class=\"alert alert-warning alert-dismissible\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>"+warningInfo+"</div>");
};

var showsuccess = function(classname,successInfo){
    $(classname).append("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>"+successInfo+"</div>");
};