from django.http import HttpResponse
from django.shortcuts import render

import operator

def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionnary = {}
    for word in wordlist:
        if word in worddictionnary:
            #increase
            worddictionnary[word] += 1
        else:
            #add to the worddictionnary
            worddictionnary[word] = 1

    sortedwords = sorted(worddictionnary.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'worddictionnary':sortedwords})
