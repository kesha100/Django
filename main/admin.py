from django.contrib import admin
from main.models import Film, Director
# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'duration', 'director']
    search_fields = 'id title director'.split()
    list_filter = 'title director rating duration'.split()
    list_editable = 'rating duration'.split()
    list_per_page = 100


admin.site.register(Film, FilmAdmin)
admin.site.register(Director)