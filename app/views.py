from django.http import HttpResponse
import requests

from .helpers import LimitSize
from django.shortcuts import render
from django.views import View

class MainView(View):
    def get(self, request):
        data = request.META
        return HttpResponse(data)

class UserView(View):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        pages = requests.get(f"http://127.0.0.1:8008/users?size=3").json()["pages"]

        if int(page) <= int(pages):

            if page is None:
                data = requests.get(f"http://127.0.0.1:8008/users?size={LimitSize}").json()["items"]
                return render(request, "users.html", context={"users": data, "pages": pages, "page": 1, "next": 2, "previous": 0})


            data = requests.get(f"http://127.0.0.1:8008/users?page={page}&size={LimitSize}").json()["items"]
            return render(request, "users.html", context={"users": data, "pages": pages, "page": page, "next": int(page) + 1, "previous": int(page) - 1})

        return render(request, "users.html", context={"message": "Not found"})








