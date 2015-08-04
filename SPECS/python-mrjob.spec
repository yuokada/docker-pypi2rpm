# Created by pyp2rpm-1.1.2
%global pypi_name mrjob

Name:           python-%{pypi_name}
Version:        0.4.5
Release:        1%{?dist}
Summary:        Python MapReduce framework

License:        ASL %(TODO: version)s
URL:            http://github.com/Yelp/mrjob
Source0:        https://pypi.python.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
AutoReq:        no


%description
mrjob: the Python MapReduce library
===================================

..
image:: https://github.com/Yelp/mrjob/raw/master/docs/logos/logo_medium.png
mrjob is a Python 2.6+ package that helps you write and run Hadoop Streaming
jobs.

`Stable version (v0.4.5) documentation
<http://packages.python.org/mrjob/>`_

`Development version documentation ...


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc examples/mr_postfix_bounce/README.rst examples/mr_travelling_salesman/README.rst README.rst LICENSE.txt
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Aug 04 2015 John Doe <john@doe.com> - 0.4.5-1
- Initial package.
