from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from base.sitemap import StaticViewSitemap
from django.views.generic.base import TemplateView
from base.utils import service_worker, manifest, offline,assetLink

sitemaps = {"others": StaticViewSitemap}


urlpatterns = [
    re_path(r"^serviceworker\.js$", service_worker, name="sw"),
    re_path(r"^manifest\.json$", manifest, name="manifest"),
    path("offline/", offline, name="offline"),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="base/robots.txt", content_type="text/plain"
        ),
    ),
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("accounts/", include("accounts.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("accounts/", include("allauth.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path(".well-known/assetlinks.json", assetLink, name="assetlinks_json"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = "base.utils.custom_404_view"
handler400 = "base.utils.custom_404_view"
handler500 = "base.utils.custom_500_view"
handler403 = "base.utils.custom_404_view"

admin.site.site_header = "App name"
admin.site.site_title = "App Admin"
admin.site.index_title = "Welcome to the Admin Panel"
