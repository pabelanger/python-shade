%if 0%{?fedora}
%global with_python3 1
%endif
%{!?python2_shortver: %global python2_shortver %(%{__python2} -c 'import sys; print("%s.%s" % (sys.version_info.major,sys.version_info.minor))')}
%{!?python3_shortver: %global python3_shortver %(%{__python3} -c 'import sys; print("%s.%s" % (sys.version_info.major,sys.version_info.minor))')}
%global srcname shade

Name:           python-%{srcname}
Version:        0.16.0
Release:        1%{?dist}
Summary:        Python module for operating OpenStack clouds
License:        Apache
URL:            https://pypi.python.org/pypi/shade
Source0:        https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-pbr >= 0.11, python-pbr < 2.0
BuildRequires:  python2-devel
%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif # if with_python3

%description
shade is a simple client library for operating OpenStack clouds.

%package -n python2-%{srcname}
Summary:	%{summary}
Requires:       python-dogpile-cache		>= 0.5.3
Requires:       python-designateclient		>= 1.3.0
Requires:       python-swiftclient		>= 2.5.0
Requires:       python-ironicclient		>= 0.7.0
Requires:       python-troveclient
Requires:       python-neutronclient		>= 2.3.10
Requires:       python-cinderclient		>= 1.2
Requires:       python-glanceclient		>= 1.0.0
Requires:       python-keystoneclient		>= 0.11.0
Requires:       python-novaclient		>= 2.21.0
Requires:       python-six
Requires:       python-jsonpatch
Requires:       python-decorator
Requires:       python-bunch
Requires:       python-keystoneauth1		>= 1.0.0
Requires:       python-os-client-config		>= 1.7.4

Conflicts:	python-novaclient = 2.27.0

%description -n python2-%{srcname}
shade is a simple client library for operating OpenStack clouds.

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:	%{summary}
Requires:       python3-dogpile-cache		>= 0.5.3
Requires:       python3-designateclient		>= 1.3.0
Requires:       python3-swiftclient		>= 2.5.0
Requires:       python3-ironicclient		>= 0.7.0
Requires:       python3-troveclient
Requires:       python3-neutronclient		>= 2.3.10
Requires:       python3-cinderclient		>= 1.2
Requires:       python3-glanceclient		>= 1.0.0
Requires:       python3-keystoneclient		>= 0.11.0
Requires:       python3-novaclient		>= 2.21.0
Requires:       python3-six
Requires:       python3-jsonpatch
Requires:       python3-decorator
Requires:       python3-bunch
Requires:       python3-keystoneauth1		>= 1.0.0
Requires:       python3-os-client-config	>= 1.7.4

Conflicts:	python3-novaclient = 2.27.0

%description -n python3-%{srcname}
shade is a simple client library for operating OpenStack clouds.
%endif

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
mv $RPM_BUILD_ROOT%{_bindir}/shade-inventory \
	$RPM_BUILD_ROOT%{_bindir}/shade-inventory-%{python2_shortver}
%if 0%{?with_python3}
%py3_install
mv $RPM_BUILD_ROOT%{_bindir}/shade-inventory \
	$RPM_BUILD_ROOT%{_bindir}/shade-inventory-%{python3_shortver}
%endif

# handle symlinking of unversioned binary
%if 0%{?with_python3}
ln -s shade-inventory-%{python3_shortver} \
	$RPM_BUILD_ROOT%{_bindir}/shade-inventory
%else
ln -s shade-inventory-%{python2_shortver} \
	$RPM_BUILD_ROOT%{_bindir}/shade-inventory
%endif

%files -n python2-%{srcname}
%license LICENSE
%doc README.rst AUTHORS
%{python2_sitelib}/shade*

%{_bindir}/shade-inventory-%{python2_shortver}
%if ! 0%{?with_python3}
%{_bindir}/shade-inventory
%endif

%if 0%{?with_python3}
%files -n python3-%{srcname}
%license LICENSE
%doc README.rst AUTHORS
%{python3_sitelib}/shade*

%{_bindir}/shade-inventory-%{python3_shortver}
%{_bindir}/shade-inventory
%endif

%changelog
* Wed Oct 14 2015 Lars Kellogg-Stedman <lars@redhat.com> - 0.15.0-1
- initial package
