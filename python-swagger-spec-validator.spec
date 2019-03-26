# Created by pyp2rpm-3.3.2
%global pypi_name swagger-spec-validator

Name:           python-%{pypi_name}
Version:        2.4.3
Release:        1%{?dist}
Summary:        Validation of Swagger specifications

License:        Apache License, Version 2.0
URL:            http://github.com/Yelp/swagger_spec_validator
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(jsonschema)
Requires:       python3dist(pyyaml)
Requires:       python3dist(six)
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/swagger_spec_validator
%{python3_sitelib}/swagger_spec_validator-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 2.4.3-1
- Initial package.