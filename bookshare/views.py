from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
	return render(request, 'index.html')

# Can acces extra fields dirctly. For username use student.username or vice-versa.
def signin(request):
	if request.method == "POST":
		roll_no = request.POST.get("roll_no")
		password = request.POST.get("pass")
		student = authenticate(username = roll_no, password = password)
		if student != None:
			student.user.backend = 'django.contrib.auth.backends.ModelBackend'
			login(request, student.user)
			return render(request, 'success.html')
		else:
			return render(request, 'signin.html', 
				{'error' : "Invalid credentials or webmail is down. Please try again"})
	return render(request, 'signin.html')

def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
	return HttpResponse("You are logged out")


def test(request):
	if request.user.is_authenticated():
		return HttpResponse("This is test")
	return HttpResponse("This is not test")
	