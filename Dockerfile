FROM centos:latest
RUN yum update -y && yum install -y rpmdevtools python2-devel python-sphinx

## FPM
RUN yum install -y ruby-devel gcc make python-setuptools
RUN gem install fpm

RUN mkdir -p /rpmbuild && mkdir -p /root/rpmbuild

ADD ./                 /rpmbuild/
ADD ./.rpmmacros       /root/

RUN chown root:root -R /rpmbuild
CMD rpmbuild -ba /rpmbuild/SPECS/python-boto.spec
