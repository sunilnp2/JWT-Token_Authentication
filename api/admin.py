from django.contrib import admin
from api.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):

    list_display = ('id','username','profile', 'is_admin')
    list_display_links = ('id','username','profile', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('profile',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)