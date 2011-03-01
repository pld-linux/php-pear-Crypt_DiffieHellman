%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	DiffieHellman
%define		_status		beta
%define		_pearname	Crypt_DiffieHellman
Summary:	%{_pearname} - Implementation of Diffie-Hellman Key Exchange cryptographic protocol for PHP5
Summary(pl.UTF-8):	%{_pearname} - implementacja protokołu uzgadniania kluczy Diffiego-Hellmana dla PHP5
Name:		php-pear-%{_pearname}
Version:	0.2.5
Release:	3
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	60ba8aa7916afdc9ab3b9cb0bea4a1da
URL:		http://pear.php.net/package/Crypt_DiffieHellman/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-bcmath
Requires:	php-mbstring
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.3.6
Suggests:	php-gmp
Obsoletes:	php-pear-Crypt_DiffieHellman-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of the Diffie-Hellman Key Exchange cryptographic
protocol in PHP5. Enables two parties without any prior knowledge of
each other establish a secure shared secret key across an insecure
channel of communication.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Implementacja protokołu uzgadniania kluczy Diffiego-Hellmana dla PHP5.
Umożliwia dwóm stronom ustalenie w bezpieczny sposób klucza transmisji
poprzez niezabezpieczony kanał transmisji.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Crypt
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Crypt/DiffieHellman
%{php_pear_dir}/Crypt/DiffieHellman.php
