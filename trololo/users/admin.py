from django.contrib import admin
from users.models import TrololoUser

class TrololoUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'first_name', 'last_name', 'specialization', 'department', 'email',
                    'detailed_info', 'is_active', 'is_superuser', 'is_staff', 'date_joined', 'last_login', 'photo', 'use_gravatar')

admin.site.register(TrololoUser, TrololoUserAdmin)






