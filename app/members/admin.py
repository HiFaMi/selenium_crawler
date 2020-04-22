from django.contrib import admin
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from suit.admin import SortableModelAdmin

from suit.widgets import SuitSplitDateTimeWidget

User = get_user_model()


class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'last_login': SuitSplitDateTimeWidget,
            'date_joined': SuitSplitDateTimeWidget,
        }


class UserAdmin(SortableModelAdmin):
    readonly_fields = ('username', 'password',)
    list_display = ['username', 'user_email', 'is_superuser', 'social', 'order']
    list_editable = ('is_superuser',)
    sortable = 'order'
    form = UserChangeForm

    fieldsets = [
        (None, {
            'fields': ['username', 'user_email', 'password', 'last_login', 'date_joined',
                       'is_staff', 'is_active', ]
        })
    ]

    def suit_row_attributes(self, obj):
        css_class = {
            '1': 'success',
            '0': 'warning',
        }.get(obj.is_superuser_status)
        if css_class:
            return {'class': css_class, 'data': obj.is_superuser_status}


admin.site.register(User, UserAdmin)
