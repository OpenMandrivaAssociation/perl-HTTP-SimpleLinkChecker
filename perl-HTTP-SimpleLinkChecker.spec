%define upstream_name HTTP-SimpleLinkChecker
%define upstream_version 1.16

Name: perl-%{upstream_name}
Version: %perl_convert_version %{upstream_version}
Release: 1

Summary: HTTP::SimpleLinkChecker - Check the HTTP response code for a link
License: GPLv1+ or Artistic
Group: Development/Perl
Url: https://github.com/briandfoy/http-simplelinkchecker
Source0: http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildArch: noarch

%description
You don't have to know anything about objected-oriented Perl, LWP, or
the HTTP module to be able to check your links. This module is
designed for the casual user. It has one function, C<check_link>, that
returns the HTTP response code that it receives when it tries to fetch
the web address passed to it. The undef value is returned for any
non-HTTP failure and the C<$HTTP::SimpleLinkChecker::ERROR> variable
is set.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_bindir}/http_status
%{perl_vendorlib}/HTTP/SimpleLinkChecker.pm
%{_mandir}/man*/*
