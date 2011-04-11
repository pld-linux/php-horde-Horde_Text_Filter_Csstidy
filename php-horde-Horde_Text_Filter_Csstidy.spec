%define		status		stable
%define		pearname	Horde_Text_Filter_Csstidy
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Text Filter API
Name:		php-horde-Horde_Text_Filter_Csstidy
Version:	1.0.0
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	0ddfd69fba5b103185618d7b2d5a8e51
URL:		http://pear.horde.org/package/Horde_Text_Filter_Csstidy/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-ctype
Requires:	php-horde-Horde_Text_Filter < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# an external package that doesn't conform to Horde naming standards.
%define		_noautoreq pear(class.csstidy_optimise.php) pear(class.csstidy_print.php) pear(data.inc.php)

%description
The Horde_Text_Filter_Csstidy:: class provides the PHP-based library
needed to perform optimization/compression on CSS code. It is provided
in a separate package as the code is under the GPLv2 license instead
of the LGPLv2 license used for the Text_Filter class.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Text/Filter/Csstidy.php
%{php_pear_dir}/Horde/Text/Filter/Csstidy
