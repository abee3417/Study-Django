from django.shortcuts import render, redirect
from .models import CustomUser

# Create your views here.

def index(request):
    return render(request, 'pybo/main.html')

def login(request):
    return render(request, 'pybo/login.html')

def signup(request):
    return render(request, 'pybo/signup.html')

def signup_func(request):
    if request.method == "POST":
        newUser = CustomUser(username=request.POST.get('username'), password=request.POST.get('password'))
        for cus in CustomUser.objects.all():
            if newUser.username == cus.username:
                context = {'err': '동일 유저 존재'}
                return render(request, 'pybo/signup.html', context)
        newUser.save()
        return redirect('pybo:main')

def login_func(request): #로그인 가능 여부를 확인
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST.get('password')
        '''
        id = request.POST['username']
        pw = request.POST['password']
        try:
            user = CustomUser.objects.filter(username=id).get(password=pw)
        except:
            user = None
        if user:
            로그인성공
        else:
            로그인실패, redirect
        
        
        '''
        for cus in CustomUser.objects.all():
            if username == cus.username:
                if password == cus.password:
                    return redirect('pybo:main')
                else:
                    context = {'err': '비밀번호 틀림'}
                    return render(request, 'pybo/login.html', context)

        context = {'err': '아이디 틀림'}
        return render(request, 'pybo/login.html', context)
