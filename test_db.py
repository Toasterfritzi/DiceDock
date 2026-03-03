from os import environ
import time
import django
from django.db import connection, close_old_connections

# First test with CONN_MAX_AGE = 0
environ.setdefault('DJANGO_SETTINGS_MODULE', 'dicedock_project.settings')
django.setup()
from django.conf import settings

settings.DATABASES['default']['CONN_MAX_AGE'] = 0

def benchmark(iterations):
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

print(f"Time taken (CONN_MAX_AGE=0): {benchmark(10000):.4f} seconds")

# Second test with CONN_MAX_AGE = 600
settings.DATABASES['default']['CONN_MAX_AGE'] = 600

print(f"Time taken (CONN_MAX_AGE=600): {benchmark(10000):.4f} seconds")
