from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import Order, User, Candidate


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created_date')


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_filter = ('presented_date',)


fields = list(UserAdmin.fieldsets)
fields[1] = (
    'Personal Info', {'fields': ('first_name',
                                 'last_name',
                                 'email',
                                 'company',
                                 'vat_no',
                                 'user_type'
                                 )})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)
