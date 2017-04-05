#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEDAE37B02CEB490D (emil.l.velikov@gmail.com)
#
Name     : libpciaccess
Version  : 0.13.5
Release  : 14
URL      : http://xorg.freedesktop.org/releases/individual/lib/libpciaccess-0.13.5.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libpciaccess-0.13.5.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/lib/libpciaccess-0.13.5.tar.gz.sig
Summary  : Library providing generic access to the PCI bus and devices.
Group    : Development/Tools
License  : MIT
Requires: libpciaccess-lib
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(xorg-macros)

%description
xorg/lib/libpciaccess - Generic PCI access library
Documentation of the libpciaccess API's can be generated from the
sources via the doxygen command.    Information about porting Xorg
drivers to libpciaccess is located at:

%package dev
Summary: dev components for the libpciaccess package.
Group: Development
Requires: libpciaccess-lib
Provides: libpciaccess-devel

%description dev
dev components for the libpciaccess package.


%package dev32
Summary: dev32 components for the libpciaccess package.
Group: Default
Requires: libpciaccess-lib32
Requires: libpciaccess-dev

%description dev32
dev32 components for the libpciaccess package.


%package lib
Summary: lib components for the libpciaccess package.
Group: Libraries

%description lib
lib components for the libpciaccess package.


%package lib32
Summary: lib32 components for the libpciaccess package.
Group: Default

%description lib32
lib32 components for the libpciaccess package.


%prep
%setup -q -n libpciaccess-0.13.5
pushd ..
cp -a libpciaccess-0.13.5 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491398193
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1491398193
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libpciaccess.so
/usr/lib64/pkgconfig/pciaccess.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpciaccess.so
/usr/lib32/pkgconfig/32pciaccess.pc
/usr/lib32/pkgconfig/pciaccess.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpciaccess.so.0
/usr/lib64/libpciaccess.so.0.11.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpciaccess.so.0
/usr/lib32/libpciaccess.so.0.11.1
