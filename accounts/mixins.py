from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect, render

# Only superusers, managers
class AdminAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not (user.is_superuser or user.is_manager):
            return render(request, 'error_pages/page_403.html',status=403)
        return super().dispatch(request, *args, **kwargs)