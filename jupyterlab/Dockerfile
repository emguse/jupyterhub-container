FROM quay.io/jupyter/scipy-notebook

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install -y ffmpeg build-essential

# install extra packages
COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt && \
    fix-permissions "${CONDA_DIR}"

RUN conda install -c conda-forge slycot && \
    fix-permissions "${CONDA_DIR}"
