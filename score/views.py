from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Scores


# Create your views here.
class ScoresView(View):
    def get(self, *args):
        score = Scores.objects.get(pk=1)
        return HttpResponse(f"<p>Respuesta: {score.predict}</p>")

    def public(self):
        return {
            "score": 100,
            "origin": 'Carlos Andres',
        }
