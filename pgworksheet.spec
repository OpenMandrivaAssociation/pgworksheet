%define name pgworksheet
%define version 1.8.1
%define release %mkrel 2

Summary: A simple GUI frontend to PostgreSQL
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: pgworksheet-16.png
Source2: pgworksheet-32.png
Source3: pgworksheet-48.png
License: GPL
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
mkdir -p %buildroot%_menudir

install -m 644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot%_iconsdir/%name.png
install -m 644 %SOURCE3 %buildroot%_liconsdir/%name.png

cat > %buildroot%_menudir/%name <<EOF
?package(%name):\
    needs="X11"\
    section="Applications/Databases"\
    title="PGworksheet"\
    longtitle="GUI frontend to PostgreSQL"\
    command="%{_bindir}/%{name}"\
    icon="%{name}.png"\
    xdg="true"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS README
%_bindir/%name
%_prefix/lib/python*/site-packages/*
%dir %_datadir/pixmaps/pgworksheet
%_datadir/pixmaps/pgworksheet.png
%_datadir/pixmaps/pgworksheet/*
%_datadir/applications/pgworksheet.desktop
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png
%_menudir/%name

