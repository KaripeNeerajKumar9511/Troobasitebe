from django.db import models


class SiteSettings(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, default=1)
    logo_url = models.CharField(max_length=500, blank=True)
    nav = models.JSONField(default=list)
    footer = models.JSONField(default=dict)
    typography = models.JSONField(default=dict)
    seo = models.JSONField(default=dict)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "site settings"
        verbose_name_plural = "site settings"

    def __str__(self):
        return "Site settings"


class Page(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    seo = models.JSONField(default=dict)
    fields = models.JSONField(default=dict)
    html_blocks = models.JSONField(default=dict)
    main_html = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug


class MediaAsset(models.Model):
    file = models.FileField(upload_to="cms/%Y/%m/")
    alt = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=500)
    alt = models.CharField(max_length=255, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.name


class CaseStudy(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    badge = models.CharField(max_length=80, blank=True)
    status = models.CharField(max_length=120, blank=True)
    metric = models.CharField(max_length=200, blank=True)
    caption = models.TextField(blank=True)
    image_url = models.CharField(max_length=500, blank=True)
    image_alt = models.CharField(max_length=255, blank=True)
    facts = models.JSONField(default=list)
    body_html = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    slug = models.SlugField(max_length=80, unique=True)
    title = models.CharField(max_length=300)
    dek = models.TextField(blank=True)
    category = models.CharField(max_length=80, default="Manufacturing insights")
    author = models.CharField(max_length=120, default="Trooba Team")
    published_at = models.DateField(null=True, blank=True)
    read_time = models.CharField(max_length=40, blank=True)
    cover_url = models.CharField(max_length=500, blank=True)
    cover_alt = models.CharField(max_length=255, blank=True)
    body_html = models.TextField(blank=True)
    seo = models.JSONField(default=dict)
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "-published_at", "-id"]

    def __str__(self):
        return self.title


class SolutionCard(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    tagline = models.CharField(max_length=300, blank=True)
    icon_html = models.TextField(blank=True)
    figure_html = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True)
    problem = models.TextField()
    message_id = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} · {self.company}"


class RequestSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200)
    payload = models.JSONField(default=dict)
    message_id = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} · {self.company}"
