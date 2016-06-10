from django.shortcuts import render
from django.contrib.auth import authenticate

def index(request):
	return render(request, 'index.html')

def signin(request):
	if request.method == "POST":
		roll_no = request.POST.get("roll_no")
		password = request.POST.get("pass")
		user = authenticate(username = roll_no, password = password)
		if user == None:
			return render(request, 'profile.html')
		return render(request, 'success.html')
	return render(request, 'signin.html')