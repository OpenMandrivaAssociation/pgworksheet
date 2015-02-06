%define debug_package %{nil}

Summary: A simple GUI frontend to PostgreSQL
Name:    pgworksheet
Version: 1.9
Release: 8
Source0: %{name}-%{version}.tar.bz2
Source1: pgworksheet-16.png
Source2: pgworksheet-32.png
Source3: pgworksheet-48.png
License: GPLv2+
Group: Databases
Url: http://pgworksheet.projects.postgresql.org/index.html
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
python setup.py install --root %{buildroot}

%find_lang %{name}

mkdir -p %{buildroot}{%_liconsdir,%_iconsdir,%_miconsdir}

install -m 644 %SOURCE1 %{buildroot}%_miconsdir/%name.png
install -m 644 %SOURCE2 %{buildroot}%_iconsdir/%name.png
install -m 644 %SOURCE3 %{buildroot}%_liconsdir/%name.png

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/%{name}
%{_prefix}/lib/python*/site-packages/*
%dir %{_datadir}/pixmaps/pgworksheet
%{_datadir}/pixmaps/pgworksheet.png
%{_datadir}/pixmaps/pgworksheet/*
%{_datadir}/applications/pgworksheet.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
