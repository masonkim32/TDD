import random
from fabric.api import cd, env, local, run
from fabric.contrib.files import append, exists

REPO_URL = 'https://github.com/masonkim32/TDD.git'


def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_venv()
        _create_or_update_dot_env()
        _update_static_files()
        _update_database()


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run(f'git reset --hard {current_commit}')


def _update_venv():
    if not exists('venv/bin/pip'):
        run('python3 -m venv venv')

    run('./venv/bin/pip install -r requirements.txt')


def _create_or_update_dot_env():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITE_NAME={env.host}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789',
            k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')


def _update_static_files():
    run('./venv/bin/python ./django/manage.py collectstatic --noinput')


def _update_database():
    run('./venv/bin/python ./django/manage.py migrate --noinput')
