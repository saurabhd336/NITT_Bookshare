from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html')

# Can acces extra fields dirctly. For username use student.username or vice-versa.
def signin(request):
	if request.method == "POST":
		roll_no = request.POST.get("roll_no")
		password = request.POST.get("pass")
		student = authenticate(username = roll_no, password = password)
		return render(request, 'success.html', {'student' : student})
	return render(request, 'signin.html')

@login_required(login_url = "/signin/")
def test(request):
	return HttpResponse("This is test")