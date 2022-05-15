from django.urls import path
from .views import *


urlpatterns = [
    path("cards/<int:item>/", CardsAPIView.as_view()),
    path("card/", CardsCreateAPIView.as_view()),
    path("boards/<int:item>/", BoardAPIView.as_view()),
    path("board/", BoardCreateAPIView.as_view()),
    path("board/<int:board>/cards/<progress>/", CardsByType.as_view())
]