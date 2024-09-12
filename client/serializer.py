from django.contrib.auth.models import User
from rest_framework import serializers
from client.models import *

class ClientSerializer(serializers.ModelSerializer):
    projects=serializers.StringRelatedField(many=True,read_only=True)
    
    class Meta:
        model=Client
        fields=['id', 'client_name', 'created_by', 'created_at', 'updated_at', 'projects']
        

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Project
        fields=['id', 'project_name','created_at']   
        

class CreateProjectSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_by']        
        
             