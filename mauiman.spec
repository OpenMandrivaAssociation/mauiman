%define major 0

%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary:	Maui Manager Library
Name:		mauiman
Version:	1.0.2
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
Requires:	%{libname} = %{EVRD}

%description
Maui Manager Library.

%files
%{_kde5_bindir}/MauiManServer

#--------------------------------------------

%package -n %{libname}
Summary:	Library files for MauiMan
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Library files for MauiMan.

%files -n %{libname}
#{_kde5_libdir}/libMauiMan.so.%{major}*

#--------------------------------------------

%package -n %{devname}
Summary:	Development files for MauiMan
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:   %{name}-devel = %{EVRD}

%description -n %{devname}
Development files for MauiMan

%files -n %{devname}
%{_includedir}/MauiMan
%{_kde5_libdir}/cmake/MauiMan
%{_kde5_libdir}/libMauiMan.so

#--------------------------------------------

%prep
%autosetup -n %{name}-v%{version} -p1

%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
