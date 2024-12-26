%bcond_without	lua51		# lua51 package
%bcond_without	lua52		# lua52 package
%bcond_without	lua53		# lua53 package

%define		real_name	luafilesystem
%define		tag_ver		%(echo %{version} | tr . _)

Summary:	File System Library for Lua
Summary(hu.UTF-8):	Fájlrendszer-könyvtár Lua-hoz.
Name:		lua54-filesystem
Version:	1.8.0
Release:	3
License:	BSD-like
Group:		Development/Languages
Source0:	https://github.com/keplerproject/luafilesystem/archive/v%{tag_ver}/%{real_name}-%{version}.tar.gz
# Source0-md5:	b012ab5292237a8d69a193d5798b2157
URL:		https://keplerproject.github.io/luafilesystem/
BuildRequires:	lua54-devel
BuildRequires:	rpmbuild(macros) >= 1.605
%{?with_lua51:BuildRequires:	lua51-devel}
%{?with_lua52:BuildRequires:	lua52-devel}
%{?with_lua53:BuildRequires:	lua53-devel}
Requires:	lua54-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaFileSystem is a Lua library developed to complement the set of
functions related to file systems offered by the standard Lua
distribution.

%description -l hu.UTF-8
LuaFileSystem egy Lua könyvtár, amely függvények halmazát nyújtja,
hogy a fájlrendszeren műveleteket végezhess.

%package -n lua51-filesystem
Summary:	File System Library for Lua
Summary(hu.UTF-8):	Fájlrendszer-könyvtár Lua-hoz.
Requires:	lua51-libs
Obsoletes:	lua-filesystem < 1.7.0.2

%description -n lua51-filesystem
LuaFileSystem is a Lua library developed to complement the set of
functions related to file systems offered by the standard Lua
distribution.

Package for Lua 5.1.

%description -n lua51-filesystem -l hu.UTF-8
LuaFileSystem egy Lua könyvtár, amely függvények halmazát nyújtja,
hogy a fájlrendszeren műveleteket végezhess.

Package for Lua 5.1.

%package -n lua52-filesystem
Summary:	File System Library for Lua
Summary(hu.UTF-8):	Fájlrendszer-könyvtár Lua-hoz.
Requires:	lua52-libs
Obsoletes:	lua-filesystem < 1.7.0.2

%description -n lua52-filesystem
LuaFileSystem is a Lua library developed to complement the set of
functions related to file systems offered by the standard Lua
distribution.

Package for Lua 5.2.

%description -n lua52-filesystem -l hu.UTF-8
LuaFileSystem egy Lua könyvtár, amely függvények halmazát nyújtja,
hogy a fájlrendszeren műveleteket végezhess.

Package for Lua 5.2.

%package -n lua53-filesystem
Summary:	File System Library for Lua
Summary(hu.UTF-8):	Fájlrendszer-könyvtár Lua-hoz.
Requires:	lua53-libs

%description -n lua53-filesystem
LuaFileSystem is a Lua library developed to complement the set of
functions related to file systems offered by the standard Lua
distribution.

Package for Lua 5.3.

%description -n lua53-filesystem -l hu.UTF-8
LuaFileSystem egy Lua könyvtár, amely függvények halmazát nyújtja,
hogy a fájlrendszeren műveleteket végezhess.

Package for Lua 5.3.

%prep
%setup -q -n %{real_name}-%{tag_ver}

%{__mkdir} build-5.4
%{?with_lua51:%{__mkdir} build-5.1}
%{?with_lua51:%{__mkdir} build-5.2}
%{?with_lua53:%{__mkdir} build-5.3}

%build
%{__make} clean
%{__make} \
	CC="%{__cc}" \
	WARN="%{rpmcflags} %{rpmcppflags} -fPIC" \
	LUA_VERSION=5.4 \
	PREFIX=%{_prefix} \
	LUA_LIBDIR=%{_libdir}/lua/5.4

%{__mv} src/lfs.so build-5.4

%if %{with lua51}
%{__make} clean
%{__make} \
	CC="%{__cc}" \
	WARN="%{rpmcflags} %{rpmcppflags} -fPIC" \
	LUA_VERSION=5.1 \
	PREFIX=%{_prefix} \
	LUA_LIBDIR=%{_libdir}/lua/5.1

%{__mv} src/lfs.so build-5.1
%endif

%if %{with lua52}
%{__make} clean
%{__make} \
	CC="%{__cc}" \
	WARN="%{rpmcflags} %{rpmcppflags} -fPIC" \
	LUA_VERSION=5.2 \
	PREFIX=%{_prefix} \
	LUA_LIBDIR=%{_libdir}/lua/5.2

%{__mv} src/lfs.so build-5.2
%endif

%if %{with lua53}
%{__make} clean
%{__make} \
	CC="%{__cc}" \
	WARN="%{rpmcflags} %{rpmcppflags} -fPIC" \
	LUA_VERSION=5.3 \
	PREFIX=%{_prefix} \
	LUA_LIBDIR=%{_libdir}/lua/5.3

%{__mv} src/lfs.so build-5.3
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/lua/5.4
install -p build-5.4/lfs.so $RPM_BUILD_ROOT%{_libdir}/lua/5.4/lfs.so

%if %{with lua51}
install -d $RPM_BUILD_ROOT%{_libdir}/lua/5.1
install -p build-5.1/lfs.so $RPM_BUILD_ROOT%{_libdir}/lua/5.1/lfs.so
%endif

%if %{with lua52}
install -d $RPM_BUILD_ROOT%{_libdir}/lua/5.2
install -p build-5.2/lfs.so $RPM_BUILD_ROOT%{_libdir}/lua/5.2/lfs.so
%endif

%if %{with lua53}
install -d $RPM_BUILD_ROOT%{_libdir}/lua/5.3
install -p build-5.3/lfs.so $RPM_BUILD_ROOT%{_libdir}/lua/5.3/lfs.so
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md doc/us/*
%attr(755,root,root) %{_libdir}/lua/5.4/lfs.so

%if %{with lua51}
%files -n lua51-filesystem
%defattr(644,root,root,755)
%doc README.md doc/us/*
%attr(755,root,root) %{_libdir}/lua/5.1/lfs.so
%endif

%if %{with lua52}
%files -n lua52-filesystem
%defattr(644,root,root,755)
%doc README.md doc/us/*
%attr(755,root,root) %{_libdir}/lua/5.2/lfs.so
%endif

%if %{with lua53}
%files -n lua53-filesystem
%defattr(644,root,root,755)
%doc README.md doc/us/*
%attr(755,root,root) %{_libdir}/lua/5.3/lfs.so
%endif
