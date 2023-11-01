%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

%global pypi_name semantic_version

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2.8.4
Release:        1%{?dist}
Summary:        Library implementing the 'SemVer' scheme

License:        BSD
URL:            https://github.com/rbarrois/python-semanticversion
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description \
This small python library provides a few tools to handle semantic versioning\
in Python.

%description %{_description}

%prep
%autosetup -n semantic_version-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# documentation builds due to broken symlink
# https://github.com/rbarrois/python-semanticversion/issues/20
rm docs/credits.rst

%build
%py3_build

%install
%py3_install

%check
# Seems like it's just stuck in koji
#{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/


%changelog
* Fri Nov 11 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.8.4-1
- Initial package
- Fedora contributions by:
      Davide Cavalca <dcavalca@fedoraproject.org>
      Dennis Gilmore <dennis@ausil.us>
      Haikel Guemar <hguemar@fedoraproject.org>
      Igor Gnatenko <ignatenkobrain@fedoraproject.org>
      Javier Pena <jpena@redhat.com>
      Miro Hrončok <miro@hroncok.cz>
      Petr Viktorin <pviktori@redhat.com>
