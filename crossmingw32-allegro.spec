%define		realname	allegro
Summary:	A game programming library
Summary(pl):	Biblioteka do programowania gier
Name:		crossmingw32-%{realname}
Version:	4.1.9
Release:	1
License:	Giftware
Group:		Libraries
Source0:	http://dl.sourceforge.net/alleg/%{realname}-%{version}.tar.gz
# Source0-md5:	d4423486f7aed064e10071a19fd06b1e
Patch0:		%{realname}-info.patch
Patch1:		%{realname}-examples.patch
Patch2:		%{realname}-alsa9.patch
Patch3:		%{realname}-crossmingw32.patch
Patch4:		%{realname}-opt.patch
URL:		http://alleg.sourceforge.net/
BuildRequires:	crossmingw32-dx70
BuildRequires:	crossmingw32-gcc
BuildRoot:	%{tmpdir}/%{realname}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

%prep
%setup  -q -n %{realname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
./fix.sh mingw32

CC=%{target}-gcc ; export CC
CXX=%{target}-g++ ; export CXX

%{__make} lib \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 \
	MINGDIR=$RPM_BUILD_ROOT%{arch} \
	TARGET_ARCH="%{rpmcflags}" TARGET_OPTS="-ffast-math"

%{__make} lib \
	DEBUGMODE=1 \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 \
	MINGDIR=$RPM_BUILD_ROOT%{arch} \
	TARGET_ARCH="%{rpmcflags}" TARGET_OPTS="-ffast-math"

%{__make} lib \
	PROFILEMODE=1 \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 \
	MINGDIR=$RPM_BUILD_ROOT%{arch} \
	TARGET_ARCH="%{rpmcflags}" TARGET_OPTS="-ffast-math"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{arch}
%{__make} install \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 \
	MINGDIR=$RPM_BUILD_ROOT%{arch}

%{__make} install \
	DEBUGMODE=1 \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 \
	MINGDIR=$RPM_BUILD_ROOT%{arch}

%{__make} install \
	PROFILEMODE=1 \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 \
	MINGDIR=$RPM_BUILD_ROOT%{arch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/include/*
%{arch}/lib/*
