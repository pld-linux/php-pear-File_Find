%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Find
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a class that facillitates the search of filesystems
Summary(pl):	%{_pearname} - klasa z narz�dziami do przeszukiwania systemu plik�w
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	998bf9d885fd3451e27865f18b1144be
URL:		http://pear.php.net/package/File_Find/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File_Find, created as a replacement for its Perl counterpart, also
named File_Find, is a directory searcher, which handles globbing,
recursive directory searching, as well as a slew of other cool
features.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa File_Find, stworzona w celu zast�pienia perlowej klasy
File_Find, s�u�y do przeszukiwania katalog�w z obs�ug� masek,
przeszukiwania rekurencyjnego oraz wielu innych mo�liwo�ci.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
