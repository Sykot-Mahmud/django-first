import imp
from lib2to3.pgen2.literals import evalString
from re import A
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": 'Eat no meat for this month!',
    "february": "Work For at least 20 minutes!",
    "march": "Learn Django at least 20 minutes",
    "april": 'Eat no meat for this month!',
    "may": "Work For at least 20 minutes!",
    "june": "Learn Django at least 20 minutes",
    "july": 'Eat no meat for this month!',
    "august": "Work For at least 20 minutes!",
    "september": "Learn Django at least 20 minutes",
    "october": 'Eat no meat for this month!',
    "november": "Work For at least 20 minutes!",
    "december": None

}
# Create your views here.

def index(request):
    months=list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months":months

    })

    # for month in months:
    #     capitalized_month=month.capitalize()
    #     month_path=reverse("month-challenge",args=[month])
    #     list_items+=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data=f"<ul>{list_items}</ul>"
    #hardcoded Response
    # response_data="""
    # <ul>
    # <li><a href="/challenges/january">January</a></li>
    # <li><a href="/challenges/february">February</a></li>
    # <li><a href="/challenges/march">March</a></li>
    # <li><a href="/challenges/april">April</a></li>
    # <li><a href="/challenges/may">May</a></li>
    # <li><a href="/challenges/june">June</a></li>
    # <li><a href="/challenges/july">July</a></li>
    # <li><a href="/challenges/august">August</a></li>
    # <li><a href="/challenges/september">September</a></li>
    # <li><a href="/challenges/october">October</a></li>
    # <li><a href="/challenges/november">November</a></li>
    # <li><a href="/challenges/december">December</a></li>
    # </ul>
    # """
    # return HttpResponse(response_data)


# def january(request):
#     return HttpResponse("Eat no meat for this month!")


# def february(request):
#     return HttpResponse("Work For at least 20 minutes!")

# def march(request):
#     return HttpResponse("Learn Django at least 20 minutes")


def monthly_challenge_number(request, month):
    months=list(monthly_challenges.keys())
    if (month>len(months))or (month==0):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
   
    
    redirected_month=months[month-1]
    redirected_path=reverse("month-challenge",args=[redirected_month])

    return HttpResponseRedirect(redirected_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,
            "month_name":month
        })
        # response_data=render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

    except:
        # response_data= render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404("")