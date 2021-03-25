from django.contrib import admin
from score.models import Scores


# Register your models here.

class ScoresAdmin(admin.ModelAdmin):
    pass


admin.site.register(Scores, ScoresAdmin)
