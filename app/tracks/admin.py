from django.contrib import admin
from .models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'created_at', 'modified_at')
    list_filter = ('created_at', 'modified_at')

    class Meta:
        model = Track


admin.site.register(Track, TrackAdmin)
