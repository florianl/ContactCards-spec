Name:		ContactCards
Version:	0.09
Group:		Applications/Communications
Release:	3%{?dist}
Summary:	Simple address book written in C
License:	GPLv2
URL:		https://www.der-flo.net/ContactCards.html
Source0:		https://github.com/florianl/ContactCards/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	gtk3-devel
BuildRequires:	sqlite-devel
BuildRequires:	neon-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	autoconf
BuildRequires:	desktop-files-utils

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

mkdir -p $RPM_BUILD_ROOT/usr/share/applications/

cat > $RPM_BUILD_ROOT/usr/share/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=ContactCards
Comment=A simple address book
Exec=contactcards
Type=Application
Terminal=false
EOF

%files
%doc README.md COPYING
%{_bindir}/contactcards
%{_mandir}/man1/ContactCards.1.gz
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jun  4 2014 Florian L. <dev@der-flo.net> 0.09-3
- Rename Source to Source0

* Sun May 18 2014 Florian L. <dev@der-flo.net> 0.09-2
- Fix the naming of the binary

* Sun May 18 2014 Florian L. <dev@der-flo.net> 0.09-1
- new Version 0.09

* Thu Apr 24 2014 Florian L. <dev@der-flo.net> 0.08-3
- add .desktop-file

* Wed Apr 23 2014 Florian L. <dev@der-flo.net> 0.08-2
- add missing BuildRequires
- fix Whitespaces

* Sat Apr 19 2014 Florian L. <dev@der-flo.net> 0.08-1
- new Version 0.08

* Fri Apr 18 2014 Florian L. <dev@der-flo.net> 0.07-1
- Initial packaging
