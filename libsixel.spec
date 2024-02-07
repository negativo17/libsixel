%global commit 490ec15087e37d8e1395e4dbfb99fc543c5bae5d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20221121

Name:       libsixel
Version:    1.10.3
Release:    1.%{date}git%{shortcommit}%{?dist}
Summary:    SIXEL encoder/decoder
License:    MIT
URL:        https://github.com/libsixel/libsixel

Source0:    %{url}/archive/%{commit}.tar.gz#/libsixel-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)

%description
This package provides a C encoder/decoder implementation for DEC SIXEL graphics.

SIXEL is one of image formats for printer and terminal imaging introduced by
Digital Equipment Corp. (DEC). Its data scheme is represented as a
terminal-friendly escape sequence. So if you want to view a SIXEL image file,
all you have to do is "cat" it to your terminal.

%package devel
Summary:    SIXEL encoder/decoder development files
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%package tools
Summary:    SIXEL encoder/decoder tools
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description tools
Utilites for %{name}.

%prep
%autosetup -n libsixel-%{commit}

%build
%meson \
    -Dgd=enabled \
    -Dgdk-pixbuf2=enabled \
    -Dimg2sixel=enabled \
    -Djpeg=enabled \
    -Dlibcurl=enabled \
    -Dpng=enabled \
    -Dpython=disabled \
    -Dsixel2png=enabled \
    -Dtests=enabled

%meson_build 

%install
%meson_install

%check
%meson_test

%files
%{_libdir}/libsixel.so.*

%files devel
%{_includedir}/sixel.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/img2sixel
%{_bindir}/libsixel-config
%{_bindir}/sixel2png
%{_datadir}/bash-completion/completions
%{_datadir}/zsh/site-functions/
%{_mandir}/man1/img2sixel.1*
%{_mandir}/man1/sixel2png.1*

%changelog
* Wed Feb 07 2024 Simone Caronni <negativo17@gmail.com> - 1.10.3-1.20221121git490ec15
- First build.
