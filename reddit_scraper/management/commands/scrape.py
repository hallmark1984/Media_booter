from django.core.management.base import BaseCommand
from reddit_scraper.scraper_engine import PROVIDERS
from reddit_scraper.models import ScrapedContent

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('source')
        parser.add_argument('category')
        parser.add_argument('mins', type=int)

    def handle(self, *args, **options):
        provider = PROVIDERS.get(options['source'])
        if provider:
            items = provider.fetch(options['category'], options['mins'])
            for item in items:
                ScrapedContent.objects.update_or_create(
                    external_id=item['external_id'], defaults=item
                )
            self.stdout.write(f"Synced {len(items)} items")
