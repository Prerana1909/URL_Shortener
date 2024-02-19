from django.http import HttpResponse
from django.shortcuts import render

from .models import LongToShort

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, world.")

def home_page(request):
    context = {
        "submitted": False,
        "error": False
    }

    if request.method == 'POST':
        #context['submitted'] = True

        data = request.POST #dict
        long_url = data['longurl']
        custom_name = data['custom_name']
        #print(long_url)
        #print(custom_name)
        #print(request.POST)

        try:
              obj = LongToShort(long_url = long_url, short_url = custom_name)
              obj.save()



              date = obj.date
              clicks = obj.clicks

              context["long_url"] = long_url
              context["short_url"] = custom_name
              context["date"] = date
              context["clicks"] = clicks
              context["submitted"] = True
              """context = {
        "submitted": True
    }"""
        except:
            context["error"] = True

    else:
        print("Enter Value")


    #print(request.method)
    return render(request, "index.html", context)

def analytics_page(request):
    return render(request, 'analytics.html')

def task_page(request):
    context = {
        "my_name":"Prerana"
    }
    return render(request, 'task.html', context)

def all_analytics(request):
    context = {
        "submitted": False,
        "error": False
    }

    if request.method == 'POST':
        # context['submitted'] = True

        data = request.POST  # dict
        long_url = data['longurl']
        custom_name = data['custom_name']
        # print(long_url)
        # print(custom_name)
        # print(request.POST)

        try:
            obj = LongToShort(long_url=long_url, short_url=custom_name)
            obj.save()

            date = obj.date
            clicks = obj.clicks

            context["long_url"] = long_url
            context["short_url"] = custom_name
            context["date"] = date
            context["clicks"] = clicks
            context["submitted"] = True
            """context = {
      "submitted": True
  }"""
        except:
            context["error"] = True

    else:
        print("Enter Value")

    # print(request.method)


    return render(request, 'all-analytics.html', context)