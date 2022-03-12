from django.urls import path

from . import views
urlpatterns = [
    # declaring path which will take two
    # argument url name and view function

    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march)


    #seeting url and view dynamically
    path("",views.index),
    path("<int:month>",views.monthly_challenge_number),
    path("<str:month>",views.monthly_challenge,name='month-challenge')




]
