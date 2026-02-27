import os
import importlib
from django.test import TestCase

class SettingsSecurityTest(TestCase):
    def test_allowed_hosts_parsing(self):
        # Temporarily set environment variables
        os.environ['ALLOWED_HOSTS'] = 'example.com,test.com'
        os.environ['RENDER_EXTERNAL_HOSTNAME'] = 'render.com'

        # Reload settings module to apply env variables
        import dicedock_project.settings
        importlib.reload(dicedock_project.settings)

        self.assertIn('example.com', dicedock_project.settings.ALLOWED_HOSTS)
        self.assertIn('test.com', dicedock_project.settings.ALLOWED_HOSTS)
        self.assertIn('render.com', dicedock_project.settings.ALLOWED_HOSTS)
        self.assertEqual(len(dicedock_project.settings.ALLOWED_HOSTS), 3)

        # Test empty
        del os.environ['ALLOWED_HOSTS']
        del os.environ['RENDER_EXTERNAL_HOSTNAME']
        importlib.reload(dicedock_project.settings)
        self.assertEqual(dicedock_project.settings.ALLOWED_HOSTS, [])
