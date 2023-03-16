from django.shortcuts import render

# Create your views here.
def ifcond(request):
    d={'a':100}
    return render(request,'ifcond.html',d)
def elifcond(request):
    d={'a':10,'b':22,'c':23}
    return render(request,'elifcond.html',d)
def nestedif(request):
    d={'a':10,'b':22,'c':23}
    return render(request,'nestedif.html',d)
def forloop(request):
    d={'love':'TEJU'}
    return render(request,'forloop.html',d)

