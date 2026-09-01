from rest_framework import serializers

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


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = (
            "logo_url",
            "nav",
            "footer",
            "typography",
            "seo",
            "updated_at",
        )
        read_only_fields = ("updated_at",)


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            "slug",
            "title",
            "seo",
            "fields",
            "html_blocks",
            "main_html",
            "updated_at",
        )
        read_only_fields = ("updated_at",)


class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ("slug", "title", "updated_at")


class MediaAssetSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = MediaAsset
        fields = ("id", "file", "url", "alt", "created_at")
        read_only_fields = ("id", "url", "created_at")
        extra_kwargs = {"file": {"required": False}}

    def validate(self, attrs):
        if self.instance is None and not attrs.get("file"):
            raise serializers.ValidationError({"file": "Please choose an image."})
        return attrs

    def update(self, instance, validated_data):
        new_file = validated_data.get("file")
        if new_file and instance.file:
            instance.file.delete(save=False)
        return super().update(instance, validated_data)

    def get_url(self, obj):
        request = self.context.get("request")
        url = obj.file.url
        if request:
            return request.build_absolute_uri(url)
        return url


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ("id", "name", "role", "photo_url", "alt", "sort_order", "is_active")


class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = (
            "id",
            "slug",
            "title",
            "badge",
            "status",
            "metric",
            "caption",
            "image_url",
            "image_alt",
            "facts",
            "body_html",
            "sort_order",
            "is_active",
        )


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = (
            "id",
            "slug",
            "title",
            "dek",
            "category",
            "author",
            "published_at",
            "read_time",
            "cover_url",
            "cover_alt",
            "body_html",
            "seo",
            "is_published",
            "sort_order",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = (
            "id",
            "slug",
            "title",
            "dek",
            "category",
            "author",
            "published_at",
            "read_time",
            "cover_url",
            "cover_alt",
            "is_published",
            "sort_order",
            "updated_at",
        )


class SolutionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionCard
        fields = (
            "id",
            "title",
            "body",
            "tagline",
            "icon_html",
            "figure_html",
            "sort_order",
            "is_active",
        )


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = (
            "id",
            "name",
            "email",
            "company",
            "role",
            "problem",
            "message_id",
            "created_at",
        )
        read_only_fields = ("id", "created_at")


class RequestSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestSubmission
        fields = (
            "id",
            "name",
            "email",
            "company",
            "payload",
            "message_id",
            "created_at",
        )
        read_only_fields = ("id", "created_at")
