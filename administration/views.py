from django.shortcuts import render,redirect

from user.models import Quotes

# Create your views here.
def index(request):
    quotes = Quotes.objects.all()
    
    return render (request,'admin/quotespage.html',{'quotesList' : quotes})

def logout(request) :
    del request.session['admin_id']
    return redirect('user:loginuser')

def approve(request,uid):
    quotes = Quotes.objects.all()
    data = Quotes.objects.filter(id = uid)
    data.update(status='approve')
    return render (request,'admin/quotespage.html',{'quotesList' : quotes})


