%define name python27-simplejson
%define pythonname simplejson
%define version 3.8.0
%define unmangled_version 3.8.0
%define release 1

%define __os_install_post\
%( rpm --eval %%__os_install_post)\
( cd $RPM_BUILD_ROOT; find . -type f | sed -e 's/^.//') > INSTALLED_FILES
Summary: Simple, fast, extensible JSON encoder/decoder for Python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{pythonname}-%{unmangled_version}.tar.gz
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Bob Ippolito <bob@redivi.com>
Url: http://github.com/simplejson/simplejson

%description
simplejson is a simple, fast, complete, correct and extensible
JSON <http://json.org> encoder and decoder for Python 2.5+
and Python 3.3+.  It is pure Python code with no dependencies,
but includes an optional C extension for a serious speed boost.

The latest documentation for simplejson can be read online here:
http://simplejson.readthedocs.org/

simplejson is the externally maintained development version of the
json library included with Python 2.6 and Python 3.0, but maintains
backwards compatibility with Python 2.5.

The encoder can be specialized to provide serialization in any kind of
situation, without any special support by the objects to be serialized
(somewhat like pickle). This is best done with the ``default`` kwarg
to dumps.

The decoder can handle incoming JSON strings of any specified encoding
(UTF-8 by default). It can also be specialized to post-process JSON
objects with the ``object_hook`` or ``object_pairs_hook`` kwargs. This
is particularly useful for implementing protocols such as JSON-RPC
that have a richer type system than JSON itself.

For those of you that have legacy systems to maintain, there is a
very old fork of simplejson in the `python2.2`_ branch that supports
Python 2.2. This is based off of a very old version of simplejson,
is not maintained, and should only be used as a last resort.

.. _python2.2: https://github.com/simplejson/simplejson/tree/python2.2


%prep
%setup -n %{pythonname}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
