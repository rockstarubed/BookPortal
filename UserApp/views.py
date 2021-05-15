from django.shortcuts import render,redirect,HttpResponse
from UserApp.forms import UserRegisterForm,FeedbackForm
from BooksApp.models import Books
from UserApp.models import FeedBack


#Home page view
def home(request):
	books = Books.objects.all()
	return render (request, 'home.html',{'books':books})

#Signup page View
def signup(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')

	else:
		form = UserRegisterForm()
	return render (request, 'registration/signup.html',{
		'form':form
	})


#About page view
def about(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('feedback')

	else:
		form = FeedbackForm()
	return render (request, 'about.html',{
		'form':form
	})

#Feedback page View
def feedback(request):
	return render(request,'feedback.html')
	
