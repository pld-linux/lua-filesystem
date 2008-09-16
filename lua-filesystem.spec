Summary:	File System Library for Lua
Summary(hu.UTF-8):	Fájlrendszer-könyvtár Lua-hoz.
Name:		lua-filesystem
Version:	1.4.1
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	http://luaforge.net/frs/download.php/3345/luafilesystem-%{version}.tar.gz
# Source0-md5:	fe2fa6decc48f0267b4f09975750280e
URL:		http://www.keplerproject.org/luafilesystem/
BuildRequires:	lua51-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaFileSystem is a Lua library developed to complement the set of
functions related to file systems offered by the standard Lua
distribution.


%description -l hu.UTF-8
LuaFileSystem egy Lua könyvtár, amely függvények halmazát nyújtja,
hogy a fájlrendszeren műveleteket végezhess.

%prep
%setup -q -n luafilesystem-%{version}
sed -i "s|PREFIX=.*|PREFIX=%{_prefix}|" config
sed -i -r "s|(LUA_INC=.*)|\1/lua51|" config

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/lua/5.1
cp src/lfs.so $RPM_BUILD_ROOT%{_libdir}/lua/5.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/us/*
%{_libdir}/lua/5.1/*.so
