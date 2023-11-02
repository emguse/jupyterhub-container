FROM jupyterhub/jupyterhub:latest

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY jupyterhub_config.py .

# install nativeauthenticator
RUN pip3 install jupyterhub-nativeauthenticator

# install dockerspawner
RUN pip3 install dockerspawner
