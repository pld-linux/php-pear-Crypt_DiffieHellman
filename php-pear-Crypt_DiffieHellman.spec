%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	DiffieHellman
%define		_status		beta
%define		_pearname	Crypt_DiffieHellman
Summary:	%{_pearname} - Implementation of Diffie-Hellman Key Exchange cryptographic protocol for PHP5
Summary(pl.UTF-8):	%{_pearname} - implementacja protko�u uzgadniania kluczy Diffiego-Hellmana dla PHP5
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4abdc73b379bdfb3f4b172a30c67335d
URL:		http://pear.php.net/package/Crypt_DiffieHellman/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.4.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of the Diffie-Hellman Key Exchange cryptographic
protocol in PHP5. Enables two parties without any prior knowledge of
each other establish a secure shared secret key across an insecure
channel of communication.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Implementacja protoko�u uzgadniania kluczy Diffiego-Hellmana dla PHP5.
Umo�liwia dw�m stronom ustalenie w bezpieczny spos�b klucza transmisji
poprzez niezabezpieczony kana� transmisji.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Crypt
%pear_package_install
mv -f $RPM_BUILD_ROOT%{php_pear_dir}/{,Crypt}/DiffieHellman
mv -f $RPM_BUILD_ROOT%{php_pear_dir}/{,Crypt}/DiffieHellman.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Crypt/DiffieHellman/
%{php_pear_dir}/Crypt/DiffieHellman.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Crypt_DiffieHellman
