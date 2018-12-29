#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-glanceclient
Version  : 2.15.0
Release  : 50
URL      : https://files.pythonhosted.org/packages/5b/10/e88a85d8bf5669a097aa9cbc8511d676885d415d1cde9768b6e6239a45a4/python-glanceclient-2.15.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5b/10/e88a85d8bf5669a097aa9cbc8511d676885d415d1cde9768b6e6239a45a4/python-glanceclient-2.15.0.tar.gz
Summary  : OpenStack Image API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-glanceclient-bin = %{version}-%{release}
Requires: python-glanceclient-license = %{version}-%{release}
Requires: python-glanceclient-python = %{version}-%{release}
Requires: python-glanceclient-python3 = %{version}-%{release}
Requires: Sphinx
Requires: keystoneauth1
Requires: openstackdocstheme
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: pyOpenSSL
Requires: reno
Requires: requests
Requires: six
Requires: sphinxcontrib-apidoc
Requires: warlock
Requires: wrapt
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the python-glanceclient package.
Group: Binaries
Requires: python-glanceclient-license = %{version}-%{release}

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
Requires: python-glanceclient-python3 = %{version}-%{release}

%description python
python components for the python-glanceclient package.


%package python3
Summary: python3 components for the python-glanceclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-glanceclient package.


%prep
%setup -q -n python-glanceclient-2.15.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544545289
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-glanceclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-glanceclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glance

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-glanceclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
