Summary:	Highly customizable Wayland bar for Sway and Wlroots based compositors
Summary(pl.UTF-8):	Bardzo konfigurowalny pasek Waylanda do kompozytorów opartych na Sway i Wlroots
Name:		waybar
Version:	0.14.0
Release:	3
License:	MIT
Group:		Applications
Source0:	https://github.com/Alexays/Waybar/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7d413dd64391933f8b8eb37eb29dbce0
URL:		https://github.com/Alexays/Waybar/
BuildRequires:	cmake
BuildRequires:	glib2-devel
BuildRequires:	gpsd-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-layer-shell-devel >= 0.9.0
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
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pipewire-devel >= 0.3
BuildRequires:	pipewire-wireplumber-devel >= 0.5
BuildRequires:	pkgconfig
BuildRequires:	playerctl-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	scdoc >= 1.9.2
BuildRequires:	spdlog-devel >= 1:1.10.0
BuildRequires:	systemd-devel
BuildRequires:	udev-devel
BuildRequires:	upower-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.39
Requires(post,preun):	systemd-units >= 1:250.1
Requires:	gtk-layer-shell >= 0.9.0
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_user_post waybar.service

%preun
%systemd_user_preun waybar.service

%triggerpostun -- waybar < 0.10.0
if [ -f /etc/xdg/waybar/config.rpmsave ]; then
	%{__mv} -f /etc/xdg/waybar/config.jsonc{,.rpmnew}
	%{__mv} -f /etc/xdg/waybar/config{.rpmsave,.jsonc}
fi

%files
%defattr(644,root,root,755)
%doc README.md
%dir /etc/xdg/waybar
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/waybar/config.jsonc
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/waybar/style.css
%attr(755,root,root) %{_bindir}/waybar
%{systemduserunitdir}/waybar.service
%{_mandir}/man5/waybar*.5*
