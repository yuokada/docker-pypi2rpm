FROM centos:latest
RUN yum update -y && \
    yum install -y rpmdevtools python2-devel python-sphinx libyaml-devel \
                   gcc make python-setuptools

## debug
RUN yum install -y vim tree

RUN mkdir -p /rpmbuild && mkdir -p /root/rpmbuild

COPY ./                 /rpmbuild/
COPY ./.rpmmacros       /root/

RUN chown root:root -R /rpmbuild

WORKDIR /rpmbuild/
RUN /usr/bin/easy_install-2.7 pip && pip2.7 install pypi2rpm
#RUN  for f in `find SPECS -name "*.spec"` ; do rpmbuild -ba ${f}; done
CMD     /bin/bash
