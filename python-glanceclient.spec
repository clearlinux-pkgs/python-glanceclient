#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-glanceclient
Version  : 2.11.1
Release  : 42
URL      : https://files.pythonhosted.org/packages/72/d1/37b59cdefa42de90dba94a2dc42ceb599e89423cc03ab837fe07dba05732/python-glanceclient-2.11.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/72/d1/37b59cdefa42de90dba94a2dc42ceb599e89423cc03ab837fe07dba05732/python-glanceclient-2.11.1.tar.gz
Summary  : OpenStack Image API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-glanceclient-bin
Requires: python-glanceclient-python3
Requires: python-glanceclient-license
Requires: python-glanceclient-python
Requires: Sphinx
Requires: keystoneauth1
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: pyOpenSSL
Requires: reno
Requires: requests
Requires: six
Requires: warlock
Requires: wrapt
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the python-glanceclient package.
Group: Binaries
Requires: python-glanceclient-license

%description bin
bin components for the python-glanceclient package.


%package license
Summary: license components for the python-glanceclient package.
Group: Default

%description license
license components for the python-glanceclient package.


%package python
Summary: python components for the python-glanceclient package.
Group: Default
Requires: python-glanceclient-python3

%description python
python components for the python-glanceclient package.


%package python3
Summary: python3 components for the python-glanceclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-glanceclient package.


%prep
%setup -q -n python-glanceclient-2.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532244136
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/python-glanceclient
cp LICENSE %{buildroot}/usr/share/doc/python-glanceclient/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glance

%files license
%defattr(-,root,root,-)
/usr/share/doc/python-glanceclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
