from django.shortcuts import render
from .models import Student

# Create your views here.
def Main(request):
	if request.POST:
		model = Student()
		model.name = request.POST['name']
		model.surname = request.POST['surname']
		model.email = request.POST['email']
		model.password = request.POST['password']
		model.save()
		print(request.POST)
	return render(request, 'index.html')
def Royxat(request):
	queryset = Student.objects.all().order_by('-name')
	return render(request, 'main.html', {'royxat':queryset})