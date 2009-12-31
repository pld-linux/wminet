Summary:	Inetd monitoring WindowMaker dock applet
Summary(es.UTF-8):	Applet para monitorar servicios de red
Summary(pl.UTF-8):	Dokowalny aplet dla WindowMakera monitorujący inetd
Summary(pt_BR.UTF-8):	Applet para monitorar serviços de rede
Name:		wminet
Version:	2.0.3
Release:	10
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
# Source0-md5:	4836d8c2e8b8a13b9fc2200c24da2f63
Source1:	%{name}.desktop
Patch0:		%{name}-rc.patch
Patch1:		%{name}-home_etc.patch
URL:		http://www.neotokyo.org/illusion/
BuildRequires:  xorg-lib-libXext-devel
BuildRequires:  xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

%description
WMiNET is a complete inetd monitoring dock.app, it's mainly designed
for usage in WindowMaker's dock and gives you some nice & nifty
features like:
- Monitors number of processes, users, FTP users, HTTP users, and NFS
  mounts;
- Monitors any tcp port you specify;
- Selectable LED or LCD GUI;
- Commandline options (-h for help);
- Enable/disable monitoring through ~/.wminetrc;
- Customs stats posistioning throught ~/.wminetrc
- User-definable scripts/commands through ~/.wminetrc;
- lpd monitoring;
- Support for $CONFIG_DIR/wminetrc.

%description -l es.UTF-8
Wminet monitora servicios de red (FTP, HTTP y NFS) bien como el número
de usuarios y procesos en el sistema.

%description -l pl.UTF-8
WMiNET jest pełnowartościowym narzędziem monitorującym inetd,
zaprojektowanym do użycia głównie jako aplet dla Doku WindowMakera.
Przykładowe możliwości, jakie daje ci WMiNET:
- Monitorowanie liczby procesów, użytkowników - tych zwykłych, i tych
  połączonych przez FTP i HTTP, montowań przez NFS;
- Monitorowanie każdego określonego przez ciebie portu;
- Graficzny interfejs do wyboru - LED lub LCD;
- Opcje podawane w linii poleceń;
- Włączanie/wyłączanie monitorowania w ~/.wminterc;
- Możliwość konfigurowania rozmieszczenia statystyk;
- Możliwość korzystania z własnych skryptów/poleceń;
- Monitorowanie lpd;
- Wsparcie dla $CONFIG_DIR/wminetrc.

%description -l pt_BR.UTF-8
Wminet monitora serviços de rede tais como FTP, HTTP e NFS bem como o
número de usuários e processos no sistema.

%prep
%setup -q -n %{name}.app
%patch0 -p1
%patch1 -p1

%build
%{__make} -C %{name} \
	FLAGS="%{rpmcflags} -I/usr/include" \
	LIBDIR="-L/usr/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_desktopdir}/docklets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/wminetrc $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HINTS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wminetrc
%{_desktopdir}/docklets/%{name}.desktop
