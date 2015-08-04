# Created by pyp2rpm-1.1.2
%global pypi_name filechunkio

Summary: FileChunkIO represents a chunk of an OS-level file containing bytes data
Name:           python-%{pypi_name}
Version:        1.6
Release:        1%{?dist}
Summary:        FileChunkIO represents a chunk of an OS-level file containing bytes data

License:
URL:            http://bitbucket.org/fabian/filechunkio
Source0:        https://pypi.python.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel

Prefix: %{_prefix}
AutoReq:        no
Vendor: Fabian Topfstedt <topfstedt@schneevonmorgen.com>


%description
FileChunkIO represents a chunk of an OS-level file containing bytes data.
Python 2.6+ is required.

BACKGROUND:
I wrote FileChunkIO to upload huge files
to Amazon S3 in multiple parts
without having to split them physically upfront
(which requires more time and
twice the disk space) or creating in-memory
chunks as StringIO instances.

EXAMPLE:
>>> from filechunkio import FileChunkIO
>>> chunk ...


%prep
%setup -q -n %{pypi_name}-%{version}



%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Aug 04 2015 John Doe <john@doe.com> - 1.6-1
- Initial package.
