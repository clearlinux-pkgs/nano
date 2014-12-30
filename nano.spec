#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nano
Version  : 2.4.2
Release  : 13
URL      : http://www.nano-editor.org/dist/v2.4/nano-2.4.2.tar.gz
Source0  : http://www.nano-editor.org/dist/v2.4/nano-2.4.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-3.0 GPL-3.0+
Requires: nano-bin
Requires: nano-data
Requires: nano-doc
Requires: nano-locales
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : groff
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(zlib)
BuildRequires : texinfo
BuildRequires : zlib-dev
Patch1: stateless.patch

%description
GNU nano is a small and friendly text editor.  It aims to emulate the
Pico text editor while also offering several enhancements.

%package bin
Summary: bin components for the nano package.
Group: Binaries
Requires: nano-data

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

%description doc
doc components for the nano package.


%package locales
Summary: locales components for the nano package.
Group: Default

%description locales
locales components for the nano package.


%prep
%setup -q -n nano-2.4.2
%patch1 -p1

%build
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang nano

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nano
/usr/bin/rnano

%files data
%defattr(-,root,root,-)
/usr/share/defaults/nano/nanorc
/usr/share/man/fr/man1/nano.1
/usr/share/man/fr/man1/rnano.1
/usr/share/man/fr/man5/nanorc.5
/usr/share/nano/asm.nanorc
/usr/share/nano/awk.nanorc
/usr/share/nano/c.nanorc
/usr/share/nano/changelog.nanorc
/usr/share/nano/cmake.nanorc
/usr/share/nano/css.nanorc
/usr/share/nano/debian.nanorc
/usr/share/nano/default.nanorc
/usr/share/nano/elisp.nanorc
/usr/share/nano/fortran.nanorc
/usr/share/nano/gentoo.nanorc
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
/usr/share/nano/mgp.nanorc
/usr/share/nano/mutt.nanorc
/usr/share/nano/nanorc.nanorc
/usr/share/nano/objc.nanorc
/usr/share/nano/ocaml.nanorc
/usr/share/nano/patch.nanorc
/usr/share/nano/perl.nanorc
/usr/share/nano/php.nanorc
/usr/share/nano/po.nanorc
/usr/share/nano/postgresql.nanorc
/usr/share/nano/pov.nanorc
/usr/share/nano/python.nanorc
/usr/share/nano/ruby.nanorc
/usr/share/nano/sh.nanorc
/usr/share/nano/spec.nanorc
/usr/share/nano/tcl.nanorc
/usr/share/nano/tex.nanorc
/usr/share/nano/texinfo.nanorc
/usr/share/nano/xml.nanorc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/nano/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files locales -f nano.lang 
%defattr(-,root,root,-)

