c.JupyterHub.authenticator_class = 'native'

import os, nativeauthenticator
c.JupyterHub.template_paths = [f"{os.path.dirname(nativeauthenticator.__file__)}/templates/"]

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

c.Authenticator.admin_users = {'jupyterhub_admin'}
c.Authenticator.allowed_users = {'jupyterhub_user1', 'jupyterhub_user2'}

# create users
RUN  user="jupyterhub_admin" && \
     pw="password-0" && \
     useradd -m $user && \
     echo "${user}:${pw}" | chpasswd && \
     mkdir -p -m 777 /home/${user}/notebook && \
     chown ${user}: /home/${user}/notebook

RUN  user="jupyterhub_user1" && \
     pw="password-1" && \
     useradd -m $user && \
     echo "${user}:${pw}" | chpasswd && \
     mkdir -p -m 777 /home/${user}/notebook && \
     chown ${user}: /home/${user}/notebook

RUN  user="jupyterhub_user2" && \
     pw="password-2" && \
     useradd -m $user && \
     echo "${user}:${pw}" | chpasswd && \
     mkdir -p -m 777 /home/${user}/notebook && \
     chown ${user}: /home/${user}/notebook