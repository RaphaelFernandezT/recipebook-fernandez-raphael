from django.shortcuts import render

def homepage(request):
    return render(request, "ledger/homepage.html")

