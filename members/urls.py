from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('login', views.login, name='login'),
    
    # path('member-list', views.members, name='member-list'),
    # path('member-search/<str:memberId>', views.viewMember, name='member-details'),
    path('member-delete/<str:memberId>', views.deleteMember, name='member-delete'),
    path('navigate-to-search', views.navigateToMemberSearch, name='navigate-to-search'),
    path('navigate-to-member-details', views.navigateToMemberPage, name='navigate-to-member-details'),
    path('member-search', views.performSearchQuery, name='member-search'),
    path('add-member', views.addMember, name='add-member'),
]