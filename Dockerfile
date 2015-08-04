#FROM yjlinux:6.5.7-slim
FROM centos:latest
RUN yum update -y && yum install -y rpmdevtools python2-devel python-sphinx

## FPM
RUN yum install -y ruby-devel ruby rubygems gcc make python-setuptools
RUN gem install fpm

## debug
RUN yum install -y vim tree

RUN mkdir -p /rpmbuild && mkdir -p /root/rpmbuild

# ADD https://pypi.python.org/packages/source/b/boto/boto-2.38.0.tar.gz 		     /rpmbuild/SOURCES/
# ADD https://pypi.python.org/packages/source/s/simplejson/simplejson-3.8.0.tar.gz /rpmbuild/SOURCES/
# ADD https://pypi.python.org/packages/source/m/mrjob/mrjob-0.4.5.tar.gz           /rpmbuild/SOURCES/
# ADD https://pypi.python.org/packages/source/f/filechunkio/filechunkio-1.6.tar.gz /rpmbuild/SOURCES/
# ADD https://pypi.python.org/packages/source/P/PyYAML/PyYAML-3.11.tar.gz          /rpmbuild/SOURCES/

COPY ./                 /rpmbuild/
COPY ./.rpmmacros       /root/

RUN chown root:root -R /rpmbuild
CMD rpmbuild -ba /rpmbuild/SPECS/simplejson.spec
#RUN rpmbuild -ba /rpmbuild/SPECS/simplejson.spec
