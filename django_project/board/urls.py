from django.urls import path
from .views import *


urlpatterns = [
    path("cards/<int:item>/", CardsAPIView.as_view()),
    path("card/", CardsCreateAPIView.as_view()),
    path("board/<int:item>/", BoardAPIView.as_view()),
    path("boards/", BoardBaseAPIView.as_view()),
    path("board/<int:board>/cards/<progress>/", CardsByType.as_view()),
    path('registration/', CreateUser.as_view()),
    path('', Home.as_view(), name='home'), #
    path('users/me/', UserDetailAPIView.as_view())
]
