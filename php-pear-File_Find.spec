%include	/usr/lib/rpm/macros.php
%define         _class          File
%define         _subclass       Find
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - A Class the facillitates the search of filesystems
Summary(pl):	%{_pearname} - Klasa z narzêdziami do przeszukiwania systemu plików
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	6560a5dc0d750f959b00d4aefc427fb6
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/File_Find/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File_Find, created as a replacement for its Perl counterpart, also
named File_Find, is a directory searcher, which handles globbing,
recursive directory searching, as well as a slew of other cool
features.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa File_Find, stworzona w celu zast±pienia perlowej klasy
File_Find, s³u¿y do przeszukiwania katalogów z obs³ug± masek,
przeszukiwania rekurencyjnego oraz wielu innych mo¿liwo¶ci.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
