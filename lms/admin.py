from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Issue, Waitlist


# Register your models here.
@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    pass


@admin.register(Book)
class PartyAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)


@admin.register(Issue)
class GiftAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)


@admin.register(Waitlist)
class GuestAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)
