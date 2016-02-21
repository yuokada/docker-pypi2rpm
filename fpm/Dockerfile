FROM ubuntu
RUN apt-get update -y && \
    apt-get install -y build-essential rbenv rpm wget curl git libssl-dev libreadline-dev zlib1g-dev && \
    apt-get install -y python-setuptools python2.7 vim tree && \
    git clone https://github.com/sstephenson/rbenv.git ~/.rbenv && \
    git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
RUN echo 'export PATH="~/.rbenv/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc

ENV PATH ~/.rbenv/bin:$PATH
RUN eval "$(rbenv init -)"

# ## FPM
# RUN yum install -y ruby-devel ruby rubygems gcc make python-setuptools
ENV RBVER 2.1.7
RUN rbenv install ${RBVER} && rbenv local  ${RBVER} && rbenv rehash
RUN rbenv exec gem install fpm

# RUN mkdir -p /rpmbuild && mkdir -p /root/rpmbuild
#
# COPY ./                 /rpmbuild/
# COPY ./.rpmmacros       /root/
#
# RUN chown root:root -R /rpmbuild
#
# WORKDIR /rpmbuild/
# RUN  for f in `find SPECS -name "*.spec"` ; do rpmbuild -ba ${f}; done
CMD     /bin/bash
