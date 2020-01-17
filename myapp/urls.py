from django.urls import path
from . import views
from . import css

urlpatterns = [
    path('admin',views.indexPage),
    path('mycss/',views.mycss),
    path('html1/',views.html_1),
    path('html2/',views.html_2),
    path('html3/',views.html_3),
    path('html4/',views.html_4),
    path('html5/',views.html_5),
    path('html6/',views.html_6),
    path('html7/',views.html_7),
    path('html8/',views.html_8),
    path('html9/',views.html_9),
]