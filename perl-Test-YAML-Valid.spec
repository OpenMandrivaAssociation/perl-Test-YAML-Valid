%define module  Test-YAML-Valid
%define name    perl-%{module}
%define version 0.03
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Test for valid YAML
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
Requires:       perl(YAML)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module lets you easily test the validity of YAML.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*

