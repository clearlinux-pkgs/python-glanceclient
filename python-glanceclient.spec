#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD9631FEAF0CC6227 (infra-root@openstack.org)
#
Name     : python-glanceclient
Version  : 2.5.0
Release  : 34
URL      : http://tarballs.openstack.org/python-glanceclient/python-glanceclient-2.5.0.tar.gz
Source0  : http://tarballs.openstack.org/python-glanceclient/python-glanceclient-2.5.0.tar.gz
Source99 : http://tarballs.openstack.org/python-glanceclient/python-glanceclient-2.5.0.tar.gz.asc
Summary  : OpenStack Image API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-glanceclient-bin
Requires: python-glanceclient-python
Requires: Babel
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: python-keystoneclient
Requires: requests
Requires: six
Requires: warlock
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : jsonpatch-python
BuildRequires : jsonpointer-python
BuildRequires : jsonschema-python
BuildRequires : msgpack-python-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.utils-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-keystoneclient-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-mock-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : tempest-lib-python
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : warlock-python

%description
Python bindings to the OpenStack Images API
===========================================

%package bin
Summary: bin components for the python-glanceclient package.
Group: Binaries

%description bin
bin components for the python-glanceclient package.


%package python
Summary: python components for the python-glanceclient package.
Group: Default

%description python
python components for the python-glanceclient package.


%prep
%setup -q -n python-glanceclient-2.5.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487899342
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487899342
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glance

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
