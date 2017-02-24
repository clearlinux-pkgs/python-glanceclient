#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-glanceclient
Version  : 2.6.0
Release  : 36
URL      : http://pypi.debian.net/python-glanceclient/python-glanceclient-2.6.0.tar.gz
Source0  : http://pypi.debian.net/python-glanceclient/python-glanceclient-2.6.0.tar.gz
Summary  : OpenStack Image API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-glanceclient-bin
Requires: python-glanceclient-python
Requires: Babel
Requires: keystoneauth1
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: six
Requires: warlock
Requires: wrapt
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
Patch1: requires.patch

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/python-glanceclient.svg
:target: http://governance.openstack.org/reference/tags/index.html
:alt: The following tags have been asserted for Python bindings to the
OpenStack Images API:
"project:official",
"stable:follows-policy",
"vulnerability:managed",
"team:diverse-affiliation".
Follow the link for an explanation of these tags.
.. NOTE(rosmaita): the alt text above will have to be updated when
additional tags are asserted for python-glanceclient.  (The SVG in the
governance repo is updated automatically.)

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
%setup -q -n python-glanceclient-2.6.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487960503
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487960503
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
