#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfdesktop
Version  : 4.12.3
Release  : 7
URL      : http://archive.xfce.org/src/xfce/xfdesktop/4.12/xfdesktop-4.12.3.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/xfdesktop/4.12/xfdesktop-4.12.3.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfdesktop-bin
Requires: xfdesktop-data
Requires: xfdesktop-locales
Requires: xfdesktop-doc
BuildRequires : intltool
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(exo-1)
BuildRequires : pkgconfig(garcon-1)
BuildRequires : pkgconfig(libwnck-1.0)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(sm)
BuildRequires : sed
Patch1: 0001-Set-default-wallpaper.patch

%description
================================
WHAT IS IT?
~~~~~~~~~~~
Xfdesktop is a desktop manager for the Xfce Desktop Environment. Desktop
in this respect means the root window (or, rather, a window that sits on top
of the root window). The manager handles the following tasks:
- background image / color
- root menu, window list
- minimized app icons
- file icons on the desktop (using Thunar libs)

%package bin
Summary: bin components for the xfdesktop package.
Group: Binaries
Requires: xfdesktop-data

%description bin
bin components for the xfdesktop package.


%package data
Summary: data components for the xfdesktop package.
Group: Data

%description data
data components for the xfdesktop package.


%package doc
Summary: doc components for the xfdesktop package.
Group: Documentation

%description doc
doc components for the xfdesktop package.


%package locales
Summary: locales components for the xfdesktop package.
Group: Default

%description locales
locales components for the xfdesktop package.


%prep
%setup -q -n xfdesktop-4.12.3
%patch1 -p1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang xfdesktop

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfdesktop
/usr/bin/xfdesktop-settings

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce-backdrop-settings.desktop
/usr/share/backgrounds/xfce/xfce-blue.jpg
/usr/share/backgrounds/xfce/xfce-teal.jpg
/usr/share/icons/hicolor/32x32/apps/xfce4-backdrop.png
/usr/share/icons/hicolor/32x32/apps/xfce4-menueditor.png
/usr/share/icons/hicolor/48x48/apps/xfce4-backdrop.png
/usr/share/icons/hicolor/48x48/apps/xfce4-menueditor.png
/usr/share/icons/hicolor/scalable/apps/xfce4-backdrop.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-menueditor.svg
/usr/share/pixmaps/xfce4_xicon.png
/usr/share/pixmaps/xfce4_xicon1.png
/usr/share/pixmaps/xfce4_xicon2.png
/usr/share/pixmaps/xfce4_xicon3.png
/usr/share/pixmaps/xfce4_xicon4.png
/usr/share/pixmaps/xfdesktop/xfdesktop-fallback-icon.png

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f xfdesktop.lang 
%defattr(-,root,root,-)

