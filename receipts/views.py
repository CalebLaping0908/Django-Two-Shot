from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required


@login_required
def receipt_list(request):
    list = Receipt.objects.filter(purchaser=request.user)
    context = {
        "list": list,
    }
    return render(request, "receipts/home.html", context)
