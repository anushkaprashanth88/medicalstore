from django.shortcuts import render
from .models import *
from django.db.models import Max


# Create your views here.
def index(request):
    return render(request, './myapp/index.html')

def user(request):
    return render(request, './myapp/user.html')

def admindashboard(request):
    return render(request, './myapp/admindashboard.html')

def login(request):
    return render(request, './myapp/login1.html')



def registration(request):
    return render(request, './myapp/registration.html')





def login_action(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        pwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')
        ub = user_login.objects.filter(uname=un, passwd=pwd, u_type='user')
        #user_type = userlogin.objects.filter(user_type = 'user')
        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request, './myapp/admindashboard.html')

        elif len(ub) == 1:
            request.session['user_name'] = ub[0].uname
            request.session['user_id'] = ub[0].id
            context1 = {'uname': request.session['user_name' ]}
            return render(request, './myapp/user.html', context1)

        else:


            context ={ 'msg1':'Invalid username and password'}
            return render(request, './myapp/login1.html',context)

    else:
        return render(request, './myapp/login1.html')


def user_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')


        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        con = request.POST.get('country')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        email = request.POST.get('email')


        #status = "new"

        if user_login.objects.filter(uname=email):
            msg = {'msg1' : 'already username exits'}
            return render(request, './myapp/registration.html', msg)
        else:


            ul = user_login(uname=email, passwd=password, u_type='user')
            ul.save()
            user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

            ud = user_details(user_id=user_id,fname=fname, lname=lname, addr=addr,pin=pin, contact=contact, email=email, country=con)
            ud.save()


            context = {'msg': 'User Registered'}
            return render(request, 'myapp/login1.html',context)

    else:
        return render(request, 'myapp/registration.html')
