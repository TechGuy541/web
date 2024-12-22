from django.shortcuts import render

# Create your views here.
def home(request):
    page_background = 'bg-gradient-to-tl from-melonx-red to-melonx-gray animate-mesh-gradient bg-[length:200%_200%]'

    context = {
        'page_background': page_background,
    }

    return render(request, 'home/index.html', context)