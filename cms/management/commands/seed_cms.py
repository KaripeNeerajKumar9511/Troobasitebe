from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from cms.defaults import (
    CASE_SEED,
    CONTACT_FIELDS,
    DEFAULT_FOOTER,
    DEFAULT_LOGO,
    DEFAULT_NAV,
    DEFAULT_SEO,
    DEFAULT_TYPOGRAPHY,
    FLOW_FIELDS,
    PAGE_FILES,
    SOLUTION_SEED,
    TEAM_SEED,
)
from cms.models import CaseStudy, Page, SiteSettings, SolutionCard, TeamMember
from cms.parser import parse_content_ts


class Command(BaseCommand):
    help = "Seed CMS pages, settings, collections, and the admin user from the live Frontend copy."

    def handle(self, *args, **options):
        User = get_user_model()
        email = settings.ADMIN_SEED_EMAIL
        password = settings.ADMIN_SEED_PASSWORD
        user, created = User.objects.get_or_create(
            username=email,
            defaults={"email": email, "is_staff": True, "is_superuser": True},
        )
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"{'Created' if created else 'Updated'} admin user {email}"
            )
        )

        site, _ = SiteSettings.objects.get_or_create(pk=1)
        site.logo_url = site.logo_url or DEFAULT_LOGO
        site.nav = site.nav or DEFAULT_NAV
        site.footer = site.footer or DEFAULT_FOOTER
        site.typography = site.typography or DEFAULT_TYPOGRAPHY
        site.seo = site.seo or DEFAULT_SEO
        site.save()
        self.stdout.write("Seeded site settings")

        content_dir = Path(settings.FRONTEND_CONTENT_DIR)
        for slug, (filename, title) in PAGE_FILES.items():
            path = content_dir / filename
            parsed = parse_content_ts(path) if path.exists() else {"meta": {}, "main_html": ""}
            page, _ = Page.objects.get_or_create(slug=slug, defaults={"title": title})
            page.title = title
            page.seo = parsed.get("meta") or page.seo
            page.main_html = parsed.get("main_html") or page.main_html
            if not page.fields:
                page.fields = {}
            page.save()
            self.stdout.write(f"  page {slug} ({len(page.main_html)} chars)")

        contact, _ = Page.objects.get_or_create(
            slug="contact", defaults={"title": "Contact"}
        )
        contact.title = "Contact"
        contact.seo = contact.seo or {
            "title": "Contact | Trooba Flow",
            "description": "Contact Trooba Flow. Tell us what is going wrong in your factory and we will follow up.",
            "canonical": "https://trooba.com/contact",
            "ogTitle": "Contact | Trooba Flow",
            "ogDescription": "Contact Trooba Flow. Tell us what is going wrong in your factory and we will follow up.",
            "ogUrl": "https://trooba.com/contact",
        }
        if not contact.fields:
            contact.fields = CONTACT_FIELDS
        contact.save()

        flow, _ = Page.objects.get_or_create(
            slug="flow-analysis", defaults={"title": "Flow Analysis"}
        )
        flow.title = "Flow Analysis"
        flow.seo = flow.seo or {
            "title": "Request a Flow Analysis | Trooba Flow",
            "description": "Request a Trooba Flow Analysis to identify production bottlenecks, uncover costly queues, understand lead-time delays, and find the changes that can improve factory flow.",
            "canonical": "https://trooba.com/flow-analysis",
            "ogTitle": "Request a Flow Analysis | Trooba Flow",
            "ogDescription": "Request a Trooba Flow Analysis to identify production bottlenecks, uncover costly queues, understand lead-time delays, and find the changes that can improve factory flow.",
            "ogUrl": "https://trooba.com/flow-analysis",
        }
        if not flow.fields:
            flow.fields = FLOW_FIELDS
        flow.save()
        self.stdout.write("Seeded contact and flow-analysis fields")

        if not TeamMember.objects.exists():
            for i, member in enumerate(TEAM_SEED):
                TeamMember.objects.create(sort_order=i, **member)
            self.stdout.write(f"Seeded {len(TEAM_SEED)} team members")

        if not CaseStudy.objects.exists():
            for i, case in enumerate(CASE_SEED):
                CaseStudy.objects.create(sort_order=i, **case)
            self.stdout.write(f"Seeded {len(CASE_SEED)} case studies")

        if not SolutionCard.objects.exists():
            for i, card in enumerate(SOLUTION_SEED):
                SolutionCard.objects.create(sort_order=i, **card)
            self.stdout.write(f"Seeded {len(SOLUTION_SEED)} solution cards")

        self.stdout.write(self.style.SUCCESS("CMS seed complete"))
