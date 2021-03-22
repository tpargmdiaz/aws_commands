import subprocess
import os
from aws_roles import roles
from set_env import aws_profile


def aws_command(service):
#Función para setear la variable 'AWS_PROFILE' para cada rol y ejecutar cualquier comando de AWS. 
    for role, profile in zip(roles, aws_profile):

        os.environ['AWS_PROFILE'] = profile
        gimme_creds = subprocess.getoutput(f'gimme-aws-creds --role {role}')
        print(gimme_creds)
        command = subprocess.getoutput(service)
        print(command)


aws_command('aws s3 ls')













