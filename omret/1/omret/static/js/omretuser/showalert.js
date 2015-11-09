var showalert = function(classname,successInfo,errorInfo){
    change_status = $("#change_status").html();
    if(change_status == "success"){
	$(classname).append("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>"+successInfo+"</div>");
    }
    else if(change_status == "error"){
	$(classname).append("<div class=\"alert alert-error alert-dismissible\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>"+successInfo+"</div>");
    }
    else if(change_status == "normal"){
	$(classname).empty();
    }
};
