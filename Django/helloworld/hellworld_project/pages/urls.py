from django.urls import path

from .views import homepageView

urlpatterns = [path("", homepageView, name="home")]

# path(regex for teh empty string, view function, optinal name for the url)
# Here, we are saying if the user requested the home page represented teh empyt string uer the view called homepageview
