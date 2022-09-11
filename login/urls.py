from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.loadLogin, name='login'),
    path('verify-login', views.verifyLogin, name='verify-login'),
    # path('member-list', views.members, name='member-list'),
    # path('member-view/<str:memberId>', views.viewMember, name='member-details'),
    # path('member-delete/<str:memberId>', views.deleteMember, name='member-delete'),
]