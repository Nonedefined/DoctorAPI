from django.contrib import admin

from main.models import Direction, Doctor


@admin.register(Direction)
class DirectionModel(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Doctor)
class DoctorModel(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', 'directions', 'experience')
    search_fields = ('name', )
    ordering = ('sort_number', 'name')


