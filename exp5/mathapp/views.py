from django.shortcuts import render

def surfacearea(request):
    context={}
    context['area'] = "0"
    context['r'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        r = request.POST.get('radius','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('Radius=',r)
        print('Height=',h)
        area = 2*3.14*int(r)*(int(h)+int(r))
        context['area'] = area
        context['r'] = r
        context['h'] = h
        print('Surface Area =',area)
    return render(request,'mathapp/math.html',context)