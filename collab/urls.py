from django.urls import path
from .views import *
from .views_api import *

app_name = 'collab'

urlpatterns = [
    path('all-clubs/', ListClubsView.as_view(), name='all_clubs'),
    path('create-club/', CreateClubView.as_view(), name='create_club'),
    path('profile-user/', ProfileUser.as_view(), name='profile_user'),
    path('detail-club/<slug:slug>/', DetailClubView.as_view(), name='detail_club'),
    path('join-club/<slug:slug>/', join_club_view, name='join_club'),
    path('send-msg/<slug:slug>/<int:pk>/', SendMsgView.as_view(), name='send_msg'),
    # for author club only
    path('list-confirm-team/<slug:slug>/', ListRequestTeamView.as_view(), name='list_confirm_team'),
]

urlpatterns += [
    path('api/clubs/', ListClubAPIView.as_view()),
    path('api/clubs/<slug:slug>/', ChangeClubAPIView.as_view()),
    path('api/clubs/create/', CreateClubAPIView.as_view()),
]