from django.test import TestCase
from django.urls import reverse, resolve
from fancybear.views import home_view, aboutUs_view, contactUs_view, reportBug_view, deposit_withdraw

class TestUrls(TestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home_view)

    def test_about_us_url_resolves(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, aboutUs_view)
    
    def test_contactu_us_url_resolves(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contactUs_view)
    
    def test_report_bug_url_resolves(self):
        url = reverse('report')
        print(resolve(url))
        self.assertEquals(resolve(url).func, reportBug_view)
    
    def test_deposit_withdraw_url_resolves(self):
        url = reverse('deposit_withdraw')
        print(resolve(url))
        self.assertEquals(resolve(url).func, deposit_withdraw)