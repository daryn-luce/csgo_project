from django.shortcuts import render
import random


locations = ["van", "bench", "window", "ticket", "stairs", "ramp"]
random.shuffle(locations)


def home(request):
    context = {
        'title': 'Home',
        'locations': locations,
    }
    return render(request, 'callout/index.html', context)
