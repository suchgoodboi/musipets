from django.contrib import admin

from meupet import models


class SongAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'group',
        'description',
    )
    # list_filter = (
    #     'status',
    #     'kind',
    #     'created',
    #     'active',
    # )


admin.site.register(models.Song, SongAdmin)
admin.site.register(models.Group)