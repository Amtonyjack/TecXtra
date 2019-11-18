from django.urls import path
from .import views
urlpatterns=[
    path('',views.index, name='main'),
    path('cover/',views.cover, name="cover"),
    path('organisars/',views.organisars, name="organisars"),
    path('contstant/',views.contstant, name="contstant"),
    path('staff/',views.staff, name="staff"),
    path('progress/', views.progress, name="progress"),
    path('marks/', views.marks , name="marks"),
    path('getmarks/', views.getmarks, name="getmarks"),
    path('ranks/', views.ranks, name="ranks")



]