from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from core.forms import CustomUserCreationForm, CustomUserChangeForm
from core.models import CustomUser, Company


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]


# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)
admin.site.register(Company)
