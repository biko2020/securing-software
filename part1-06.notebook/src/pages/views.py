from django.shortcuts import render

# Create your views here.

def addPageView(request):
	content = request.POST.get('content')
	if content:
		items = request.session.get('items', [])
		items.append(content)
		if len(items) > 10:
			items = items[-10:]
		request.session['items'] = items
	return render(request, 'pages/index.html', {'items' : items})

def erasePageView(request):
	request.session['items'] = []
	items = request.session.get('items', [])
	return render(request, 'pages/index.html', {'items' : items})


def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	items = request.session.get('items', [])

	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})
