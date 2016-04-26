from django.shortcuts import render_to_response

def test(request):
    return render_to_response("validateok.html",{});
	
def aboutUs(request):
	return render_to_response("aboutUs.html",{});
