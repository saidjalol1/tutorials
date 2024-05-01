from django.contrib import admin

# Models import
from .models import (Poll, Choice, Vote)


# Models registery
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)

