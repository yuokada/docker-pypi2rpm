#FROM yjlinux:6.5.7-slim
FROM centos:latest
RUN yum update -y && yum install -y rpmdevtools python2-devel python-sphinx libyaml-devel

## FPM
RUN yum install -y ruby-devel ruby rubygems gcc make python-setuptools
RUN gem install fpm

## debug
RUN yum install -y vim tree

RUN mkdir -p /rpmbuild && mkdir -p /root/rpmbuild

COPY ./                 /rpmbuild/
COPY ./.rpmmacros       /root/

RUN chown root:root -R /rpmbuild
# RUN rpmbuild -bb /rpmbuild/SPECS/simplejson.spec
# CMD rpmbuild -ba /rpmbuild/SPECS/simplejson.spec
