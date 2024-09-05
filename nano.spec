#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0x514BBE2EB8E1961F (bensberg@telfort.nl)
#
Name     : nano
Version  : 8.2
Release  : 94
URL      : https://www.nano-editor.org/dist/v8/nano-8.2.tar.gz
Source0  : https://www.nano-editor.org/dist/v8/nano-8.2.tar.gz
Source1  : https://www.nano-editor.org/dist/v8/nano-8.2.tar.gz.asc
Source2  : 514BBE2EB8E1961F.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-3.0 GPL-3.0+
Requires: nano-bin = %{version}-%{release}
Requires: nano-data = %{version}-%{release}
Requires: nano-info = %{version}-%{release}
Requires: nano-license = %{version}-%{release}
Requires: nano-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file-dev
BuildRequires : gettext-dev
BuildRequires : glibc-locale
BuildRequires : gnupg
BuildRequires : groff
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : slang-dev
BuildRequires : texinfo
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Support-a-stateless-configuration-by-default.patch

%description
GNU nano -- a simple editor, inspired by Pico
Purpose
Nano is a small and simple text editor for use on the terminal.
It copied the interface and key bindings of the Pico editor but
added several missing features: undo/redo, syntax highlighting,
line numbers, softwrapping, multiple buffers, selecting text by
holding Shift, search-and-replace with regular expressions, and
several other conveniences.

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 514BBE2EB8E1961F' gpg.status
%setup -q -n nano-8.2
cd %{_builddir}/nano-8.2
%patch -P 1 -p1
pushd ..
cp -a nano-8.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725545038
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static --disable-browser \
--disable-extra \
--disable-help \
--disable-histories \
--disable-justify \
--disable-libmagic \
--disable-nls \
--enable-utf8
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure --disable-static --disable-browser \
--disable-extra \
--disable-help \
--disable-histories \
--disable-justify \
--disable-libmagic \
--disable-nls \
--enable-utf8
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1725545038
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nano
cp %{_builddir}/nano-%{version}/COPYING %{buildroot}/usr/share/package-licenses/nano/842745cb706f8f2126506f544492f7a80dbe29b3 || :
cp %{_builddir}/nano-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/nano/bd75d59f9d7d9731bfabdc48ecd19e704d218e38 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/nano
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
/usr/share/nano/extra/fortran.nanorc
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
/usr/share/nano/yaml.nanorc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/nano/*

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
