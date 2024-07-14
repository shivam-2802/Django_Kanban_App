from django.contrib import admin
from .models import ToDoCard, DoingCard, DoneCard

@admin.register(ToDoCard)
class ToDoCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    

@admin.register(DoingCard)
class DoingCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    

@admin.register(DoneCard)
class DoneCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
