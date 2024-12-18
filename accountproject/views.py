from django.shortcuts import render

def MainIndex(request):
	return render(request, 'mainindex.html', context={})
