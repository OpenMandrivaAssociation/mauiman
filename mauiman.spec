%define major 3

#define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary:	Maui Manager Library
Name:		mauiman
Version:	3.1.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv3
Url:		https://mauikit.org/
Source0:	https://invent.kde.org/maui/mauiman/-/archive/v%{version}/mauiman-v%{version}.tar.bz2

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	ninja
BuildRequires:  cmake(Qt5SystemInfo)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)

%description
Maui Manager Library.

%files
%{_bindir}/MauiManServer%{major}
%{_libdir}/libMauiMan%{major}.so
%{_datadir}/dbus-1/services/org.mauiman.Manager%{major}.service

#--------------------------------------------

%package -n %{devname}
Summary:	Development files for MauiMan
Group:		Development/KDE and Qt
Requires:   %{name} = %{EVRD}
Provides:   %{name}-devel = %{EVRD}

%description -n %{devname}
Development files for MauiMan

%files -n %{devname}
%{_includedir}/MauiMan%{major}/
%{_libdir}/cmake/MauiMan3/

#--------------------------------------------

%prep
%autosetup -n %{name}-v%{version} -p1

%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
