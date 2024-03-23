from django.http import HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# https://www.cnblogs.com/zqifa/p/django-csrf-1.html

@csrf_exempt
def gpu_info(request):
    post_data: dict = dict(request.POST)

    print(post_data)
    print(type(post_data))

    # print(request.GET)
    # print(type(request.GET))

    return HttpResponse("111")
