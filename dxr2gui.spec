Summary:	GNOME GUI for Creative Labs DXR2 devices
Summary(pl.UTF-8):	Interfejs graficzny GNOME dla urządzeń Creative Labs DXR2
Name:		dxr2gui
Version:	0.5.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://downloads.sourceforge.net/dxr2gui/%{name}.tar.gz
# Source0-md5:	c527fc3d99cf576699e3159e3291ea7a
Patch0:		%{name}-am.patch
Patch1:		%{name}-install.patch
URL:		http://dxr2gui.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME GUI for Creative Labs DXR2 devices.

%description -l pl.UTF-8
Interfejs graficzny GNOME dla urządzeń Creative Labs DXR2.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

:>acinclude.m4
# keep only AM_ACLOCAL_INCLUDE and GNOME_* macros
#head -n 374 acinclude.m4 | tail -n +163 > acinclude.m4.new
#head -n 1093 acinclude.m4 | tail -n +984 >> acinclude.m4.new
#%{__mv} acinclude.m4.new acinclude.m4

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/dxr2gui
%{_desktopdir}/dxr2gui.desktop
%{_pixmapsdir}/dxr2gui-logo.png
