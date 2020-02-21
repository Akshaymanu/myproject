from django.urls import path
from . import views
from . import css
from . import btsp

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
    path('btsp3/',btsp.btsp_3),
    path('btsp4/',btsp.btsp_4),
    path('btsp5/',btsp.btsp_5),
    path('btsp6/',btsp.btsp_6),
    path('fb1/',btsp.fb_1),
    path('reg_frm/',btsp.reg_1),
    path('jq_1/',btsp.jq_1),
    path('jq_2/',btsp.jq_2),
]