from django.contrib.admin import site, ModelAdmin
from todoList.models import noteModel # Register your models here.


class noteModelList(ModelAdmin):
    list_display = (
        'noteStar',
        'noteStyle',
        'noteBold',
        'noteItalic',
        'noteUnderline',
        'noteTextColor',
        'noteBackgroundColor'
    )


site.register(noteModel, noteModelList)
