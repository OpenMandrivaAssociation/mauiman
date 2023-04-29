%define major 0

%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Maui Manager Library
Name:		mauiman
Version:	1.0.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv3
Url:		http://mauikit.org/
Source0:	https://download.kde.org/stable/maui/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires:	extra-cmake-modules
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
%{_kde5_libdir}/libMauiMan.so.%{major}*

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
%autosetup -p1

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build