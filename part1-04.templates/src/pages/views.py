from django.http import HttpResponse
from django.template import loader


# Create your views here.

def homePageView(request):
	template  = loader.get_template('pages/index.html')
	return HttpResponse('Home page' + template.render())

def videoPageView(request):
	template = loader.get_template('pages/video.html')
	return HttpResponse("This is where I'd put my video, if I had any" + template.render())
