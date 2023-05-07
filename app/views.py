from django.shortcuts import render

# Create your views here.
def Built_in_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'Hai hoW aRe YoU','dt':dt,'c':1}
    return render(request,'Built_in_filters.html',d)