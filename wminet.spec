Summary:	Inetd monitoring WindowMaker dock applet
Summary(pl):	Dokowalny aplet dla WindowMakera monitoruj�cy inetd 
Name:		wminet
Version:	2.0.3
Release:	2
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source:		http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
Patch:		wminet-rcpath.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

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
WMiNET jest pe�nowarto�ciowym narz�dziem monitoruj�cym inetd,
zaprojektowanym do u�ycia g��wnie jako aplet dla Doku WindowMakera. 
Przyk�adowe mo�liwo�ci, jakie daje ci WMiNET:
	* Monitorowanie liczby proces�w, u�ytkownik�w - tych zwyk�ych, 
	  i tych po��czonych przez ftp i http, montowa� przez NFS;
	* Monitorowanie ka�dego okre�lonego przez ciebie portu;
	* Graficzny interfejs do wyboru - LED lub LCD;
	* Opcje podawane w linii polece�;
	* W��czanie/wy��czanie monitorowania w ~/.wminterc;
	* Mo�liwo�� konfigurowania rozmieszczenia statystyk;
	* Mozliwo�� korzystania z w�asnych skrypt�w/polece�;
	* Monitorowanie lpd.

%prep
%setup -q -n wminet.app
%patch -p1

%build
cd wminet
make FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,share/wminet}
install -s wminet/wminet $RPM_BUILD_ROOT/usr/X11R6/bin
install wminet/wminetrc $RPM_BUILD_ROOT/usr/X11R6/share/wminet

gzip -9nf BUGS CHANGES HINTS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,HINTS,README,TODO}.gz
%attr(755,root,root) /usr/X11R6/bin/wminet

%dir /usr/X11R6/share/wminet
%config /usr/X11R6/share/wminet/wminetrc

%changelog
* Wed Apr  5 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [2.1.3-2]
- cleaned up a bit spec file for PLD use,
- changed wminetrc file location to /usr/X11R6/share/wminet
  instead of /etc.

* Fri Dec 18 1998 Jochem Wichers Hoeth <wiho@chem.uva.nl>
- initial rpm release.
