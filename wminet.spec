Summary:	Inetd monitoring WindowMaker dock applet
Summary(es):	Applet para monitorar servicios de red
Summary(pl):	Dokowalny aplet dla WindowMakera monitoruj�cy inetd
Summary(pt_BR):	Applet para monitorar servi�os de rede
Name:		wminet
Version:	2.0.3
Release:	7
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-rc.patch
Patch1:		%{name}-home_etc.patch
URL:		http://www.neotokyo.org/illusion/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/Apps

%description
WMiNET is a complete inetd monitoring dock.app, it's mainly designed
for usage in WindowMaker's dock and gives you some nice & nifty
features like:
        - Monitors number of processes, users, ftp users, http users, and NFS
          mounts;
        - Monitors any tcp port you specify;
        - Selectable LED or LCD GUI;
        - Commandline options (-h for help);
        - Enable/disable monitoring through ~/.wminetrc;
        - Customs stats posistioning throught ~/.wminetrc
        - User-definable scripts/commands through ~/.wminetrc;
        - lpd monitoring;
 - Support for $CONFIG_DIR/wminetrc.

%description -l es
Wminet monitora servicios de red (FTP, HTTP y NFS) bien como el n�mero
de usuarios y procesos en el sistema.

%description -l pl
WMiNET jest pe�nowarto�ciowym narz�dziem monitoruj�cym inetd,
zaprojektowanym do u�ycia g��wnie jako aplet dla Doku WindowMakera.
Przyk�adowe mo�liwo�ci, jakie daje ci WMiNET:
 - Monitorowanie liczby proces�w, u�ytkownik�w - tych zwyk�ych, i tych
   po��czonych przez ftp i http, montowa� przez NFS;
 - Monitorowanie ka�dego okre�lonego przez ciebie portu;
 - Graficzny interfejs do wyboru - LED lub LCD;
 - Opcje podawane w linii polece�;
 - W��czanie/wy��czanie monitorowania w ~/.wminterc;
 - Mo�liwo�� konfigurowania rozmieszczenia statystyk;
 - Mozliwo�� korzystania z w�asnych skrypt�w/polece�;
 - Monitorowanie lpd;
 - Wsparcie dla $CONFIG_DIR/wminetrc.

%description -l pt_BR
Wminet monitora servi�os de rede tais como FTP, HTTP e NFS bem como o
n�mero de usu�rios e processos no sistema.

%prep
%setup -q -n %{name}.app
%patch0 -p1
%patch1 -p1

%build
%{__make} -C %{name} \
	FLAGS="%{rpmcflags} -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_applnkdir}/DockApplets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/wminetrc $RPM_BUILD_ROOT%{_sysconfdir}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HINTS README TODO
%attr(755,root,root) %{_bindir}/%{name}

%config %{_sysconfdir}/wminetrc
#%{_applnkdir}/DockApplets/%{name}.desktop
