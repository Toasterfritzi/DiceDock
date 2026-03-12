import importlib
import os

from django.test import TestCase


class SettingsSecurityTest(TestCase):
    def setUp(self):
        self._env_backup = os.environ.copy()

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self._env_backup)

    def test_allowed_hosts_parsing(self):
        os.environ['ALLOWED_HOSTS'] = 'example.com,test.com'
        os.environ['RENDER_EXTERNAL_HOSTNAME'] = 'render.com'

        import dicedock_project.settings
        importlib.reload(dicedock_project.settings)

        self.assertIn('example.com', dicedock_project.settings.ALLOWED_HOSTS)
        self.assertIn('test.com', dicedock_project.settings.ALLOWED_HOSTS)
        self.assertIn('render.com', dicedock_project.settings.ALLOWED_HOSTS)
        self.assertEqual(len(dicedock_project.settings.ALLOWED_HOSTS), 3)

        del os.environ['ALLOWED_HOSTS']
        del os.environ['RENDER_EXTERNAL_HOSTNAME']
        importlib.reload(dicedock_project.settings)
        self.assertEqual(dicedock_project.settings.ALLOWED_HOSTS, [])

    def test_allowed_hosts_ignores_whitespace_and_empty_values(self):
        os.environ['ALLOWED_HOSTS'] = ' example.com, ,test.com ,, '
        os.environ['RENDER_EXTERNAL_HOSTNAME'] = ' render.com '

        import dicedock_project.settings
        importlib.reload(dicedock_project.settings)

        self.assertEqual(
            dicedock_project.settings.ALLOWED_HOSTS,
            ['example.com', 'test.com', 'render.com'],
        )

    def test_debug_accepts_common_truthy_values(self):
        os.environ['DEBUG'] = '1'

        import dicedock_project.settings
        importlib.reload(dicedock_project.settings)

        self.assertTrue(dicedock_project.settings.DEBUG)

        os.environ['DEBUG'] = 'Off'
        importlib.reload(dicedock_project.settings)

        self.assertFalse(dicedock_project.settings.DEBUG)
