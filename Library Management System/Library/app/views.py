from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Book  # import model here Book for addbook views
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,"home.html")


def addbook(request):
    return render(request,"addbook.html")    


def allbook(request):
    books=Book.objects.all()
    return render(request,"allbook.html",{"books":books})    

def view(request):
    if request.method=="POST":
        student_name=request.POST["student_name"]
        enrollment=request.POST["enrollment"]
        book_name=request.POST["book_name"]
        author_name=request.POST["author_name"]
        issued_date=request.POST["issued_date"]
        expiry_date=request.POST["expiry_date"]
        fine=request.POST["fine"]
        print(student_name,enrollment,book_name,author_name,issued_date,expiry_date,fine)
        book=Book()
        book.student_name=student_name
        book.enrollment=enrollment
        book.book_name=book_name
        book.author_name=author_name
        book.issued_date=issued_date
        book.expiry_date=expiry_date
        book.fine=fine
        book.save()   #save model
        return HttpResponseRedirect('/')

    
def editbook(request):
    if request.method=="POST":
        student_name=request.POST["student_name"]
        enrollment=request.POST["enrollment"]
        book_name=request.POST["book_name"]
        author_name=request.POST["author_name"]
        issued_date=request.POST["issued_date"]
        expiry_date=request.POST["expiry_date"]
        if expiry_date:
            expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').date()
        else:
            expiry_date = None 
        fine=request.POST["fine"]
        book=Book.objects.get(id=request.POST['bid'])
        book.student_name=student_name
        book.enrollment=enrollment
        book.book_name=book_name
        book.author_name=author_name
        book.issued_date=issued_date
        book.expiry_date=expiry_date
        book.fine=fine
        book.save()   #save model
        return HttpResponseRedirect('/allbook')
     
    
def editbookview(request):
    book=Book.objects.get(id=request.GET['bookid'])
    print(book)
    return render(request,"edit-book.html",{"book":book})


def deletebookview(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/allbook')
