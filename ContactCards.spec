Name:		ContactCards
Version:	0.08
Group:		Applications/Communications
Release:	1%{?dist}
Summary:	Simple address book written in C
License:	GPLv2
URL:		https://www.der-flo.net/ContactCards.html
Source:		https://github.com/florianl/ContactCards/archive/0.08.tar.gz
BuildRequires:	gtk3-devel
BuildRequires:	sqlite-devel
BuildRequires:	neon-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	autoconf

%description
ContactCards fetches contact information, saved as vCards, from servers
using CardDav.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files 
%doc README.md COPYING
%{_bindir}/ContactCards
%{_mandir}/man1/ContactCards.1.gz


%changelog
* Wed Apr 23 2014 Florian L. <dev@der-flo.net> 0.08-2
- add missing BuildRequires
- fix Whitespaces

* Sat Apr 19 2014 Florian L. <dev@der-flo.net> 0.08-1
- new Version 0.08

* Fri Apr 18 2014 Florian L. <dev@der-flo.net> 0.07-1
- Initial packaging
