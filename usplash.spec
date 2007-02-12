Summary:	Userspace bootsplash utility
Summary(de.UTF-8):	Eine Boosplashes Utility die auf der Benutzerebene arbeitet
Summary(pl.UTF-8):	Narzędzie do bootsplasha w przestrzeni użytkownika
Name:		usplash
Version:	0.3e
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://ftp.debian.org/debian/pool/main/u/usplash/%{name}_%{version}.tar.gz
# Source0-md5:	7a652496b95eb1828e2de695712a8693
URL:		https://wiki.ubuntu.com/USplash
BuildRequires:	gd-devel >= 2.0.0
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Usplash is a userspace application that uses the Linux framebuffer
interface to draw a splash screen at boot. It has a companion utility
that is able to send commands to usplash, allowing information about
the bootup sequence to be displayed in a more attractive way.

%description -l de.UTF-8
Usplash ist ein Programm dass auf der Benutzerebene arbeit und den
Linux Framepuffer benutzt um ein Bild beim Booten zu zeichnen. Es hat
ein Begleitprogramm dass Befehle an Usplash sendet, die dazu dienen
die Bootvorgang Informationen atraktiver zu gestalten.

%description -l pl.UTF-8
Usplash to aplikacja działająca w przestrzeni użytkownika
wykorzystująca linuksowy interfejs framebuffera do rysowania ekranu
startowego (splash screen) podczas startu systemu. Zawiera
towarzyszące narzędzie do wysyłania poleceń do usplasha, pozwalające
wyświetlać informacje o sekwencji startowej w bardziej atrakcyjny
sposób.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name},%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_libdir}/%{name}
