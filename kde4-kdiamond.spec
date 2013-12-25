%define		_state		stable
%define		orgname		kdiamond
%define		qtver		4.8.0

Summary:	KDiamond
Name:		kde4-%{orgname}
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	9495759940010cfb3f370220d5c08ed1
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDiamond.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdiamond
%{_desktopdir}/kde4/kdiamond.desktop
%{_datadir}/apps/kdiamond
%{_datadir}/config/kdiamond.knsrc
%{_iconsdir}/*/*/apps/kdiamond.png
%{_iconsdir}/hicolor/scalable/apps/kdiamond.svgz
%{_datadir}/sounds/KDiamond-Stone-Drop.ogg
%{_datadir}/sounds/KDiamond-Stone-Swap.ogg
%{_datadir}/sounds/KDiamond-Stone-Touch.ogg
