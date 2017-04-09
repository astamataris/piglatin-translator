from django.http import HttpResponse
from django.shortcuts import render

# def hello(request):
# 	return HttpResponse("Hello World!")

def home(request):
	return render(request, 'home.html')

def translate(request):

	original = request.GET['originaltext'].lower()

	originalList = original.split()

	translation = ''

	for word in original.split():
		if word[0] in ["a", "e", "i", "o", "u"]:
			#vowel
			translation += word  #+"yay "
			translation += 'yay '
		else:
			# consonant
			translation += word[1:]
			translation += word[0]
			translation += 'ay '

	return render(request,'translate.html',{'original':original, 'translation': translation})

def about(request):
	return render(request, 'about.html')

def newpage(request):
	return render(request, 'new_page.html')