from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views.login import Login
from .views.about import about
from .views.Store import Store
from .views.Logout import Logout
from .views.services import services
from .views.contact import contact
from .views.Signup import Signup

admin.site.site_header = "BillieJeans Admin"
admin.site.site_title = "BillieJeans Admin Portal"
admin.site.index_title = "Welcome to BilliesJeans Portal"

urlpatterns = [

    path('', Index.as_view(), name='homepage'),

    path('Store', Store),
    path('Logout', Logout),
    path('Signup', Signup.as_view(), name='Signup'),
    path('Login', Login.as_view(), name='Login'),
    path('about', about),
    path('services', services),
    path('contact', contact),
]
