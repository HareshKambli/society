from django.urls import path
from . import views

#app_name='picnic'

urlpatterns=[
    path('',views.picnic, name='picnic'),
    path('rajgad/',views.rajgad,name='rajgad'),
    path('shivneri/',views.shivneri,name='shivneri'),
    path('raigad/',views.raigad,name='raigad'),
    path('malvan/',views.malvan,name='malvan'),
    path('harihareshwar/',views.harihareshwar,name='harihareshwar'),
    path('khopoli/',views.khopoli,name='khopoli'),
    path('malvali/',views.malvali,name='malvali'),
    path('vijaydurga/',views.vijaydurga,name='vijaydurga'),
]
