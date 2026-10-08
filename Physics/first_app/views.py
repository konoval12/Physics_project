from django.shortcuts import render

def my_page(request):
    context = {
        "name": "Леня",
        "age": 17
    }
    return render(request, "mypage.html", context)