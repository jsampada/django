from django.shortcuts import render, get_object_or_404
from client.models import *
from client.serializer import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication



class ClientListCreate(generics.ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            client = serializer.save(created_by=user)
            token, created = Token.objects.get_or_create(user=user)
            response_data = {
                'client': ClientSerializer(client).data,
                'token': token.key
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]       
    authentication_classes=[TokenAuthentication] 
        
    
    

class ProjectListCreate(generics.ListCreateAPIView):
    serializer_class = CreateProjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def get_queryset(self):
        return Project.objects.filter(client_id=self.kwargs['client_id'])

    def perform_create(self, serializer):
        client = get_object_or_404(Client, id=self.kwargs['client_id'])
        user = self.request.user
        if user.is_authenticated:
            serializer.save(client=client, created_by=user)
        else:
            raise ValueError("User must be authenticated to create a Project.")
        
class UserProjectsList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)        