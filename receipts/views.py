from django.shortcuts import render
from receipts.models import Receipt

# from django.contrib.auth.decorators import login_required


def receipt_list(request):
    if request.user.is_authenticated:
        list = Receipt.objects.filter(purchaser=request.user)
    else:
        list = Receipt.objects.none
    context = {
        "list": list,
    }
    return render(request, "receipts/home.html", context)
