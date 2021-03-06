#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dmenu
Version  : 4.9
Release  : 9
URL      : https://dl.suckless.org/tools/dmenu-4.9.tar.gz
Source0  : https://dl.suckless.org/tools/dmenu-4.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: dmenu-bin = %{version}-%{release}
Requires: dmenu-license = %{version}-%{release}
Requires: dmenu-man = %{version}-%{release}
BuildRequires : libXinerama-dev
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xft)
Patch1: 0001-fix-prefix.diff

%description
dmenu - dynamic menu
====================
dmenu is an efficient dynamic menu for X.

%package bin
Summary: bin components for the dmenu package.
Group: Binaries
Requires: dmenu-license = %{version}-%{release}

%description bin
bin components for the dmenu package.


%package license
Summary: license components for the dmenu package.
Group: Default

%description license
license components for the dmenu package.


%package man
Summary: man components for the dmenu package.
Group: Default

%description man
man components for the dmenu package.


%prep
%setup -q -n dmenu-4.9
cd %{_builddir}/dmenu-4.9
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604357174
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1604357174
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dmenu
cp %{_builddir}/dmenu-4.9/LICENSE %{buildroot}/usr/share/package-licenses/dmenu/719999e02dc895467affff283964327ea63caa7f
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dmenu
/usr/bin/dmenu_path
/usr/bin/dmenu_run
/usr/bin/stest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dmenu/719999e02dc895467affff283964327ea63caa7f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dmenu.1
/usr/share/man/man1/stest.1
