from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.urls import reverse
from django.utils.html import escape
from django.middleware.csrf import get_token

# Create your views here.
def home(request): 
    return HttpResponse(
        "<h1>Welcome to PyLab!</h1>"
        "<p>Learn NumPy, Pandas and python with us.</p>"
    )

@login_required
def student_dashboard(request):
    username = escape(request.user.username)

    logout_url = reverse("logout")
    csrf_token = get_token(request)

    html = f"""
        <h1>Welcome to your dashboard, {username}!</h1>

        <p>You are currently logged in.</p>

        <form action="{logout_url}" method="post">
            <input type="hidden"
                   name="csrfmiddlewaretoken"
                   value="{csrf_token}">

            <button type="submit">Logout</button>
        </form>
    """

    return HttpResponse(html)

