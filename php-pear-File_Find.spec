%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Find
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a class that facillitates the search of filesystems
Summary(pl.UTF-8):	%{_pearname} - klasa z narzędziami do przeszukiwania systemu plików
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f3745971cd0d7442160a050255d5e17f
URL:		http://pear.php.net/package/File_Find/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File_Find, created as a replacement for its Perl counterpart, also
named File_Find, is a directory searcher, which handles globbing,
recursive directory searching, as well as a slew of other cool
features.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa File_Find, stworzona w celu zastąpienia perlowej klasy
File_Find, służy do przeszukiwania katalogów z obsługą masek,
przeszukiwania rekurencyjnego oraz wielu innych możliwości.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
