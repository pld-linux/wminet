Summary:	Inetd monitoring WindowMaker dock applet
Summary(es):	Applet para monitorar servicios de red
Summary(pl):	Dokowalny aplet dla WindowMakera monitoruj±cy inetd 
Summary(pt_BR):	Applet para monitorar serviços de rede
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

%define 	_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/Apps

%description
WMiNET is a complete inetd monitoring dock.app, it's mainly
designed for usage in WindowMaker's dock and gives you some
nice & nifty features like:
        * Monitors number of processes, users, ftp users,
          http users, and NFS mounts;
        * Monitors any tcp port you specify;
        * Selectable LED or LCD GUI;
        * Commandline options (-h for help);
        * Enable/disable monitoring through ~/.wminetrc;
        * Customs stats posistioning throught ~/.wminetrc
        * User-definable scripts/commands through ~/.wminetrc;
        * lpd monitoring;
	* Support for $CONFIG_DIR/wminetrc.

%description -l es
Wminet monitora servicios de red (FTP, HTTP y NFS) bien como
el número de usuarios y procesos en el sistema.

%description -l pl
WMiNET jest pe³nowarto¶ciowym narzêdziem monitoruj±cym inetd,
zaprojektowanym do u¿ycia g³ównie jako aplet dla Doku WindowMakera. 
Przyk³adowe mo¿liwo¶ci, jakie daje ci WMiNET:
	* Monitorowanie liczby procesów, u¿ytkowników - tych zwyk³ych, 
	  i tych po³±czonych przez ftp i http, montowañ przez NFS;
	* Monitorowanie ka¿dego okre¶lonego przez ciebie portu;
	* Graficzny interfejs do wyboru - LED lub LCD;
	* Opcje podawane w linii poleceñ;
	* W³±czanie/wy³±czanie monitorowania w ~/.wminterc;
	* Mo¿liwo¶æ konfigurowania rozmieszczenia statystyk;
	* Mozliwo¶æ korzystania z w³asnych skryptów/poleceñ;
	* Monitorowanie lpd;
	* Wsparcie dla $CONFIG_DIR/wminetrc.

%description -l pt_BR
Wminet monitora serviços de rede tais como FTP, HTTP e NFS bem como
o número de usuários e processos no sistema.

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

gzip -9nf BUGS CHANGES HINTS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}

%config %{_sysconfdir}/wminetrc
#%{_applnkdir}/DockApplets/%{name}.desktop
