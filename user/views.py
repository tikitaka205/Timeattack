from django.shortcuts import render, redirect

#로그인 요구
from django.contrib.auth.decorators import login_required

#회원가입시 필요
from .models import UserModel

#로그인시 필요
from django.contrib import auth



# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        UserModel.objects.create_user(
        username=username,
        password=password,
        phone=phone,
        address=address,
        )
        return redirect('/login/')
#에러 나타내기 redirect사용법 로그아웃
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        # 입력란 빈칸일때
        if username == '':
            return render(request, 'login.html', {'error': '아이디를 입력해주세요.'})
        elif password == '':
            return render(request, 'login.html', {'error': '패스워드를 입력해주세요.'})

        # User 인증 함수
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 로그인 처리
            user = request.user
            return redirect('/home/')
        else:
            print('로그인 실패')
            return render(request, 'user/login.html', {'error': '유저 정보를 찾을 수 없습니다.'})

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

#로그아웃
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login/')