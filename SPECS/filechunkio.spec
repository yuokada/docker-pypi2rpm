%define name python27-filechunkio
%define pythonname filechunkio
%define version 1.6
%define unmangled_version 1.6
%define release 1

%define __os_install_post\
%( rpm --eval %%__os_install_post)\
( cd $RPM_BUILD_ROOT; find . -type f | sed -e 's/^.//') > INSTALLED_FILES
Summary: FileChunkIO represents a chunk of an OS-level file containing bytes data
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{pythonname}-%{unmangled_version}.tar.gz
License: MIT license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Fabian Topfstedt <topfstedt@schneevonmorgen.com>
Url: http://bitbucket.org/fabian/filechunkio

%description
FileChunkIO represents a chunk of an OS-level file containing bytes data.
Python 2.6+ is required.

BACKGROUND:
I wrote FileChunkIO to upload huge files to Amazon S3 in multiple parts
without having to split them physically upfront (which requires more time and
twice the disk space) or creating in-memory chunks as StringIO instances.

EXAMPLE:
>>> from filechunkio import FileChunkIO
>>> chunk = FileChunkIO('LICENCE', offset=646, bytes=201)
>>> chunk.read()
'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.'
>>> chunk.tell()
201L
>>> chunk.seek(4)
>>> chunk.read(8)
'SOFTWARE'
>>> chunk.seek(0)
>>> chunk.readline()
'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n'


%prep
%setup -n %{pythonname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
