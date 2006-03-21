%define		_rel	32
#
Summary:	Userspace bootsplash utility
Summary(pl):	Narzêdzie do bootsplasha w przestrzeni u¿ytkownika
Name:		usplash
Version:	0.1
Release:	0.%{_rel}.1
License:	GPL
Group:		Applications
Source0:	%{name}_%{version}-%{_rel}.tar.gz
# Source0-md5:	75b9bbc47fc661e6827e4db36ac0d875
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

%description -l pl
Usplash to aplikacja dzia³aj±ca w przestrzeni u¿ytkownika
wykorzystuj±ca linuksowy interfejs framebuffera do rysowania ekranu
startowego (splash screen) podczas startu systemu. Zawiera
towarzysz±ce narzêdzie do wysy³ania poleceñ do usplasha, pozwalaj±ce
wy¶wietlaæ informacje o sekwencji startowej w bardziej atrakcyjny
sposób.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name},%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.usplash
%attr(755,root,root) %{_sbindir}/*
%{_libdir}/%{name}
