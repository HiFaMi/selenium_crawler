from django.contrib import admin
from django.contrib.auth import get_user_model
from suit.admin import SortableModelAdmin

User = get_user_model()


class UserAdmin(SortableModelAdmin):
    list_display = ['username', 'user_email', 'is_superuser', 'order']
    list_editable = ('order',)
    sortable = 'order'


admin.site.register(User, UserAdmin)
