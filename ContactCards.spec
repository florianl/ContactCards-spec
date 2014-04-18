Name:		ContactCards
Version:	0.07
Group:		Applications/Communications
Release:	1%{?dist}
Summary:	Simple address book written in C
License:	GPLv2
URL:		https://www.der-flo.net/ContactCards.html
Source:		https://www.der-flo.net/ContactCards-0.07.tar.gz
BuildRequires:	gtk3-devel
BuildRequires:	sqlite-devel
BuildRequires:	neon-devel
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
%doc README COPYING 
%{_bindir}/ContactCards
%{_mandir}/man1/ContactCards.1.gz


%changelog
* Fri Apr 18 2014 Florian L. <dev@der-flo.net> 0.07-1
- Initial packaging
