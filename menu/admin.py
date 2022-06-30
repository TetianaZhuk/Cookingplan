from django.contrib import admin

# Register your models here.
from menu.models import Day


class DayAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('date',)}


admin.site.register(Day, DayAdmin)

