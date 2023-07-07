
from django.shortcuts import render, redirect

from .models import questions

def find_topic(tid):
	for q in questions:
		if q['id'] == tid:
			return q
	return None


def quizView(request, tid):
<<<<<<< HEAD

	request.session['level'] = 0
	request.session['topic'] = tid
	topic = find_topic(tid)

=======

	topic = find_topic(tid)

	request.session['level'] = 0
	request.session['finished'] = 0
>>>>>>> cf1ba96d7c852b6ea5e9ae86237edab57b636920
	return render(request, 'pages/question.html', {'topic' : topic, 'question' : topic['questions'][0]})



def answerView(request, tid, aid):
<<<<<<< HEAD

=======
	request.session['finished'] = 0
>>>>>>> cf1ba96d7c852b6ea5e9ae86237edab57b636920
	if request.session['topic'] != tid or request.session['level'] == -1 :
		return redirect('/cheater/')
	topic = find_topic(tid)
	level = request.session.get('level')

<<<<<<< HEAD
=======
	level = request.session['level']
	print("currently at level: ", level)
>>>>>>> cf1ba96d7c852b6ea5e9ae86237edab57b636920

	if topic['questions'][level]['correct'] == aid:
		level += 1
		request.session['level'] = level
		print("moving to level: ", level)

		if level == len(topic['questions']):
			request.session['level'] = -1
			request.session['finished'] = 1
<<<<<<< HEAD
=======
			print("level reset to: ", request.session['level'])
>>>>>>> cf1ba96d7c852b6ea5e9ae86237edab57b636920
			return redirect('/finish/')

		return render(request, 'pages/question.html', {'topic' : topic, 'question' : topic['questions'][level]})
	else:
		return redirect('/incorrect/')


def incorrectView(request):
	request.session['level'] = -1
	return render(request, 'pages/incorrect.html')


def finishView(request):
<<<<<<< HEAD

=======
>>>>>>> cf1ba96d7c852b6ea5e9ae86237edab57b636920
	try:
		if request.session['finished'] == 1:
			request.session['finished'] = 0
			return render(request, 'pages/finish.html')
		else:
			return redirect('/cheater/')
	except:
		return redirect('/cheater/')
	


def cheaterView(request):
	return render(request, 'pages/cheater.html')


def thanksView(request):
	# Like we were going to pay anyone
	return render(request, 'pages/thanks.html')



def topicView(request, tid):
	request.session['finished'] = 0
	request.session['topic'] = tid
	topic = find_topic(tid)
	return render(request, 'pages/topic.html', {'topic' : topic})


def topicsView(request):
	return render(request, 'pages/topics.html', {'questions' : questions})
