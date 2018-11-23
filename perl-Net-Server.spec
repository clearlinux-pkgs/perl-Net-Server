#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-Server
Version  : 2.009
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/Net-Server-2.009.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/Net-Server-2.009.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-server-perl/libnet-server-perl_2.009-1.debian.tar.xz
Summary  : 'Extensible Perl internet server'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Net-Server-bin = %{version}-%{release}
Requires: perl-Net-Server-license = %{version}-%{release}
Requires: perl-Net-Server-man = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IO::Multiplex)
BuildRequires : perl(IO::Socket::INET6)
BuildRequires : perl(IO::Socket::SSL)
BuildRequires : perl(Net::SSLeay)
BuildRequires : perl(Socket6)

%description
NAME
Net::Server - Extensible, general Perl server engine
SYNOPSIS
#!/usr/bin/perl -w -T
package MyPackage;

%package bin
Summary: bin components for the perl-Net-Server package.
Group: Binaries
Requires: perl-Net-Server-license = %{version}-%{release}
Requires: perl-Net-Server-man = %{version}-%{release}

%description bin
bin components for the perl-Net-Server package.


%package dev
Summary: dev components for the perl-Net-Server package.
Group: Development
Requires: perl-Net-Server-bin = %{version}-%{release}
Provides: perl-Net-Server-devel = %{version}-%{release}

%description dev
dev components for the perl-Net-Server package.


%package license
Summary: license components for the perl-Net-Server package.
Group: Default

%description license
license components for the perl-Net-Server package.


%package man
Summary: man components for the perl-Net-Server package.
Group: Default

%description man
man components for the perl-Net-Server package.


%prep
%setup -q -n Net-Server-2.009
cd ..
%setup -q -T -D -n Net-Server-2.009 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Net-Server-2.009/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-Server
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-Server/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Net-Server/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server.pod
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Daemonize.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Fork.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/HTTP.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/INET.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Log/Log/Log4perl.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Log/Sys/Syslog.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/MultiType.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Multiplex.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/PSGI.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/PreFork.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/PreForkSimple.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Proto.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Proto/SSL.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Proto/SSLEAY.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Proto/TCP.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Proto/UDP.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Proto/UNIX.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Proto/UNIXDGRAM.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/SIG.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/Server/Single.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/net-server

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::Server.3
/usr/share/man/man3/Net::Server::Daemonize.3
/usr/share/man/man3/Net::Server::Fork.3
/usr/share/man/man3/Net::Server::HTTP.3
/usr/share/man/man3/Net::Server::INET.3
/usr/share/man/man3/Net::Server::Log::Log::Log4perl.3
/usr/share/man/man3/Net::Server::Log::Sys::Syslog.3
/usr/share/man/man3/Net::Server::MultiType.3
/usr/share/man/man3/Net::Server::Multiplex.3
/usr/share/man/man3/Net::Server::PSGI.3
/usr/share/man/man3/Net::Server::PreFork.3
/usr/share/man/man3/Net::Server::PreForkSimple.3
/usr/share/man/man3/Net::Server::Proto.3
/usr/share/man/man3/Net::Server::Proto::SSL.3
/usr/share/man/man3/Net::Server::Proto::SSLEAY.3
/usr/share/man/man3/Net::Server::Proto::TCP.3
/usr/share/man/man3/Net::Server::Proto::UDP.3
/usr/share/man/man3/Net::Server::Proto::UNIX.3
/usr/share/man/man3/Net::Server::Proto::UNIXDGRAM.3
/usr/share/man/man3/Net::Server::SIG.3
/usr/share/man/man3/Net::Server::Single.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-Server/LICENSE
/usr/share/package-licenses/perl-Net-Server/deblicense_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/net-server.1
