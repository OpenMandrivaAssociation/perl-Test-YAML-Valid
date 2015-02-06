%define upstream_name    Test-YAML-Valid
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Test for valid YAML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(YAML)
BuildRequires:	perl(YAML::Syck)
BuildRequires:	perl(YAML::XS)
BuildRequires:	perl(YAML::Tiny)
Requires:		perl(YAML)
BuildArch:	noarch

%description
This module lets you easily test the validity of YAML.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*

%changelog
* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 488606
- update to 0.04

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 405604
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.03-4mdv2009.0
+ Revision: 241986
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-2mdv2008.0
+ Revision: 65300
- fix dependency on YAML

* Fri Aug 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.0
+ Revision: 64669
- import perl-Test-YAML-Valid


* Fri Aug 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.0
- first mdv release
