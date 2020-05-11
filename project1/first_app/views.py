from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,Users
from . import forms



from first_app import views
# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    return render(request,'first_app/index.html',context=date_dict)
def customers(request):
    cus_list = Users.objects.all()
    dic = {'cus_list':cus_list}
    return render(request,'first_app/customers.html',context=dic)

def formpage(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("data")
            print("name: "+form.cleaned_data['name'])
            print("email: " + form.cleaned_data['email'])
            print("text: " + form.cleaned_data['text'])
    return render(request,'first_app/form_page.html',{'form_dict':form})
def signup(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        if form.is_valid():
            print("name: "+form.cleaned_data['first_name'])
            print("email: "+form.cleaned_data['last_name'])
            print("email: " + form.cleaned_data['email'])
            form.save(commit=True)
            return index(request)
    return render(request,'first_app/signup.html',{'signup_form':form})
def login(request):
    form = forms.login()
    if request.method == "POST":
        form = forms.login(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            users_list = Users.objects.all()
            for users in users_list:
                if fname.lower() == users.first_name.lower() and lname.lower() == users.last_name.lower() and email.lower() == users.email.lower():
                    return index(request)
            return HttpResponse("<h1>no account found</h1>")
    return render(request,'first_app/login.html',{'login':form})

