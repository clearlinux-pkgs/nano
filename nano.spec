#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0D28D4D2A0ACE884 (bensberg@telfort.nl)
#
Name     : nano
Version  : 5.1
Release  : 71
URL      : https://www.nano-editor.org/dist/v5/nano-5.1.tar.xz
Source0  : https://www.nano-editor.org/dist/v5/nano-5.1.tar.xz
Source1  : https://www.nano-editor.org/dist/v5/nano-5.1.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-3.0 GPL-3.0+
Requires: nano-bin = %{version}-%{release}
Requires: nano-data = %{version}-%{release}
Requires: nano-info = %{version}-%{release}
Requires: nano-license = %{version}-%{release}
Requires: nano-man = %{version}-%{release}
BuildRequires : glibc-locale
BuildRequires : groff
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : slang-dev
Patch1: 0001-Support-a-stateless-configuration-by-default.patch

%description
GNU nano -- a simple editor, inspired by Pico
Overview
The nano project was started because of a few "problems" with the
wonderfully easy-to-use and friendly Pico text editor.

%package bin
Summary: bin components for the nano package.
Group: Binaries
Requires: nano-data = %{version}-%{release}
Requires: nano-license = %{version}-%{release}

%description bin
bin components for the nano package.


%package data
Summary: data components for the nano package.
Group: Data

%description data
data components for the nano package.


%package doc
Summary: doc components for the nano package.
Group: Documentation
Requires: nano-man = %{version}-%{release}
Requires: nano-info = %{version}-%{release}

%description doc
doc components for the nano package.


%package info
Summary: info components for the nano package.
Group: Default

%description info
info components for the nano package.


%package license
Summary: license components for the nano package.
Group: Default

%description license
license components for the nano package.


%package man
Summary: man components for the nano package.
Group: Default

%description man
man components for the nano package.


%prep
%setup -q -n nano-5.1
cd %{_builddir}/nano-5.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597368006
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%reconfigure --disable-static --disable-browser \
--disable-extra \
--disable-help \
--disable-histories \
--disable-justify \
--disable-libmagic \
--disable-nls \
--enable-utf8
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1597368006
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nano
cp %{_builddir}/nano-5.1/COPYING %{buildroot}/usr/share/package-licenses/nano/842745cb706f8f2126506f544492f7a80dbe29b3
cp %{_builddir}/nano-5.1/COPYING.DOC %{buildroot}/usr/share/package-licenses/nano/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nano
/usr/bin/rnano

%files data
%defattr(-,root,root,-)
/usr/share/defaults/nano/nanorc
/usr/share/nano/asm.nanorc
/usr/share/nano/autoconf.nanorc
/usr/share/nano/awk.nanorc
/usr/share/nano/c.nanorc
/usr/share/nano/changelog.nanorc
/usr/share/nano/cmake.nanorc
/usr/share/nano/css.nanorc
/usr/share/nano/default.nanorc
/usr/share/nano/elisp.nanorc
/usr/share/nano/email.nanorc
/usr/share/nano/extra/ada.nanorc
/usr/share/nano/extra/debian.nanorc
/usr/share/nano/extra/fortran.nanorc
/usr/share/nano/extra/gentoo.nanorc
/usr/share/nano/extra/haskell.nanorc
/usr/share/nano/extra/povray.nanorc
/usr/share/nano/extra/spec.nanorc
/usr/share/nano/go.nanorc
/usr/share/nano/groff.nanorc
/usr/share/nano/guile.nanorc
/usr/share/nano/html.nanorc
/usr/share/nano/java.nanorc
/usr/share/nano/javascript.nanorc
/usr/share/nano/json.nanorc
/usr/share/nano/lua.nanorc
/usr/share/nano/makefile.nanorc
/usr/share/nano/man.nanorc
/usr/share/nano/markdown.nanorc
/usr/share/nano/nanohelp.nanorc
/usr/share/nano/nanorc.nanorc
/usr/share/nano/nftables.nanorc
/usr/share/nano/objc.nanorc
/usr/share/nano/ocaml.nanorc
/usr/share/nano/patch.nanorc
/usr/share/nano/perl.nanorc
/usr/share/nano/php.nanorc
/usr/share/nano/po.nanorc
/usr/share/nano/python.nanorc
/usr/share/nano/ruby.nanorc
/usr/share/nano/rust.nanorc
/usr/share/nano/sh.nanorc
/usr/share/nano/sql.nanorc
/usr/share/nano/tcl.nanorc
/usr/share/nano/tex.nanorc
/usr/share/nano/texinfo.nanorc
/usr/share/nano/xml.nanorc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/nano/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/nano.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nano/842745cb706f8f2126506f544492f7a80dbe29b3
/usr/share/package-licenses/nano/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/nano.1
/usr/share/man/man1/rnano.1
/usr/share/man/man5/nanorc.5
