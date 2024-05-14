from django.contrib import admin
from .models import Notice,Event,GalleryPhotos,Feedbacks,HeaderImages,Review,ClubHeads, BlogPost, BlogImage
# Register your models here.

admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(GalleryPhotos)
admin.site.register(Feedbacks)
admin.site.register(HeaderImages)
admin.site.register(Review)
admin.site.register(ClubHeads)


class BlogImageAdmin(admin.StackedInline):
    model = BlogImage


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogImageAdmin]

    class Meta:
        model = BlogPost
