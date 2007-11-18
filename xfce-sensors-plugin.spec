%define oname xfce4-sensors-plugin

Summary:	Sensor plugin for the Xfce panel
Name:		xfce-sensors-plugin
Version:	0.10.99.2
Release:	%mkrel 2
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-sensors-plugin/%{oname}-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3.0
Requires:	lm_sensors
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	libxfcegui4-devel >= 4.3.0 
BuildRequires:	lm_sensors-devel
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A panel plugin for the Xfce panel.
It reads your hardware sensor values and displays them in your panel.

%prep
%setup -qn %{oname}-%{version}

%build 
%configure2_5x \
	--disable-static
	
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{oname}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.png
