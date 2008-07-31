Summary:	Sensor plugin for the Xfce panel
Name:		xfce4-sensors-plugin
Version:	0.10.99.3
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-sensors-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
Requires:	lm_sensors
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	lm_sensors-devel
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-sensors-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A Xfce panel plugin which reads your hardware sensor 
values and displays them in your panel.

%prep
%setup -q

%build 
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.png
