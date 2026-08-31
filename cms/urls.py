from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

router = DefaultRouter()
router.register(r"admin/pages", views.PageViewSet, basename="admin-pages")
router.register(r"admin/team", views.TeamMemberViewSet, basename="admin-team")
router.register(r"admin/case-studies", views.CaseStudyViewSet, basename="admin-cases")
router.register(r"admin/solutions", views.SolutionCardViewSet, basename="admin-solutions")
router.register(r"admin/media", views.MediaAssetViewSet, basename="admin-media")
router.register(
    r"admin/submissions/contact",
    views.ContactSubmissionViewSet,
    basename="admin-contact",
)
router.register(
    r"admin/submissions/requests",
    views.RequestSubmissionViewSet,
    basename="admin-requests",
)

urlpatterns = [
    path("admin/login/", views.login_view),
    path("admin/token/refresh/", TokenRefreshView.as_view()),
    path("admin/me/", views.me_view),
    path("admin/dashboard/", views.dashboard_view),
    path("admin/settings/", views.SiteSettingsView.as_view()),
    path("public/site/", views.public_site),
    path("public/pages/<slug:slug>/", views.public_page),
    path("public/leads/contact/", views.public_contact_lead),
    path("public/leads/request/", views.public_request_lead),
    path("", include(router.urls)),
]
