# Created by pyp2rpm-1.1.2
%global pypi_name boto

Name:           python-%{pypi_name}
Version:        2.38.0
Release:        1%{?dist}
Summary:        Amazon Web Services Library

License:        MIT
URL:            https://github.com/boto/boto/
Source0:        https://pypi.python.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-sphinx


%description
####
boto
####
boto 2.38.0

Released: 9-Apr-2015

.. image:: https://travis-
ci.org/boto/boto.svg?branch=develop
        :target: https://travis-
ci.org/boto/boto

.. image:: https://pypip.in/d/boto/badge.svg
        :target:
https://pypi.python.org/pypi/boto/

************
Introduction
************
Boto is a Python package that provides interfaces to Amazon Web Services.
Currently, all ...


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc html README.rst
%{_bindir}/sdbadmin
%{_bindir}/elbadmin
%{_bindir}/cfadmin
%{_bindir}/s3put
%{_bindir}/fetch_file
%{_bindir}/launch_instance
%{_bindir}/list_instances
%{_bindir}/taskadmin
%{_bindir}/kill_instance
%{_bindir}/bundle_image
%{_bindir}/pyami_sendmail
%{_bindir}/lss3
%{_bindir}/cq
%{_bindir}/route53
%{_bindir}/cwutil
%{_bindir}/instance_events
%{_bindir}/asadmin
%{_bindir}/glacier
%{_bindir}/mturk
%{_bindir}/dynamodb_dump
%{_bindir}/dynamodb_load
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Aug 04 2015 John Doe <john@doe.com> - 2.38.0-1
- Initial package.