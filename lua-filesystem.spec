
%define		luaver 5.3
%define		real_name luafilesystem

%define		luasuffix %(echo %{luaver} | tr -d .)
%if "%{luaver}" == "5.1"
%define		luaincludedir %{_includedir}/lua51
%else
%define		luaincludedir %{_includedir}/lua%{luaver}
%endif
%define		lualibdir %{_libdir}/lua/%{luaver}
%define		luapkgdir %{_datadir}/lua/%{luaver}

Summary:	File System Library for Lua
Summary(hu.UTF-8):	Fájlrendszer-könyvtár Lua-hoz.
Name:		lua%{luasuffix}-filesystem
Version:	1.7.0.2
Release:	2
License:	BSD-like
Group:		Development/Languages
Source0:	https://github.com/keplerproject/luafilesystem/archive/v1_7_0_2/%{real_name}-%{version}.tar.gz
# Source0-md5:	5166c00df1599a54dc97e84852be7f0c
URL:		https://keplerproject.github.io/luafilesystem/
BuildRequires:	lua%{luasuffix}-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaFileSystem is a Lua library developed to complement the set of
functions related to file systems offered by the standard Lua
distribution.


%description -l hu.UTF-8
LuaFileSystem egy Lua könyvtár, amely függvények halmazát nyújtja,
hogy a fájlrendszeren műveleteket végezhess.

%prep
%setup -q -n %{real_name}-1_7_0_2
%{__sed} -i -e 's|PREFIX=.*|PREFIX=%{_prefix}|' config

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} %{rpmldflags} -I%{luaincludedir} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{lualibdir}
cp -p src/lfs.so $RPM_BUILD_ROOT%{lualibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md doc/us/*
# XXX: parent dir runtime dep?
%attr(755,root,root) %{lualibdir}/*.so
