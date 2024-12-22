from django.shortcuts import render, redirect
from .models import GameEntry
from django.contrib import messages

# Create your views here.
def home(request):
    compatibility_filter = request.GET.get('compatibility')
    ram_filter = request.GET.get('ram')
    search_query = request.GET.get('search', '')

    game_entry = GameEntry.objects.all().order_by('-entry').filter(published=True)

    if compatibility_filter:
        game_entry = game_entry.filter(compatibility=compatibility_filter, published=True)
    if ram_filter:
        game_entry = game_entry.filter(device_memory=ram_filter, published=True)
    if search_query:
        game_entry = game_entry.filter(name__icontains=search_query, published=True)

    page_background = 'bg-gradient-to-tl from-melonx-red to-melonx-gray animate-mesh-gradient bg-[length:200%_200%]'

    total_games = GameEntry.objects.count()

    status_counts = {status[0]: GameEntry.objects.filter(compatibility=status[0]).count() for status in GameEntry.COMPATIBILITY_STATUS}

    status_percentages = {
        status: (count / total_games * 100) if total_games > 0 else 0
        for status, count in status_counts.items()
    }

    context = {
        'page_background': page_background,
        'game_entry': game_entry,
        'status_percentages': status_percentages,
        'compatibility_filter': compatibility_filter,
        'ram_filter': ram_filter,
        'search_query': search_query,
        'compatibility_choices': GameEntry.COMPATIBILITY_STATUS,
        'ram_choices': GameEntry.RAM_CHOICES,
    }

    return render(request, 'compatibility/index.html', context)

def request_game_entry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        game_id = request.POST.get('game_id')
        description = request.POST.get('description')
        compatibility = request.POST.get('compatibility')
        device_memory = request.POST.get('device_memory')
        video = request.POST.get('video')

        GameEntry.objects.create(
            name=name,
            game_id=game_id,
            description=description,
            compatibility=compatibility,
            device_memory=device_memory,
            video=video,
        )
        messages.success(request, 'Game entry successfully added!')
        return redirect('compatibility:home')
    
    page_background = 'bg-gradient-to-tl from-melonx-red to-melonx-gray animate-mesh-gradient bg-[length:200%_200%]'

    context = {
        'page_background': page_background,
        'compatibility_choices': GameEntry.COMPATIBILITY_STATUS,
        'ram_choices': GameEntry.RAM_CHOICES,
    }
    
    return render(request, 'compatibility/request_game_entry.html', context)
