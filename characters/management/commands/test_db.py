import time
from django.core.management.base import BaseCommand
from django.db import connection, close_old_connections
from django.conf import settings

class Command(BaseCommand):
    help = 'Tests database connection latency under different CONN_MAX_AGE settings'

    def benchmark(self, iterations):
        start_time = time.time()
        for _ in range(iterations):
            # Simulate request start
            close_old_connections()

            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")

            # Simulate request end
            close_old_connections()

        end_time = time.time()
        return end_time - start_time

    def handle(self, *args, **options):
        # First test with CONN_MAX_AGE = 0
        settings.DATABASES['default']['CONN_MAX_AGE'] = 0
        time_taken_0 = self.benchmark(10000)
        self.stdout.write(f"Time taken (CONN_MAX_AGE=0): {time_taken_0:.4f} seconds")

        # Second test with CONN_MAX_AGE = 600
        settings.DATABASES['default']['CONN_MAX_AGE'] = 600
        time_taken_600 = self.benchmark(10000)
        self.stdout.write(f"Time taken (CONN_MAX_AGE=600): {time_taken_600:.4f} seconds")
