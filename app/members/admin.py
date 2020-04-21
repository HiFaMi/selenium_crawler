from django.contrib import admin
from django.contrib.auth import get_user_model
from suit.admin import SortableModelAdmin

User = get_user_model()


class UserAdmin(SortableModelAdmin):
    list_display = ['username', 'user_email', 'is_superuser', 'social', 'order']
    list_editable = ('is_superuser',)
    sortable = 'order'

    def suit_row_attributes(self, obj):
        css_class = {
            '1': 'success',
            '0': 'warning',
        }.get(obj.is_superuser_status)
        if css_class:
            return {'class': css_class, 'data': obj.is_superuser_status}


admin.site.register(User, UserAdmin)
