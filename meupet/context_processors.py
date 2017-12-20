from .models import Song


def pets_count(request):
    return {
        'pets_count': Song.objects.count(),
    }
