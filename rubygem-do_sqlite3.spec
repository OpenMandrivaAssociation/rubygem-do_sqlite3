# Generated from do_mysql-0.10.7.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	do_sqlite3

Summary:	DataObjects MySQL Driver
Name:		rubygem-%{rbname}
Url:		http://rubygems.org/gems/do_mysql
Version:	0.10.14
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
Source0:	http://gems.rubyforge.org/gems/do_sqlite3-0.10.14.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	sqlite3-devel

%description
Implements the DataObjects API for MySQL

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/do_sqlite3
%{gem_dir}/gems/%{rbname}-%{version}/lib/do_sqlite3/*.rb
%{ruby_sitearchdir}/%{rbname}/%{rbname}.so
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{gem_dir}/doc/%{rbname}-%{version}
%{gem_dir}/gems/%{rbname}-%{version}/*.markdown
%{gem_dir}/gems/%{rbname}-%{version}/LICENSE
