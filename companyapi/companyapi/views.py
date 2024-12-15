from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("home page reuqest")
    friend=[
        "asaht",
        "bhiyu",
        "dsjad",
    ]
    # return HttpResponse("this is home page")
    return JsonResponse(friend,safe=False)
