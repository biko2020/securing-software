from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
	message_id = request.GET.get('id')
	if message_id:
		try:
			message = Message.objects.get(pk=message_id)
			content = message.content
		except Message.DoesNotExist:
			content = 'Message not found'
	else:
		content = 'Hello Web!';
	return HttpResponse(content)
