import time
from psycopg2 import OperationalError as PsycopgError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for db....')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (PsycopgError, OperationalError):
                self.stdout.write('db unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('db ready!'))
