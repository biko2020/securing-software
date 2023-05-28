from django.http import HttpResponse


# Create your views here.

def addPageView(request):
	first = request.GET.get('first')
	second = request.GET.get('second')
	if first is not None and second is not None:
		try:
			first = int(first)
			second = int(second)	
			return HttpResponse(first + second)
		except Error:
			return HttpResponse("Parameters should be integer !")
		

def multiplyPageView(request):
	first = request.GET.get('first')
	second = request.GET.get('second')
	if first is not None and second is not None:
		try:
			first  = float(first)
			second = float(second)
			return HttpResponse(int(first) * int(second))
		except Error:
			return HttpResponse("Parameters should be numbers !")
