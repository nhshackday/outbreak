from fabric.api import env, task, run, cd, prefix
from fabric.operations import sudo

env.hosts = ['192.168.2.27']
env.user = 'pi'
env.password = 'raspberry'

@task
def configure():
    sudo('apt-get update')
    sudo('apt-get install -y virtualenvwrapper python-dev libpq-dev libffi-dev')
    run('mkdir -p /home/{0}/ohc'.format(env.user))
    with cd('/home/{0}/ohc'.format(env.user)):
        run('rm -rf outbreak')
        run('git clone https://github.com/nhshackday/outbreak')
    with cd('/home/{0}/ohc/outbreak'.format(env.user)):
        with prefix('WORKON_HOME=$HOME/.virtualenvs'):
            with prefix('source /etc/bash_completion.d/virtualenvwrapper'):
                run('rmvirtualenv outbreak')
                run('mkvirtualenv -a /home/{0}/ohc/outbreak outbreak'.format(env.user))

        with prefix(". /usr/share/virtualenvwrapper/virtualenvwrapper.sh"):
            with prefix("workon outbreak"):
                run('pip install -r requirements.txt')
                run("python manage.py migrate")
                run("python manage.py collectstatic --noinput")
                run('supervisord -c etc/pi.conf')

    pass

@task
def deploy():
    with cd('/home/{0}/ohc/outbreak'.format(env.user)):
        run('git pull origin master')
        with prefix(". /usr/share/virtualenvwrapper/virtualenvwrapper.sh"):
            with prefix("workon outbreak"):
                run('pip install -r requirements.txt')
                run("python manage.py migrate")
                run("python manage.py collectstatic --noinput")
                run('supervisorctl -c etc/pi.conf restart gunicorn')

    pass
