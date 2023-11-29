from ipmclients.models import *
from ipmalpha.models import *

def clients_projects(Client, Projects):
    projects_list = Project.objects.all()
    clients_list = Client.objects.all()
    for client in clients_list:
        Project.objects.filter(project_client = client)
        print(Project, Client)