Summary:	Set of additional widgets for GTK+
Summary(pl):	Zestaw dodatkowych kontrolek dla GTK+
Name:		libsexy
Version:	0.1.8
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://releases.chipx86.com/libsexy/libsexy/%{name}-%{version}.tar.gz
# Source0-md5:	ddc52cc8196f9f0bf48a5c7569b6bb38
URL:		http://chipx86.com/wiki/Libsexy
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	enchant-devel >= 1.2.6
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of graphical widgets for GTK+ applications.

%description -l pl
Zestaw kontrolek graficznych dla programów opartych o GTK+.

%package devel
Summary:	Header files for libsexy library
Summary(pl):	Pliki nag³ówkowe biblioteki libsexy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	enchant-devel >= 1.2.6
Requires:	gtk+2-devel >= 2:2.10.0
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Header files for libsexy library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libsexy.

%package static
Summary:	Static libsexy library
Summary(pl):	Statyczna biblioteka libsexy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsexy library.

%description static -l pl
Statyczna biblioteka libsexy.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
LDFLAGS="%{rpmldflags} -Wl,--as-needed"
%configure \
	 --with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libsexy
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
