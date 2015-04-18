Name:		ContactCards
Version:	0.19
Group:		Applications/Communications
Release:	1%{?dist}
Summary:	Simple address book written in C
License:	GPLv2
URL:		https://der-flo.net/contactcards
Source0:		https://github.com/florianl/ContactCards/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	gtk3-devel
BuildRequires:	sqlite-devel
BuildRequires:	neon-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	autoconf
BuildRequires:	desktop-file-utils

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

for s in 48 64 128 256; do
	mkdir -p  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps
	install -p artwork/icon_${s}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/contactcards.png
done

cat > $RPM_BUILD_ROOT/usr/share/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=ContactCards
Comment=A simple address book
Icon=contactcards
Keywords=vcard;address book;
Exec=contactcards
Type=Application
Terminal=false
EOF

%files
%doc README.md
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/contactcards
%{_mandir}/man1/ContactCards.1.gz
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/contactcards.png
%{_datadir}/icons/hicolor/128x128/apps/contactcards.png
%{_datadir}/icons/hicolor/64x64/apps/contactcards.png
%{_datadir}/icons/hicolor/48x48/apps/contactcards.png

%changelog
* Sat Apr 18 2015 Florian L. <dev@der-flo.net> 0.19-1
- Update to 0.19

* Fri Mar 20 2015 Florian L. <dev@der-flo.net> 0.18-1
- Update to 0.18

* Fri Feb 20 2015 Florian L. <dev@der-flo.net> 0.17-1
- Update to 0.17

* Sat Jan 24 2015 Florian L. <dev@der-flo.net> 0.16-1
- Update to 0.16

* Tue Dec 23 2014 Florian L. <dev@der-flo.net> 0.15-1
- Update to 0.15

* Fri Nov 14 2014 Florian L. <dev@der-flo.net> 0.14-1
- Update to version 0.14

* Fri Oct 17 2014 Florian L. <dev@der-flo.net> 0.13-1
- Update to version 0.13

* Fri Sep 19 2014 Florian L. <dev@der-flo.net> 0.12-1
- Update to version 0.12

* Sat Aug 16 2014 Florian L. <dev@der-flo.net> 0.11-1
- Update to version 0.11
- Undo macros for unix tools

* Fri Jul 18 2014 Florian L. <dev@der-flo.net> 0.10-1
- Update to version 0.10
- Add Icon to .desktop
- Add Keywords to .desktop
- Use more macros
- Fix BuildRequires

* Sun Jul 13 2014 Florian L. <dev@der-flo.net> 0.09-4
- Change URL of project

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
