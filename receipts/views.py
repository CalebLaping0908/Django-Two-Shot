from django.shortcuts import render
from receipts.models import Receipt


def receipt_list(request):
    list = Receipt.objects.all()
    context = {
        "list": list,
    }
    return render(request, "receipts/home.html", context)
