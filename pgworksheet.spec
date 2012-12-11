%define name pgworksheet
%define version 1.9
%define release %mkrel 6

Summary: A simple GUI frontend to PostgreSQL
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: pgworksheet-16.png
Source2: pgworksheet-32.png
Source3: pgworksheet-48.png
License: GPLv2+
Group: Databases
Url: http://pgworksheet.projects.postgresql.org/index.html
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: pyPgSQL
Requires: pygtk2.0
BuildRequires: python-devel

%description
PgWorksheet is a simple GUI frontend to PostgreSQL for executing SQL queries
and psql commands without using the psql command line tool.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root %buildroot

%find_lang %name

mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}

install -m 644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot%_iconsdir/%name.png
install -m 644 %SOURCE3 %buildroot%_liconsdir/%name.png


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %name.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %_bindir/%name
%_prefix/lib/python*/site-packages/*
%dir %_datadir/pixmaps/pgworksheet
%_datadir/pixmaps/pgworksheet.png
%_datadir/pixmaps/pgworksheet/*
%_datadir/applications/pgworksheet.desktop
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png



%changelog
* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 1.9-6mdv2011.0
+ Revision: 598911
- rebuild for py2.7

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.9-5mdv2010.0
+ Revision: 440816
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.9-4mdv2009.1
+ Revision: 325781
- rebuild

  + Michael Scherer <misc@mandriva.org>
    - fix license

* Fri Aug 22 2008 Olivier Thauvin <nanardon@mandriva.org> 1.9-3mdv2009.0
+ Revision: 275009
- force files permissions, fixing #43000

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.9-2mdv2009.0
+ Revision: 268958
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jun 08 2008 Olivier Thauvin <nanardon@mandriva.org> 1.9-1mdv2009.0
+ Revision: 216940
- 1.9

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.8.1-2mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 20:28:08 (54191)
- xdg menu

* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 20:22:18 (54190)
Import pgworksheet

* Sun Feb 12 2006 Olivier Thauvin <nanardon@mandriva.org> 1.8.1-1mdk
- 1.8.1

* Sat Nov 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.7-3mdk
- Fix BuildRequires

* Sat May 07 2005 Olivier Thauvin <nanardon@mandriva.org> 1.7-2mdk
- Fix requires

* Sat May 07 2005 Olivier Thauvin <nanardon@mandriva.org> 1.7-1mdk
- first mandriva spec

