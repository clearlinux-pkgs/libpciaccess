#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpciaccess
Version  : 0.13.4
Release  : 10
URL      : http://xorg.freedesktop.org/releases/individual/lib/libpciaccess-0.13.4.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libpciaccess-0.13.4.tar.gz
Summary  : Library providing generic access to the PCI bus and devices.
Group    : Development/Tools
License  : MIT
Requires: libpciaccess-lib
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

%description dev
dev components for the libpciaccess package.


%package lib
Summary: lib components for the libpciaccess package.
Group: Libraries

%description lib
lib components for the libpciaccess package.


%prep
%setup -q -n libpciaccess-0.13.4

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
