from django.shortcuts import render,redirect
from user.models import Authentication, Quotes, Userdetails



# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['yourname']
        username = request.POST['username']
        password = request.POST['password']
        user1 = Userdetails(
            name = name
        )
        user1.save()
        print(user1.id)
        common = Authentication(
            username = username,
            password = password,
            user_id =user1.id
        )
        common.save()

    return render (request,'user/signup.html')



def homepage(request):
    return render (request,'user/home.html')

def login_user(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try :
                user = Authentication.objects.get(
                username = username,
                password = password
                )

                if user.role == 'admin':
                    request.session['admin_id']=user.id 
                    return redirect('administration:quotespage')
                elif user.role == 'user':
                    request.session['user_id']=user.id
                    return redirect('user:quote')
        except : 
                msg = 'invalid username or password'
            
                
    return render (request,'user/login_user.html',{'error_msg':msg})

def logout(request) :
    del request.session['user_id']
    return redirect('user:loginuser')


def quote(request):
    if request.method == 'POST':
        new_quote = request.POST['creating_quote']
        quote1 = Quotes(
            user_id =  request.session['user_id'],
            quote = new_quote
        )
        quote1.save()        
    return render (request,'user/quote.html')


def view_quote(request):
    new_quote = Quotes.objects.all()
    return render (request,'user/viewquote.html',{'quotesList' : new_quote})

