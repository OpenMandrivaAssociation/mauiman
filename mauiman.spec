%define major 0

#define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary:	Maui Manager Library
Name:		mauiman
Version:	3.0.2
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv3
Url:		http://mauikit.org/
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
#{_kde5_bindir}/MauiManServer
#{_datadir}/dbus-1/services/org.mauiman.Manager.service
#{_kde5_libdir}/libMauiMan.so

#--------------------------------------------

%package -n %{devname}
Summary:	Development files for MauiMan
Group:		Development/KDE and Qt
Requires:   %{name} = %{EVRD}
Provides:   %{name}-devel = %{EVRD}

%description -n %{devname}
Development files for MauiMan

%files -n %{devname}
#{_includedir}/MauiMan
#{_kde5_libdir}/cmake/MauiMan

#--------------------------------------------

%prep
%autosetup -n %{name}-v%{version} -p1

%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
