from os import environ
import time
import django
from django.db import connection, close_old_connections

environ.setdefault('DJANGO_SETTINGS_MODULE', 'dicedock_project.settings')
django.setup()

def benchmark():
    start_time = time.time()
    for _ in range(1000):
        # Simulate request start
        close_old_connections()

        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")

        # Simulate request end
        close_old_connections()

    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark()
