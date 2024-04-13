Summary:	Batch renaming extension for Caja
Name:		caja-rename
Version:	24.4.1
Release:	1
License:	GPLv3
Group:		Graphical desktop/Other
URL:		https://github.com/tari01/caja-rename/
Source:		https://github.com/tari01/caja-rename/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	cmake-extras
BuildRequires:	intltool
BuildRequires:	ninja
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcaja-extension)

Requires:	caja

%rename caja-extension-rename

%description
An extension for Caja allowing users to rename multiple files/folders
in a single pass. The application can change the case, insert, replace
and delete strings, as well as enumerate the selection. Any changes
are instantly visible in the preview list. The user interface strives
to be as simple as possible, without confusing advanced operations.

%files -f %{name}.lang
%license COPYING
%doc CHANGELOG.md README.md
%{_libdir}/caja/extensions-2.0/libcaja-rename.so
%{_datadir}/caja/extensions/libcaja-rename.caja-extension
%{_iconsdir}/hicolor/*/apps/%{name}.svg


#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake \
	-GNinja
%ninja_build

%install
%ninja_install -C build 

# locales
%find_lang %{name} --with-gnome --all-name

