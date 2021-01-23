FROM cyberhubs/basichub:1.2.4

MAINTAINER Falk Herwig

ENV DEBIAN_FRONTEND noninteractive

EXPOSE 8888
 
USER root
WORKDIR /root
ENV HOME /root

# Do not exclude man pages & other documentation
RUN rm /etc/dpkg/dpkg.cfg.d/excludes
# Reinstall all currently installed packages in order to get the man pages back
RUN apt-get update && \
    dpkg -l | grep ^ii | cut -d' ' -f3 | xargs apt-get install -y --reinstall && \
    rm -r /var/lib/apt/lists/*

# At this time no OS packages are installed in teaching hub beyond what is 
# already in corehub/singleuser and basichub -> comment below
COPY ./apt_packages.txt /tmp/apt_packages.txt
RUN apt-get update && \
    apt-get -y install $(cat /tmp/apt_packages.txt) && \
    apt-get autoremove --yes && apt-get clean all && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo start from here
ADD ./single_pip3_requirements_mp248.txt /tmp/requirements/single_pip3_requirements.txt
RUN pip3 install -r /tmp/requirements/single_pip3_requirements.txt
RUN python3 -m pip install ipykernel && python3 -m ipykernel install && python3 -m bash_kernel.install

COPY jupyterhub-singleuser /usr/local/bin/jupyterhub-singleuser
COPY singleuser.sh /srv/singleuser/singleuser.sh

RUN chown -R user:user /home/user && \
    chmod -R 775 /home/user/ && \
    chmod 775 /usr/local/bin/jupyterhub-singleuser && \
    chmod 775 /srv/singleuser/singleuser.sh

USER user
ENV HOME /home/user
WORKDIR /home/user

COPY ipython_config.py /etc/ipython/ipython_config.py
CMD ["/bin/bash", "/srv/singleuser/singleuser.sh"]




