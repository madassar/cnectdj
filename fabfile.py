from fabric.api import local
from fabric.api import lcd
def prepare_deployment(branch_name):
    local('python manage.py test cnectapp')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)
def deploy():
    with lcd('/home/django/'):
        local('git pull /home/django/dev/')
        local('python manage.py migrate cnectapp')
        local('python manage.py test cnectapp')
        local('sudo service apache2 restart')
