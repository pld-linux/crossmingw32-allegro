%define		realname	allegro
Summary:	A game programming library - Ming32 cross version
Summary(pl):	Biblioteka do programowania gier - wersja skrośna dla Ming32
Name:		crossmingw32-%{realname}
Version:	4.1.13
Release:	1
License:	Giftware
Group:		Libraries
Source0:	http://dl.sourceforge.net/alleg/%{realname}-%{version}.tar.gz
# Source0-md5:	2a96046717cfe2ea6159cf76e11bf622
Patch0:		%{realname}-info.patch
Patch1:		%{realname}-examples.patch
Patch2:		%{realname}-opt.patch
URL:		http://alleg.sourceforge.net/
BuildRequires:	crossmingw32-dx70
BuildRequires:	crossmingw32-gcc
Requires:	crossmingw32-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		arch			%{_prefix}/%{target}

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l pl
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
./fix.sh mingw32

%{__make} lib \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 XPREFIX="%{target}-" \
	CC="%{target}-gcc" CXX="%{target}-g++" \
	MINGDIR=$RPM_BUILD_ROOT%{arch} \
	TARGET_ARCH="%{rpmcflags}" TARGET_OPTS="-ffast-math"

%{__make} lib \
	DEBUGMODE=1 \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 XPREFIX="%{target}-" \
	CC="%{target}-gcc" CXX="%{target}-g++" \
	MINGDIR=$RPM_BUILD_ROOT%{arch} \
	TARGET_ARCH="%{rpmcflags}" TARGET_OPTS="-ffast-math"

%{__make} lib \
	PROFILEMODE=1 \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 XPREFIX="%{target}-" \
	CC="%{target}-gcc" CXX="%{target}-g++" \
	MINGDIR=$RPM_BUILD_ROOT%{arch} \
	TARGET_ARCH="%{rpmcflags}" TARGET_OPTS="-ffast-math"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}/lib

%{__make} install \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 \
	MINGDIR=$RPM_BUILD_ROOT%{arch}

%{__make} install \
	DEBUGMODE=1 \
	MKDIR_OPTS="-p" \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 \
	MINGDIR=$RPM_BUILD_ROOT%{arch}

%{__make} install \
	PROFILEMODE=1 \
	MKDIR_OPTS="-p" \
	NATIVEPATH=$PATH \
	CROSSCOMPILE=1 \
	MINGDIR=$RPM_BUILD_ROOT%{arch}

%{!?debug:%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{arch}/lib/lib*.a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/include/*.h
%{arch}/include/allegro
%{arch}/lib/lib*.a
