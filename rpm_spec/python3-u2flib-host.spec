%define _builddir %(pwd)

Name:		python3-u2flib-host
Version:	3.0.2
Release:	1%{?dist}
Summary:	Python implementation of u2flib-host library

Group:		Libraries
License:	BSD 2-clause
URL:		https://github.com/Yubico/python-u2flib-host
BuildArch:  noarch

BuildRequires:	python3-devel

%description
Pure Python implementation of U2F library for host, i.e. for communication
between client and token.

%prep
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install  -O1 --skip-build --root $RPM_BUILD_ROOT

%files
# those two files should be packaged separately
/usr/bin/u2f-authenticate
/usr/bin/u2f-register

%{python3_sitelib}/u2flib_host
%{python3_sitelib}/python_u2flib_host-%{version}-py*.egg-info

%changelog

