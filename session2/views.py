from django.shortcuts import render

def index(request):
    
    data = {
        "name": 'afd',
        "students": [
            "yemen",
            "selem",
            "sdfgh"
        ]
    }
    return render(request, 'index2.html', data)