from django.shortcuts import render_to_response

def test(request):
    return render_to_response("validateok.html",{});
	
def aboutus(request):
	return render_to_response("aboutus.html",{});
	
def protocol(request):
	return render_to_response("protocol.html",{});
