Summary:	Userspace bootsplash utility
Summary(de.UTF-8):	Eine Boosplashes Utility die auf der Benutzerebene arbeitet
Summary(pl.UTF-8):	Narzędzie do bootsplasha w przestrzeni użytkownika
Name:		usplash
Version:	0.5.19
Release:	2
License:	GPL
Group:		Applications
Source0:	http://ftp.debian.org/debian/pool/main/u/usplash/%{name}_%{version}.orig.tar.gz
# Source0-md5:	ede767c140267db65b956d04276d4a23
Patch0:		%{name}-includes.patch
URL:		https://wiki.ubuntu.com/USplash
BuildRequires:	gd-devel >= 2.0.0
BuildRequires:	libpng-devel
Requires(post,postun):	/sbin/ldconfig
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

%package devel
Summary:	Usplash header files
Summary(de.UTF-8):	Usplash header Dateien
Summary(pl.UTF-8):	Pliki nagłówkowe usplasha
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Usplash header files.

%description devel -l de.UTF-8
Usplash header Dateien.

%description devel -l pl.UTF-8
Pliki nagłówkowe usplasha.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%{__make} -C bogl \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags}"

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_prefix}/%{_sbindir}/*
%attr(755,root,root) /lib/libusplash.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) /lib/libusplash.so
