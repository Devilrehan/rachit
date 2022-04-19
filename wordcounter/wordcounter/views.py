from cgitb import text
from multiprocessing import context
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def show(request):
    text = request.GET['usertext']
    totalwords = len(text.split(' '))
    totalletters = len(text)

    vowelcount = 0
    consonantcount = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in text:
        if i in vowels:
            vowelcount += 1
        else:
            consonantcount += 1

    context = {
       'text' : text,
       'words' : totalwords,
       'letters': totalletters,
       'vowels' : vowelcount,
       'consonants': consonantcount   
}
    return render(request, 'show.html', context)
