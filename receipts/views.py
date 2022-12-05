from django.shortcuts import render, redirect, get_object_or_404
from receipts.models import Receipt
from receipts.forms import ReceiptForm
from django.contrib.auth.decorators import login_required


def receipt_list(request):
    if request.user.is_authenticated:
        list = Receipt.objects.filter(purchaser=request.user)
    else:
        list = Receipt.objects.none
    context = {
        "list": list,
    }
    return render(request, "receipts/home.html", context)


@login_required
def create_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            purchaser = form.save(commit=False)
            purchaser.purchaser = request.user
            purchaser.save()
            return redirect('home')
    else:
        form = ReceiptForm()
    context = {
        'form': form,
    }

    return render(request, 'receipts/create.html', context)
