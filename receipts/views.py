from django.shortcuts import render, redirect
from receipts.models import Receipt, Account, ExpenseCategory
from receipts.forms import ReceiptForm, CategoryForm, AccountForm
from django.contrib.auth.decorators import login_required


@login_required
def receipt_list(request):
    if request.user.is_authenticated:
        list = Receipt.objects.filter(purchaser=request.user)
    else:
        list = Receipt.objects.none
    context = {
        "list": list,
    }
    return render(request, "receipts/home.html", context)


def category_list(request):
    if request.user.is_authenticated:
        list = ExpenseCategory.objects.filter(owner=request.user)
    else:
        list = ExpenseCategory.objects.none
    context = {
        "list": list,
    }
    return render(request, "receipts/category.html", context)


def account_list(request):
    if request.user.is_authenticated:
        list = Account.objects.filter(owner=request.user)
    else:
        list = Account.objects.none
    context = {
        "list": list,
    }
    return render(request, "receipts/account.html", context)


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


@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            owner = form.save(commit=False)
            owner.owner = request.user
            owner.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }

    return render(request, 'receipts/create_category.html', context)


@login_required
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            owner = form.save(commit=False)
            owner.owner = request.user
            owner.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    context = {
        'form': form,
    }

    return render(request, 'receipts/create_account.html', context)
