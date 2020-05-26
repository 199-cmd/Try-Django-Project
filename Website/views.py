from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
	#return HttpResponse("Hello this is index page")
	return render(request,'index.html')
