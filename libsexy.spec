Summary:	Set of additional widgets for GTK+
Summary(pl.UTF-8):	Zestaw dodatkowych kontrolek dla GTK+
Name:		libsexy
Version:	0.1.11
Release:	9
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://releases.chipx86.com/libsexy/libsexy/%{name}-%{version}.tar.gz
# Source0-md5:	33c079a253270ec8bfb9508e4bb30754
Patch0:		%{name}-pc.patch
URL:		http://chipx86.com/w/index.php/Libsexy
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant-devel >= 1.2.6
BuildRequires:	gtk+2-devel >= 2:2.10.3
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	iso-codes >= 0.53
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of graphical widgets for GTK+ applications.

%description -l pl.UTF-8
Zestaw kontrolek graficznych dla programów opartych o GTK+.

%package devel
Summary:	Header files for libsexy library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsexy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	enchant-devel >= 1.2.6
Requires:	gtk+2-devel >= 2:2.10.3
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Header files for libsexy library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsexy.

%package static
Summary:	Static libsexy library
Summary(pl.UTF-8):	Statyczna biblioteka libsexy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsexy library.

%description static -l pl.UTF-8
Statyczna biblioteka libsexy.

%package apidocs
Summary:	libsexy API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libsexy
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libsexy API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libsexy.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsexy.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libsexy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsexy.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsexy.so
%{_includedir}/libsexy
%{_pkgconfigdir}/libsexy.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsexy.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libsexy
