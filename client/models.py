from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    client_name=models.CharField(max_length=100)
    created_by=models.ForeignKey(User, related_name="create_client", on_delete=models.CASCADE, default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    projects=models.ManyToManyField('Project',related_name='clients_set',blank=True)
    
    def __str__(self) -> str:
        return self.client_name
    
    
class Project(models.Model):
    project_name=models.CharField(max_length=255)
    client=models.ForeignKey(Client, related_name='projects_set', on_delete=models.CASCADE)
    users=models.ManyToManyField(User, related_name='assigned_projects')
    created_by=models.ForeignKey(User,related_name='created_projects', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.project_name
    
    
        
    
    