from django.contrib import admin
from core.models import Article,Tag,Category,LinkExchange

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(LinkExchange)