from django.urls import path
from . import views

# URL Patterns
urlpatterns = [
    path(route="signup", view=views.signup, name="signup"),
    path(route="signin", view=views.signin, name="signin"),
    path(route="signout", view=views.signout, name="signout"),
    path(route="password_reset", view=views.password_reset, name="password_reset")
]