from django.contrib import admin
from .models import (Grape,
                     AboutGrape,
                     Category,
                     TagGrape,
                     History,
                     AboutHistory,
                     TagHistory)
from django.db.models import F, QuerySet
# Register your models here.


admin.site.register(AboutGrape)
admin.site.register(Category)
admin.site.register(TagGrape)
admin.site.register(AboutHistory)
admin.site.register(TagHistory)

@admin.register(Grape)
class GrapeAdmin(admin.ModelAdmin):
    list_display = ["name_eng", "area", "slug"]  #
    list_editable = ["area"]  #
    # ordering = ["name_eng"]
    list_per_page = 20
    prepopulated_fields = {"slug": ("name_eng",)}
    filter_horizontal = ['tags', ]


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ["story_name", "slug"]
    # list_editable = ["area"]  #
    # ordering = ["name_eng"]
    list_per_page = 20
    prepopulated_fields = {"slug": ("story_name",)}
    filter_horizontal = ['tags', ]