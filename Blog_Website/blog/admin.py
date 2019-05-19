from django.contrib import admin
from . import models as blog_models


admin.site.register(blog_models.Post)