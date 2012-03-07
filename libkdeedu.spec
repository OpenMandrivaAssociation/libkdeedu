Name: libkdeedu
Summary: Free Educational Software based on the KDE technologies
Version: 4.8.1
Release: 1
Group: Graphical desktop/KDE
License: GPLv2
URL: http://edu.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: automoc4
# Add conflicts again khangman since some kvtml files were stored in the khangman package
Conflicts: khangman < 4.6.90
Conflicts: kanagram < 4.6.90
Obsoletes: kdeedu4 < 4.6.90
Conflicts: kdeedu4-core < 4.6.90

%description 
Runtime library for KDE Education Application

%files
%doc README AUTHORS
%dir %_kde_appsdir/kvtml/en
%_kde_appsdir/kvtml/en/animals.kvtml
%_kde_appsdir/kvtml/en/clothing.kvtml
%_kde_appsdir/kvtml/en/computers.kvtml
%_kde_appsdir/kvtml/en/currencies.kvtml
%_kde_appsdir/kvtml/en/easy.kvtml
%_kde_appsdir/kvtml/en/fruits.kvtml
%_kde_appsdir/kvtml/en/hard.kvtml
%_kde_appsdir/kvtml/en/inventions.kvtml
%_kde_appsdir/kvtml/en/medium.kvtml
%_kde_appsdir/kvtml/en/numbers.kvtml
%_kde_appsdir/kvtml/en/objects.kvtml
%_kde_appsdir/kvtml/en/people.kvtml
%_kde_appsdir/kvtml/en/professions.kvtml
%_kde_appsdir/kvtml/en/space.kvtml
%_kde_appsdir/kvtml/en/sports.kvtml
%_kde_appsdir/kvtml/en/transportation.kvtml
%_kde_appsdir/kvtml/en/vegetables.kvtml
%_kde_appsdir/kvtml/en/worldcapitals.kvtml
%_iconsdir/hicolor/*/actions/editplots.png
%_iconsdir/hicolor/*/actions/functionhelp.png
%_iconsdir/hicolor/*/actions/maximum.png
%_iconsdir/hicolor/*/actions/minimum.png
%_iconsdir/hicolor/*/actions/newdifferential.png
%_iconsdir/hicolor/*/actions/newfunction.png
%_iconsdir/hicolor/*/actions/newimplicit.png
%_iconsdir/hicolor/*/actions/newparametric.png
%_iconsdir/hicolor/*/actions/newpolar.png
%_iconsdir/hicolor/*/actions/resetview.png
%_iconsdir/hicolor/scalable/actions/deriv_func.svgz
%_iconsdir/hicolor/scalable/actions/editconstants.svgz
%_iconsdir/hicolor/scalable/actions/editplots.svgz
%_iconsdir/hicolor/scalable/actions/functionhelp.svgz
%_iconsdir/hicolor/scalable/actions/integral_func.svgz
%_iconsdir/hicolor/scalable/actions/maximum.svgz
%_iconsdir/hicolor/scalable/actions/minimum.svgz
%_iconsdir/hicolor/scalable/actions/newfunction.svgz
%_iconsdir/hicolor/scalable/actions/newparametric.svgz
%_iconsdir/hicolor/scalable/actions/newpolar.svgz
%_iconsdir/hicolor/scalable/actions/resetview.svgz
%_iconsdir/hicolor/*/actions/coords.png
%_iconsdir/hicolor/*/actions/deriv_func.png
%_iconsdir/hicolor/*/actions/editconstants.png
%_iconsdir/hicolor/*/actions/func.png
%_iconsdir/hicolor/*/actions/integral_func.png
%_iconsdir/hicolor/*/actions/lessen.png
%_iconsdir/hicolor/*/actions/magnify.png

#---------------------------------------------

%define keduvocdocument_major 4
%define libkeduvocdocument %mklibname keduvocdocument %{keduvocdocument_major}

%package -n %libkeduvocdocument
Summary: Runtime library for KDE Education Application
Group: System/Libraries

%description -n %libkeduvocdocument
Runtime library for KDE Education Application

%files -n %libkeduvocdocument
%_kde_libdir/libkeduvocdocument.so.%{keduvocdocument_major}*

#--------------------------------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: kdelibs4-devel
Requires: %libkeduvocdocument = %version-%release
Conflicts: kdeedu4-devel < 4.6.90

%description  devel
Files needed to build applications based on %{name}.

%files devel
%_kde_includedir/libkdeedu
%_kde_libdir/libkeduvocdocument.so
%_kde_libdir/libqtmmlwidget.a
%_kde_libdir/cmake/%{name}

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build

