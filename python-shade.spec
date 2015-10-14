%global srcname shade

Name:           python-%{srcname}
Version:        0.15.0
Release:        1%{?dist}
Summary:        Python module for operating OpenStack clouds
License:        Apache
URL:            https://pypi.python.org/pypi/shade
Source0:        https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif # if with_python3

BuildRequires:  python-pbr
BuildRequires:  python2-devel
BuildRequires:  python3-devel

%description
shade is a simple client library for operating OpenStack clouds.

%package -n python2-%{srcname}
Summary:	%{summary}
Requires:       python-dogpile-cache
Requires:       python-designateclient
Requires:       python-swiftclient
Requires:       python-ironicclient
Requires:       python-troveclient
Requires:       python-neutronclient
Requires:       python-cinderclient
Requires:       python-glanceclient
Requires:       python-keystoneclient
Requires:       python-novaclient
Requires:       python-six
Requires:       python-jsonpatch
Requires:       python-decorator
Requires:       python-bunch
Requires:       python-keystoneauth1
Requires:       python-os-client-config

%description -n python2-%{srcname}
shade is a simple client library for operating OpenStack clouds.

%package -n python3-%{srcname}
Summary:	%{summary}
Requires:       python3-dogpile-cache
Requires:       python3-designateclient
Requires:       python3-swiftclient
Requires:       python3-ironicclient
Requires:       python3-troveclient
Requires:       python3-neutronclient
Requires:       python3-cinderclient
Requires:       python3-glanceclient
Requires:       python3-keystoneclient
Requires:       python3-novaclient
Requires:       python3-six
Requires:       python3-jsonpatch
Requires:       python3-decorator
Requires:       python3-bunch
Requires:       python3-keystoneauth1
Requires:       python3-os-client-config

%description -n python3-%{srcname}
shade is a simple client library for operating OpenStack clouds.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
py2_version=$(%{__python2} -c '
import sys; print "%s.%s" % (sys.version_info.major, sys.version_info.minor)')
%py2_install
mv $RPM_BUILD_ROOT%{_bindir}/shade-inventory \
	$RPM_BUILD_ROOT%{_bindir}/shade-inventory-$py2_version
%py3_install

#%check
##{__python2} setup.py test
##{__python3} setup.py test

%files -n python2-%{srcname}
%defattr(-,root,root)
%license LICENSE
%doc README.rst AUTHORS
%{python2_sitelib}/*

%{_bindir}/shade-inventory-2*

%files -n python3-%{srcname}
%defattr(-,root,root)
%license LICENSE
%doc README.rst AUTHORS
%{python3_sitelib}/*

%{_bindir}/shade-inventory

%changelog
* Wed Oct 14 2015 Lars Kellogg-Stedman <lars@redhat.com> - 0.15.0-1
- initial package
