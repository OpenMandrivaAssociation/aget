Name:		aget
Version:	0.4.1
Release:	3
License:	BSD-like
Group:		Networking/File transfer
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.enderunix.org/%{name}/
Source:		http://www.enderunix.org/%{name}/%{name}-%{version}.tar.gz
Patch1:		aget-0.4-fix_build_hostent.diff
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
%patch1 -p0

%build
%{make}

%install
%{__rm} -Rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
%{__cp} -p %{name} %{buildroot}%{_bindir}

%files
%doc INSTALL README README-Developer COPYING ChangeLog AUTHORS THANKS TODO
%{_bindir}/%{name}



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-2mdv2011.0
+ Revision: 609938
- rebuild

* Fri Feb 26 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.4.1-1mdv2010.1
+ Revision: 511482
- Fix Source tag
- Fix URL tag
- Fix mix of spaces and tabs
- Update to 0.4.1
- Drop old patch

* Tue Nov 10 2009 Michael Scherer <misc@mandriva.org> 0.4-5mdv2010.1
+ Revision: 463859
- fix build on a modern glibc

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.4-1mdv2008.1
+ Revision: 167820
- fix no-buildroot-tag

* Tue Aug 07 2007 Nicolas Vigier <nvigier@mandriva.com> 0.4-1mdv2008.0
+ Revision: 59969
- Import aget

