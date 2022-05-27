from .querysSparql import Eventos
from django.shortcuts import render
from json import dumps


def index(request):
    return render(request, "index.html")


def eventos(request):
    eventoAux = Eventos()
    if request.method == "POST":
        if request.POST["action"] == "1":  # Búsqueda sólo por nombre de colegio
            evento = request.POST["nombreEvento"]
            nameEventos = eventoAux.nombreEvento(evento)
            return render(request, "eventos.html",
                          {'nEventos': len(nameEventos), 'colList': nameEventos, 'jsonList': dumps(nameEventos),
                           'action': 1})
    return render(request, "eventos.html", {'nEventos': -1})

