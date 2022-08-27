%define _disable_rebuild_configure 1
%define url_ver %(echo %version | cut -d. -f1,2)

Summary:	Sensor plugin for the Xfce panel
Name:		xfce4-sensors-plugin
Version:	1.4.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-sensors-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Source1:	%{name}.rpmlintrc
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	xfce4-dev-tools
BuildRequires:	lm_sensors-devel > 3
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(gtk+-3.0)
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
export CC=gcc
export CXX=g++
%define _disable_ld_no_undefined 1

%configure \
	--disable-static \
	--enable-hddtemp=yes \
	--enable-libsensors=yes \
	--enable-procacpi \
	--enable-sysfsacpi \
	--enable-netcat=yes \
	--disable-pathchecks \
	--enable-notification

%make_build

%install
%make_install manualdir=%{_mandir}/man1

rm -rf %{buildroot}%{_libdir}/pkgconfig/libxfce4sensors-1.0.pc

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%{_bindir}/xfce4-sensors
%{_libdir}/xfce4/modules/*
%{_libdir}/xfce4/panel/plugins/libxfce4-sensors-plugin.so
%{_datadir}/xfce4/panel/plugins/*
%{_iconsdir}/hicolor/*/apps/*.*g
%{_datadir}/applications/xfce4-sensors.desktop
%{_mandir}/man1/xfce4-sensors.1*
