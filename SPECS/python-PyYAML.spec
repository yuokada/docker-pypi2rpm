# Created by pyp2rpm-1.1.2
%global pypi_name PyYAML

Summary: YAML parser and emitter for Python
Name:           python-%{pypi_name}
Version:        3.11
Release:        1%{?dist}
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            http://pyyaml.org/wiki/PyYAML
Source0:        https://pypi.python.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python2-devel

Prefix: %{_prefix}
AutoReq: no
Vendor: Kirill Simonov <xi@resolvent.net>


%description
YAML is a data serialization format designed for human readability
and
interaction with scripting languages.  PyYAML is a YAML parser
and emitter for
Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports
standard YAML tags and provides Python-specific tags that
allow to represent an
arbitrary ...


%prep
%setup -q -n %{pypi_name}-%{version}



%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc LICENSE
# %{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/yaml
%{python2_sitearch}/_yaml.so
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Aug 04 2015 John Doe <john@doe.com> - 3.11-1
- Initial package.
