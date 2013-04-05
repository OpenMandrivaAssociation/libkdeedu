Name:		libkdeedu
Summary:	Free Educational Software based on the KDE technologies
Version:	4.10.2
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://edu.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	automoc4
# Add conflicts again khangman since some kvtml files were stored in the khangman package
Conflicts:	khangman < 4.6.90
Conflicts:	kanagram < 4.6.90
Obsoletes:	kdeedu4 < 4.6.90
Obsoletes:	kdeedu4-core < 4.6.90

%description
Runtime library for KDE Education Application

%files
%doc README AUTHORS
%dir %{_kde_appsdir}/kvtml/en
%{_kde_appsdir}/kvtml/en/animals.kvtml
%{_kde_appsdir}/kvtml/en/clothing.kvtml
%{_kde_appsdir}/kvtml/en/computers.kvtml
%{_kde_appsdir}/kvtml/en/currencies.kvtml
%{_kde_appsdir}/kvtml/en/easy.kvtml
%{_kde_appsdir}/kvtml/en/fruits.kvtml
%{_kde_appsdir}/kvtml/en/hard.kvtml
%{_kde_appsdir}/kvtml/en/inventions.kvtml
%{_kde_appsdir}/kvtml/en/medium.kvtml
%{_kde_appsdir}/kvtml/en/numbers.kvtml
%{_kde_appsdir}/kvtml/en/objects.kvtml
%{_kde_appsdir}/kvtml/en/people.kvtml
%{_kde_appsdir}/kvtml/en/professions.kvtml
%{_kde_appsdir}/kvtml/en/space.kvtml
%{_kde_appsdir}/kvtml/en/sports.kvtml
%{_kde_appsdir}/kvtml/en/transportation.kvtml
%{_kde_appsdir}/kvtml/en/vegetables.kvtml
%{_kde_appsdir}/kvtml/en/worldcapitals.kvtml
%{_iconsdir}/hicolor/*/actions/editplots.png
%{_iconsdir}/hicolor/*/actions/functionhelp.png
%{_iconsdir}/hicolor/*/actions/maximum.png
%{_iconsdir}/hicolor/*/actions/minimum.png
%{_iconsdir}/hicolor/*/actions/newdifferential.png
%{_iconsdir}/hicolor/*/actions/newfunction.png
%{_iconsdir}/hicolor/*/actions/newimplicit.png
%{_iconsdir}/hicolor/*/actions/newparametric.png
%{_iconsdir}/hicolor/*/actions/newpolar.png
%{_iconsdir}/hicolor/*/actions/resetview.png
%{_iconsdir}/hicolor/scalable/actions/deriv_func.svgz
%{_iconsdir}/hicolor/scalable/actions/editconstants.svgz
%{_iconsdir}/hicolor/scalable/actions/editplots.svgz
%{_iconsdir}/hicolor/scalable/actions/functionhelp.svgz
%{_iconsdir}/hicolor/scalable/actions/integral_func.svgz
%{_iconsdir}/hicolor/scalable/actions/maximum.svgz
%{_iconsdir}/hicolor/scalable/actions/minimum.svgz
%{_iconsdir}/hicolor/scalable/actions/newfunction.svgz
%{_iconsdir}/hicolor/scalable/actions/newparametric.svgz
%{_iconsdir}/hicolor/scalable/actions/newpolar.svgz
%{_iconsdir}/hicolor/scalable/actions/resetview.svgz
%{_iconsdir}/hicolor/*/actions/coords.png
%{_iconsdir}/hicolor/*/actions/deriv_func.png
%{_iconsdir}/hicolor/*/actions/editconstants.png
%{_iconsdir}/hicolor/*/actions/func.png
%{_iconsdir}/hicolor/*/actions/integral_func.png
%{_iconsdir}/hicolor/*/actions/lessen.png
%{_iconsdir}/hicolor/*/actions/magnify.png

#---------------------------------------------

%define keduvocdocument_major 4
%define libkeduvocdocument %mklibname keduvocdocument %{keduvocdocument_major}

%package -n %{libkeduvocdocument}
Summary:	Runtime library for KDE Education Application
Group:		System/Libraries

%description -n %{libkeduvocdocument}
Runtime library for KDE Education Application

%files -n %{libkeduvocdocument}
%{_kde_libdir}/libkeduvocdocument.so.%{keduvocdocument_major}*

#--------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libkeduvocdocument} = %{version}-%{release}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde_includedir}/libkdeedu
%{_kde_libdir}/libkeduvocdocument.so
%{_kde_libdir}/libqtmmlwidget.a
%{_kde_libdir}/cmake/%{name}

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Wed Jul 18 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Sat Jun 30 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.1-69.1mib2010.2
- New version 4.8.1
- Obsoletes kdeedu4-core instead of Conflicts
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.0-69.1mib2010.2
+ Revision: 744298
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762491
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758080
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744559
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 739314
- New upstream tarball $NEW_VERSION

* Tue Nov 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-2
+ Revision: 732319
- Add Automoc4 as buildrequires ( to workaround a rpm5/iurt bug)
- New upstream tarball 4.7.80

* Fri Aug 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.41-1
+ Revision: 697174
- New version 4.7.41

* Sun Jul 31 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.40-1
+ Revision: 692583
- New version 4.7.40

* Tue Jul 12 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.6.95-1
+ Revision: 689649
- New version 4.7Rc2

* Mon Jul 11 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.6.90-1
+ Revision: 689524
- Fix file list
- import libkdeedu

