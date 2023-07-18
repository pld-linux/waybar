Summary:	Highly customizable Wayland bar for Sway and Wlroots based compositors
Summary(pl.UTF-8):	Bardzo konfigurowalny pasek Waylanda do kompozytorów opartych na Sway i Wlroots
Name:		waybar
Version:	0.9.20
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/Alexays/Waybar/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3c736fb5a28b14ed327e72e93f193cdf
URL:		https://github.com/Alexays/Waybar/
BuildRequires:	date-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-layer-shell-devel
BuildRequires:	gtkmm3-devel >= 3.22.0
BuildRequires:	jsoncpp-devel >= 1.9.2
BuildRequires:	libdbusmenu-gtk3-devel
BuildRequires:	libevdev-devel
BuildRequires:	libfmt-devel >= 8.1.1
BuildRequires:	libinput-devel
BuildRequires:	libmpdclient-devel
BuildRequires:	libnl-devel >= 3.0
BuildRequires:	libsigc++-devel >= 2.0
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libxkbregistry-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja
BuildRequires:	pipewire-wireplumber-devel >= 0.4
BuildRequires:	pkgconfig
BuildRequires:	playerctl-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 2.011
BuildRequires:	scdoc >= 1.9.2
BuildRequires:	spdlog-devel >= 1:1.10.0
BuildRequires:	systemd-devel
BuildRequires:	udev-devel
BuildRequires:	upower-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols
Requires(post,preun):	systemd-units >= 1:250.1
Requires:	gtkmm3 >= 3.22.0
Requires:	jsoncpp >= 1.9.2
Requires:	libfmt >= 8.1.1
Requires:	spdlog >= 1:1.10.0
Requires:	systemd-units >= 1:250.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Highly customizable Wayland bar for Sway and Wlroots based
compositors.

%description -l pl.UTF-8
Bardzo konfigurowalny pasek Waylanda do kompozytorów opartych na Sway
i Wlroots.

%prep
%setup -q -n Waybar-%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_user_post waybar.service

%preun
%systemd_user_preun waybar.service

%files
%defattr(644,root,root,755)
%doc README.md
%dir /etc/xdg/waybar
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/waybar/config
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/waybar/style.css
%attr(755,root,root) %{_bindir}/waybar
%{systemduserunitdir}/waybar.service
%{_mandir}/man5/waybar*.5*
