from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
	return render(request, 'myauth/index.html')


def login(request):
	if request.method == 'POST':
		user = authenticate(request, username=request.POST['用户名'], password=request.POST['密码'])
		if user is None:
			return render(request, 'myauth/login.html', {'错误': '用户名不存在！'})
		else:
			login(request, user)
			return redirect('myauth:主页')
	else:
		return render(request, 'myauth/login.html')


def logout(request):
	logout(request)
	return redirect('myauth:主页')





