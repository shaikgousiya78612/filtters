from django.shortcuts import render

# Create your views here.
def builtin_filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'hAi Gousiya HOW r You Welcome To the NEw Year','dt':dt,'c':5}
    return render(request,'builtin_filters.html',d)




def user_define_f(request):
    d={'data':'HI Python HoW R yoU'}
    return render(request,'user_define_f.html',d)