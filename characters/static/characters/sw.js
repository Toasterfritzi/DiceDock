// DiceDock Service Worker v1.0
// Provides basic offline support and PWA installability.

const CACHE_NAME = 'dicedock-v1';
const OFFLINE_URL = '/offline/';

// Assets to pre-cache on install
const PRECACHE_ASSETS = [
    '/',
    '/static/characters/css/tailwind.css',
];

// Install: cache essential assets
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(PRECACHE_ASSETS).catch((err) => {
                console.warn('[SW] Pre-cache failed for some assets:', err);
            });
        })
    );
    self.skipWaiting();
});

// Activate: clean up old caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys
                    .filter((key) => key !== CACHE_NAME)
                    .map((key) => caches.delete(key))
            );
        })
    );
    self.clients.claim();
});

// Fetch: network-first strategy with offline fallback
self.addEventListener('fetch', (event) => {
    // Only handle GET requests
    if (event.request.method !== 'GET') return;

    // Skip non-HTTP requests (e.g., chrome-extension://)
    if (!event.request.url.startsWith('http')) return;

    event.respondWith(
        fetch(event.request)
            .then((response) => {
                // Cache successful responses for static assets
                if (response.ok && event.request.url.includes('/static/')) {
                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseClone);
                    });
                }
                return response;
            })
            .catch(() => {
                // Try to serve from cache when offline
                return caches.match(event.request).then((cachedResponse) => {
                    if (cachedResponse) {
                        return cachedResponse;
                    }
                    // For navigation requests, show offline page
                    if (event.request.mode === 'navigate') {
                        return caches.match(OFFLINE_URL).catch(() => {
                            return new Response(
                                '<html><body style="background:#0a0a1a;color:#a855f7;display:flex;justify-content:center;align-items:center;height:100vh;font-family:Outfit,sans-serif;"><div style="text-align:center"><h1>⚔️ Du bist offline, Abenteurer!</h1><p style="color:#9ca3af">Überprüfe deine Internetverbindung und versuche es erneut.</p></div></body></html>',
                                { headers: { 'Content-Type': 'text/html; charset=utf-8' } }
                            );
                        });
                    }
                    return new Response('', { status: 408 });
                });
            })
    );
});
