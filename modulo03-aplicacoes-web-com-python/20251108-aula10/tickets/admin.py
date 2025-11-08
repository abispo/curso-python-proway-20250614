from django.contrib import admin

from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "status", "created_at")
    list_filter = ("status", "owner",)
    search_fields = ("title", "description",)
    ordering = ("-created_at",)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.groups.filter(name="suporte").exists():
            return queryset
        
        return queryset.filter(owner=request.user)