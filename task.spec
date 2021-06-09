Name:	 task
Version: 1.0
Release: 1%{?dist}
Summary: simple output program
License: GPL
URL:	 https://raidix.ru
Source:	 task-1.0.tar.gz

%description
%prep
%setup

%build
make PREFIX=/usr %{?_smp_mflags}

%install
make PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/task
