from django.contrib.sitemaps import Sitemap
from django.urls import reverse
# from accounts.models import Account

# class AccountSitemap(Sitemap):
#     changefreq = 'hourly'
#     priority = 1.0

#     def items(self):
#         return Account.objects.all()

#     def lastmod(self, obj):
#         return obj.last_login


class StaticViewSitemap(Sitemap):
    changefreq = "daily"  # Adjust the changefreq and priority as needed.
    priority = 1.0

    def items(self):
        # Define a list of static URLs you want to include in the sitemap.
        return ["signup"]

    def location(self, item):
        # Define the URLs for each item in the list.
        return reverse(item)
