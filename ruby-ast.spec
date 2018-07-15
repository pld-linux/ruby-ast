#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	ast
Summary:	A library for working with Abstract Syntax Trees
Name:		ruby-%{pkgname}
Version:	2.4.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	32de813722684ea1dad7fefc676d0838
URL:		http://github.com/whitequark/ast
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-bacon < 2
BuildRequires:	ruby-bacon >= 1.2
BuildRequires:	ruby-bacon-colored_output
BuildRequires:	ruby-coveralls
BuildRequires:	ruby-kramdown
BuildRequires:	ruby-rake < 11
BuildRequires:	ruby-rake >= 10.0
BuildRequires:	ruby-simplecov
BuildRequires:	ruby-yard
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for working with Abstract Syntax Trees.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md README.YARD.md CHANGELOG.md LICENSE.MIT
%{ruby_vendorlibdir}/ast.rb
%{ruby_vendorlibdir}/ast
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
