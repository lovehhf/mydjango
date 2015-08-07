from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def blog_index(request):
	context = {
		'test': 'just for a test.',
		'welcome': 'Hello World.'
}
	return render(request,'blog_index.html',context)
