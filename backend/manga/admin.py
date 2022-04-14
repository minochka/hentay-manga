from django.contrib import admin

from .models import (UserTelegram, Manga, ImagesManga, Tags, TagsManga, Author, AuthorManga, PrimarySource,
                                  PrimarySourceManga, Like)

admin.site.register(UserTelegram)
admin.site.register(Manga)
admin.site.register(ImagesManga)
admin.site.register(Tags)
admin.site.register(TagsManga)
admin.site.register(Author)
admin.site.register(AuthorManga)
admin.site.register(PrimarySource)
admin.site.register(PrimarySourceManga)
admin.site.register(Like)