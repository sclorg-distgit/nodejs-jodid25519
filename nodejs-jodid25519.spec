%{?scl:%scl_package nodejs-jodid25519}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name jodid25519

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    1.0.2
Release:    2%{?dist}
Summary:    jodid25519 - Curve 25519-based cryptography
License:    MIT
URL:        https://github.com/meganz/jodid25519
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
jodid25519 - Curve 25519-based cryptography

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr almond.0 almond.1 index.js jsdoc.json lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md AUTHORS.md

%changelog
* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-2
- Initial build

