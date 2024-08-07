from django.urls import path
from todoList.views import *

app_name = 'todoList'
urlpatterns = [
    path('', homePage, name="homePage"),
    path('noteAdd', noteAdd, name="noteAdd"),
    path('noteUpdate', noteUpdate, name="noteUpdate"),
    path('noteDelete', noteDelete, name="noteDelete"),
    path('markStar', markStar, name="markStar"),
    path('removeStar', removeStar, name="removeStar"),

    # Common Buttons
    path('enableBold', enableBold, name="enableBold"),
    path('disableBold', disableBold, name="disableBold"),
    path('enableItalic', enableItalic, name="enableItalic"),
    path('disableItalic', disableItalic, name="disableItalic"),
    path('enableUnderline', enableUnderline, name="enableUnderline"),
    path('disableUnderline', disableUnderline, name="disableUnderline"),
    path('enableStrikeThrough', enableStrikeThrough, name="enableStrikeThrough"),
    path('disableStrikeThrough', disableStrikeThrough, name="disableStrikeThrough"),
    path('disableBackgroundColor', disableBackgroundColor, name="disableBackgroundColor"),
]

from django.contrib import admin
admin.site.site_header = 'DOTO Stack Admin Panel'                    # default: "Django Administration"
admin.site.index_title = 'DOTO list site administration'                 # default: "Site administration"
admin.site.site_title = 'Django crud admin'  # default: "Django site admin"
