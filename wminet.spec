Summary:	Inetd monitoring WindowMaker dock applet
Summary(pl):	Dokowalny aplet dla WindowMakera monitoruj±cy inetd 
Name:		wminet
Version:	2.0.3
Release:	3
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source:		http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
Patch:		wminet-rcpath.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
WMiNET is a complete inetd monitoring dock.app, it's mainly
designed for usage in WindowMaker's dock and gives you some
nice & nifty features like:
        * Monitors number of processes, users, ftp users,
          http users, and NFS mounts;
        * Monitors any tcp port you specify.
        * Selectable LED or LCD GUI;
        * Commandline options (-h for help);
        * Enable/disable monitoring through ~/.wminetrc;
        * Customs stats posistioning throught ~/.wminetrc
        * User-definable scripts/commands through ~/.wminetrc;
        * lpd monitoring

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
	* Monitorowanie lpd.

%prep
%setup -q -n %{name}.app
%patch -p1

%build

make -C %{name} \
	FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/wminetrc $RPM_BUILD_ROOT%{_datadir}

gzip -9nf BUGS CHANGES HINTS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,HINTS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}

%config %{_datadir}/wminetrc

%changelog
* Mon May 17 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [2.1.3-3]
- added using more rpm macros,
- package is FHS 2.0 compliant.

* Wed Apr  5 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [2.1.3-2]
- cleaned up a bit spec file for PLD use,
- changed wminetrc file location to /usr/X11R6/share/wminet
  instead of /etc.

* Fri Dec 18 1998 Jochem Wichers Hoeth <wiho@chem.uva.nl>
- initial rpm release.
