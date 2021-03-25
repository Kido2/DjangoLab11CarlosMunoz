from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Scores
import datetime


# Create your views here.
class ScoresView(View):
    def get(self, *args):
        score = Scores.objects.get(pk=1)
        return HttpResponse(f"<p>De parte: {score.origin} y fecha {score.date} con score {score.score}</p>")

    def public(self):
        d = datetime.date(2021, 3, 19)
        return {
            "score": 100,
            "origin": 'Carlos Andres',
            "date": f"{d}",
        }
