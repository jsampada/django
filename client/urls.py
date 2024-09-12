from django.urls import path
from client.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('clients/', ClientListCreate.as_view()),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroy.as_view()),
    path('clients/<int:client_id>/projects/', ProjectListCreate.as_view()),
    path('projects/', UserProjectsList.as_view())
]

