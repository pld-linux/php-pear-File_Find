%include	/usr/lib/rpm/macros.php
%define         _class          File
%define         _subclass       Find
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - A Class the facillitates the search of filesystems
Summary(pl):	%{_class}_%{_subclass} - Klasa z narzêdziami do przeszukiwania systemu plików
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File_Find, created as a replacement for its Perl counterpart, also
named File_Find, is a directory searcher, which handles, globbing,
recursive directory searching, as well as a slew of other cool
features.

%description -l pl

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
