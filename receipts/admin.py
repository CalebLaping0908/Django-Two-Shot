from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt


@admin.register(ExpenseCategory)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "id",
    )


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "id",
    )


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "vendor",
        "date",
        "id",
    )
