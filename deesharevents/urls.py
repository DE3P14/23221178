from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
      path('events/',views.events,name='events'),
       path('events/booking/',views.booking,name='booking'),
        path('events/booking/confirm/',views.confirm,name='confirm'),
        path('events/booking/confirm/payment/',views.payment,name='payment'),
]
