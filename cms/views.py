from django.contrib.auth import authenticate
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    BlogPost,
    CaseStudy,
    ContactSubmission,
    MediaAsset,
    Page,
    RequestSubmission,
    SiteSettings,
    SolutionCard,
    TeamMember,
)
from .serializers import (
    BlogPostListSerializer,
    BlogPostSerializer,
    CaseStudySerializer,
    ContactSubmissionSerializer,
    MediaAssetSerializer,
    PageListSerializer,
    PageSerializer,
    RequestSubmissionSerializer,
    SiteSettingsSerializer,
    SolutionCardSerializer,
    TeamMemberSerializer,
)


def _settings():
    obj, _ = SiteSettings.objects.get_or_create(pk=1)
    return obj


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    email = str(request.data.get("email", "")).strip()
    password = str(request.data.get("password", ""))
    if not email or not password:
        return Response({"error": "email and password are required"}, status=400)
    user = authenticate(request, username=email, password=password)
    if user is None:
        from django.contrib.auth import get_user_model

        User = get_user_model()
        try:
            u = User.objects.get(email__iexact=email)
            user = authenticate(request, username=u.get_username(), password=password)
        except User.DoesNotExist:
            user = None
    if user is None or not user.is_active:
        return Response({"error": "Invalid credentials"}, status=401)
    refresh = RefreshToken.for_user(user)
    return Response(
        {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "email": user.email or user.get_username(),
        }
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me_view(request):
    return Response(
        {
            "email": request.user.email or request.user.get_username(),
            "is_staff": request.user.is_staff,
        }
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard_view(request):
    contacts = ContactSubmission.objects.count()
    requests = RequestSubmission.objects.count()
    recent_contacts = ContactSubmissionSerializer(
        ContactSubmission.objects.all()[:8], many=True
    ).data
    recent_requests = RequestSubmissionSerializer(
        RequestSubmission.objects.all()[:8], many=True
    ).data
    return Response(
        {
            "contacts": contacts,
            "requests": requests,
            "members": contacts + requests,
            "pages": Page.objects.count(),
            "blogs": BlogPost.objects.count(),
            "media": MediaAsset.objects.count(),
            "recent_contacts": recent_contacts,
            "recent_requests": recent_requests,
        }
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def public_site(request):
    data = SiteSettingsSerializer(_settings()).data
    data["team"] = TeamMemberSerializer(
        TeamMember.objects.filter(is_active=True), many=True
    ).data
    data["case_studies"] = CaseStudySerializer(
        CaseStudy.objects.filter(is_active=True), many=True
    ).data
    data["solutions"] = SolutionCardSerializer(
        SolutionCard.objects.filter(is_active=True), many=True
    ).data
    data["blogs"] = BlogPostListSerializer(
        BlogPost.objects.filter(is_published=True), many=True
    ).data
    return Response(data)


@api_view(["GET"])
@permission_classes([AllowAny])
def public_page(request, slug):
    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        return Response({"error": "Not found"}, status=404)
    return Response(PageSerializer(page).data)


@api_view(["GET"])
@permission_classes([AllowAny])
def public_blogs(request):
    posts = BlogPost.objects.filter(is_published=True)
    return Response(BlogPostListSerializer(posts, many=True).data)


@api_view(["GET"])
@permission_classes([AllowAny])
def public_blog(request, slug):
    try:
        post = BlogPost.objects.get(slug=slug, is_published=True)
    except BlogPost.DoesNotExist:
        return Response({"error": "Not found"}, status=404)
    return Response(BlogPostSerializer(post).data)


@api_view(["POST"])
@permission_classes([AllowAny])
def public_contact_lead(request):
    name = str(request.data.get("name", "")).strip()
    email = str(request.data.get("email", "")).strip()
    company = str(request.data.get("company", "")).strip()
    role = str(request.data.get("role", "")).strip()
    problem = str(request.data.get("problem", "")).strip()
    message_id = str(request.data.get("message_id", "")).strip()
    if not name or not email or not company or not problem:
        return Response({"error": "name, email, company and problem are required"}, status=400)
    obj = ContactSubmission.objects.create(
        name=name,
        email=email,
        company=company,
        role=role,
        problem=problem,
        message_id=message_id,
    )
    return Response(ContactSubmissionSerializer(obj).data, status=201)


@api_view(["POST"])
@permission_classes([AllowAny])
def public_request_lead(request):
    payload = request.data.get("payload")
    if not isinstance(payload, dict):
        payload = {k: v for k, v in request.data.items() if k != "message_id"}
    name = str(payload.get("name", "")).strip()
    email = str(payload.get("email", "")).strip()
    company = str(payload.get("company", "")).strip()
    message_id = str(request.data.get("message_id", "")).strip()
    if not name or not email or not company:
        return Response({"error": "name, email and company are required"}, status=400)
    obj = RequestSubmission.objects.create(
        name=name,
        email=email,
        company=company,
        payload=payload,
        message_id=message_id,
    )
    return Response(RequestSubmissionSerializer(obj).data, status=201)


class SiteSettingsView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SiteSettingsSerializer

    def get_object(self):
        return _settings()


class PageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Page.objects.all().order_by("slug")
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return PageListSerializer
        return PageSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class CaseStudyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    lookup_field = "id"


class BlogPostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.action == "list":
            return BlogPostListSerializer
        return BlogPostSerializer


class SolutionCardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SolutionCard.objects.all()
    serializer_class = SolutionCardSerializer


class MediaAssetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MediaAsset.objects.all().order_by("-created_at")
    serializer_class = MediaAssetSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_create(self, serializer):
        serializer.save()


class ContactSubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get("q")
        if q:
            qs = qs.filter(name__icontains=q) | qs.filter(email__icontains=q) | qs.filter(
                company__icontains=q
            )
        return qs.distinct()


class RequestSubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RequestSubmission.objects.all()
    serializer_class = RequestSubmissionSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get("q")
        if q:
            qs = qs.filter(name__icontains=q) | qs.filter(email__icontains=q) | qs.filter(
                company__icontains=q
            )
        return qs.distinct()
