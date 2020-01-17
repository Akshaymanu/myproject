from django.shortcuts import render

# Create your views here.

def indexPage(request):
    return render(request,'index.html')

def mycss(request):
    return render(request,'mycss.html')  

def html_1(request):
    return render(request,'html_assg1.html')

def html_2(request):
    return render(request,'html_assg2.html')    

def html_3(request):
    return render(request,'html_assg3.html')

def html_4(request):
    return render(request,'html_assg4.html')

def html_5(request):
    return render(request,'html_assg5.html')

def html_6(request):
    return render(request,'html_assg6.html')

def html_7(request):
    return render(request,'html_assg7.html')     

def html_8(request):
    return render(request,'html_assg8.html')       

def html_9(request):
    return render(request,'html_assg9.html')    