Summary:	Extension to Tcl/Tk for object-oriented programming
Summary(pl):	Rozszerzenie Tcl/Tk do programowania zorientowanego obiektowo
Name:		otcl
Version:	1.9
Release:	1
License:	MIT
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/otcl-tclcl/%{name}-%{version}.tar.gz
# Source0-md5:	d17331ef65912f43c530c57565f85600
Patch0:		tcl-lib.patch
URL:		http://otcl-tclcl.sourceforge.net/otcl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OTcl, short for MIT Object Tcl, is an extension to Tcl/Tk for
object-oriented programming.

Some of OTcl's features as compared to alternatives are:

 * designed to be dynamically extensible, like Tcl, from the ground up
 * builds on Tcl syntax and concepts rather than importing another
   language
 * compact yet powerful object programming system (draws on CLOS,
   Smalltalk, and Self)
 * fairly portable implementation (2000 lines of C, without core
   hacks)

%description -l pl
OTcl, skrót od Obiektowego Tcl MIT, jest rozszerzeniem Tcl/Tk do
programowania zorientowanego obiektowo.

Pewne z cech OTcl-a w porównaniu do alternatywnych:

 * zaprojektowany by byæ dynamicznie rozszerzalnym, jak Tcl, od zera
 * oparty na sk³adni i koncepcie Tcl zamiast importowania innego
   jêzyka
 * kompaktowy acz potê¿ny system programowania obiektowego (CLOS,
   Smalltalk oraz Self)
 * raczej przeno¶na implementacja (2000 linii C bez niskopoziomowych
   wstawek)

%package devel
Summary:	OTcl header file
Summary(pl):	Plik nag³ówkowy OTcl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{version}

%description devel
OTcl header file.

%description devel -l pl
Plik nag³ówkowy OTcl.

%package static
Summary:	OTcl static library
Summary(pl):	Biblioteka statyczna OTcl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{version}

%description static
OTcl static library.

%description static -l pl
Biblioteka statyczna OTcl.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
./configure \
	--with-tcl-ver=8.4 \
	--with-tk-ver=8.4
%{__make} \
	CFLAGS="%{rpmcflags}"
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}}

install o*sh $RPM_BUILD_ROOT%{_bindir}
install *.h $RPM_BUILD_ROOT%{_includedir}
install libotcl.* $RPM_BUILD_ROOT%{_libdir}

rm -f doc/CHANGES.html

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.html doc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
