from django.urls import path
from . import views

#app_name='picnic'

urlpatterns=[
    path('',views.festival, name='festival'),
    path('dahihandi/',views.dahihandi,name='dahihandi'),
    path('republic/',views.republic,name='republic'),
    path('shivjayanti/',views.shivjayanti,name='shivjayanti'),
    path('ganpati/',views.ganpati,name='ganpati'),
    path('navratrostav/',views.devi,name='devi'),
    path('independence/',views.independence,name='independence'),
    path('holi/',views.holi,name='holi'),
]
