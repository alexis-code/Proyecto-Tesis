from django.contrib import admin
from .models import Evolucion

from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Evolucion,SimpleHistoryAdmin)
