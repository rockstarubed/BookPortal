from django.shortcuts import render,redirect
from . models import Books
from . forms import UploadForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# book upload form view
@login_required
def upload(request):
 	if request.method == 'POST':
 		form = UploadForm(request.POST,request.FILES)
 		if form.is_valid():
 			fs = form.save(commit=False)
 			fs.uploadedby = request.user.username
 			form.save()
 			return redirect('home')
 	else:
 		form = UploadForm()
 	return render(request,'books/uploadbook.html',{'form':form})


# books uploaded by user view
@login_required
def viewbooks(request):
	books = Books.objects.filter(uploadedby=request.user.username)
	return render(request,'books/viewbooks.html', {'books':books})

@login_required
def editbook(request,pk):
	book = Books.objects.get(pk=pk)
	form = UploadForm(instance=book)
	if request.method == 'POST':
		updateBook = UploadForm(request.POST,instance=book)
		if updateBook.is_valid():
			updateBook.save()
			messages.success(request,"Data has been updated.")
			return redirect('viewbooks')
	return render(request,'books/editbook.html',{'form':form, 'book':book})


# delete books view
@login_required
def deletebook(request,pk):
	if request.method == 'POST':
		book = Books.objects.get(pk=pk)
		book.delete()
	return redirect('viewbooks')
