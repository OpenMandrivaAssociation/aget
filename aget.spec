Name:		aget
Version:	0.4
Release:	%mkrel 4
License:	BSD-like
Group:		Networking/File transfer
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.enderunix.org/aget/
Source:		http://www.enderunix.org/aget/aget-0.4.tar.gz
# patch taken from dag rpm
Patch0:		errno-include.patch
Summary:	Multithreaded HTTP Download Accelerator
%description
Aget is a multithreaded HTTP download accelerator.

Tests show that Aget is successfull in realizing its objectives. A file
of size 36.347.010 bytes was downloaded in 14 minutes 28 secs via wget;
whereas it was downloaded in 3 minutes and 15 seconds via aget.
Aget is an acronym for two Turkish words "Acele Getir". (Eng.: Get it fast!) 

WARNING: use with care. Some people do not appreciate that you open more
than one connection to download a file from their server.

%prep
%setup -q
%patch0 -p1

%build
%{make}

%install
%{__rm} -Rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
%{__cp} -p %{name} %{buildroot}%{_bindir}

%files
%doc INSTALL README README-Developer COPYING ChangeLog AUTHORS THANKS TODO
%{_bindir}/%{name}

