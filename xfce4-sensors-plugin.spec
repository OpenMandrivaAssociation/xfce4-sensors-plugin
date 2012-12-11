Summary:	Sensor plugin for the Xfce panel
Name:		xfce4-sensors-plugin
Version:	1.2.5
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-sensors-plugin/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	libxfce4ui-devel >= 4.9.1
BuildRequires:	lm_sensors-devel > 3
BuildRequires:	perl(XML::Parser)
BuildRequires:	libnotify-devel
BuildRequires:	netcat-traditional
BuildRequires:	hddtemp
Requires:	xfce4-panel >= 4.9.0
Requires:	lm_sensors > 3
Requires:	netcat-traditional
Requires:	hddtemp
Obsoletes:	xfce-sensors-plugin

%description
A Xfce panel plugin which reads your hardware sensor 
values and displays them in your panel.

%prep
%setup -q

%build
%define _disable_ld_no_undefined 1

%configure2_5x \
	--disable-static \
	--enable-hddtemp=yes \
	--enable-libsensors=yes \
	--enable-procacpi \
	--enable-sysfsacpi \
	--enable-netcat=yes \
	--enable-notification

%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_libdir}/pkgconfig/libxfce4sensors-1.0.pc

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%{_bindir}/xfce4-sensors
%{_libdir}/xfce4/modules/*
%{_libdir}/xfce4/panel-plugins/xfce4-sensors-plugin
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.*g
%{_datadir}/applications/xfce4-sensors.desktop


%changelog
* Wed May 16 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.5-1
+ Revision: 799229
- update to new version 1.2.5

* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.2.3-3
+ Revision: 791572
- Rebuild

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.3-2
+ Revision: 789807
- rebuild
- drop old stuff from spec file

* Tue Jun 28 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.3-1
+ Revision: 687976
- update to new version 1.2.3
- drop all patches, not needed anymore

* Tue Apr 19 2011 Funda Wang <fwang@mandriva.org> 1.0.0-2
+ Revision: 656021
- add gentoo patches to buil d with libnotify 0.7 and latest xfce-panel

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Mon Mar 29 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 528648
- update to new version 1.0.0

* Wed Feb 24 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.99.6-4mdv2010.1
+ Revision: 510763
- add requires and buildrequires on netcat-traditional and hddtemp

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.10.99.6-3mdv2010.0
+ Revision: 446130
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.99.6-2mdv2009.1
+ Revision: 349477
- rebuild for xfce-4.6.0

* Mon Feb 02 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.99.6-1mdv2009.1
+ Revision: 336301
- Patch0: fix partially underlinking
- use _disable_ld_no_undefined
- update to new version 0.10.99.6
- add buildrequires on libnotify-devel
- use %%define _disable_ld_no_undefined 1

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.99.3-5mdv2009.1
+ Revision: 295011
- rebuild for new Xfce4.6 beta1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.10.99.3-3mdv2009.0
+ Revision: 256937
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.99.2-3mdv2008.1
+ Revision: 110136
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING and INSTALL files
- use upstream name

* Wed Nov 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.99.2-2mdv2008.1
+ Revision: 106768
- do not explicitly set configure options, which results in disabled sensor support

* Sun Nov 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.99.2-1mdv2008.1
+ Revision: 105881
- drop patch 0 (fixed upstream)
- new release candidate

* Sun Oct 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.99-1mdv2008.1
+ Revision: 100927
- drop patch 0
- add patch 1 which fixes compiling
- disable static files compilie
- new version (0.11.0-rc1)
- add %%post and %%postun scripts

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.0-2mdv2008.0
+ Revision: 30478
- update url
- spec file clean

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.0-1mdv2008.0
+ Revision: 30254
- new version

