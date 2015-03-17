Summary:	Sensor plugin for the Xfce panel
Name:		xfce4-sensors-plugin
Version:	1.2.5
Release:	5
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-sensors-plugin/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	lm_sensors-devel > 3
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libnotify)
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

%configure \
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
