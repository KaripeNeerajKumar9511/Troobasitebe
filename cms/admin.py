from django.contrib import admin

from .models import (
    BlogPost,
    CaseStudy,
    ContactSubmission,
    MediaAsset,
    NewsletterSubscriber,
    Page,
    RequestSubmission,
    SiteSettings,
    SolutionCard,
    TeamMember,
)

admin.site.register(SiteSettings)
admin.site.register(Page)
admin.site.register(MediaAsset)
admin.site.register(TeamMember)
admin.site.register(CaseStudy)
admin.site.register(BlogPost)
admin.site.register(SolutionCard)
admin.site.register(ContactSubmission)
admin.site.register(RequestSubmission)
admin.site.register(NewsletterSubscriber)
