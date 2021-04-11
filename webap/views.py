import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .forms import SignUpForm


# Create your views here.
class WebAppIndex(View):
    template_name = "webap/index.html"
    form_class = SignUpForm

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        url = "https://goquotes-api.herokuapp.com/api/v1/random?count=1"
        rq = requests.get(url)
        quote_body = rq.json()
        data = {
            "text": quote_body["quotes"][0]["text"],
            "author": quote_body["quotes"][0]["author"],
        }

        html_data = f"""
        <em>{ data['text'] }</em><br/>
        -- <b>{ data['author'] }</b>
        """

        return HttpResponse(html_data, status=200)
