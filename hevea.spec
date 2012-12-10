Name: 		hevea
Version: 	1.10
Release: 	6
Summary: 	A fast LaTeX to HTML translator
License: 	QPL
Group: 		Publishing
URL: 		http://para.inria.fr/~maranget/hevea
Source0: 	ftp://ftp.inria.fr/INRIA/moscova/hevea/%{name}-%{version}.tar.bz2
Source1: 	ftp://ftp.inria.fr/INRIA/moscova/hevea/%{name}-%{version}-manual.tar.bz2
Requires:           texlive-kpathsea.bin
Requires(post):     texlive-kpathsea.bin
Requires(postun):   texlive-kpathsea.bin
BuildRequires:	    ocaml >= 3.07

%description
HEVEA is a LaTeX to HTML translator.  The input language is a fairly 
complete subset of LaTeX2e (old LaTeX style is also accepted) and 
the output language is HTML that is (hopefully) correct with respect 
to version 4.0 (transitional)
This package is a binary installation of the hevea system.
This software includes the Objective Caml run-time system, which is 
copyright 1995--1999 INRIA.

%prep
%setup -q -a 1

%build
rm -f config.sh
make \
	DESTDIR=%{buildroot} \
	PREFIX=%{_prefix} \
	LIBDIR=%{_datadir}/%{name} \
	LATEXLIBDIR=%{_datadir}/texmf/tex/latex

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/texmf/tex/latex/%{name}
make install

%post
%{_bindir}/mktexlsr

%postun 
%{_bindir}/mktexlsr


%files
%doc %{name}-%{version}-manual/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/texmf/tex/latex/%{name}.sty




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10-5mdv2011.0
+ Revision: 619359
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.10-4mdv2010.0
+ Revision: 429392
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.10-3mdv2009.0
+ Revision: 240832
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2008.0
+ Revision: 78819
- new version


* Wed Jan 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-3mdv2007.0
+ Revision: 109937
- requires tetex also during %%post and %%postun, because of mktexlsr usage (thanks g?\195?\182tz)

* Wed Nov 22 2006 Jérôme Soyer <saispo@mandriva.org> 1.09-2mdv2007.1
+ Revision: 86319
- Add Requires tetex
- Add BuildRequires Tetex

* Fri Nov 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2007.0
+ Revision: 80682
- new version
- Import hevea

* Tue Sep 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-3mdk
- fix hevea.hva search

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-2mdk 
- make clean first, upstream tarball sux

* Fri Jun 03 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdk
- new release 1.08
- drop patch (merged upstream)

* Sat May 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.07-3mdk
- _really_ fix hevea.sty location (/me sux)

* Sat May 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.07-2mdk
- fix hevea.sty location
- rpmbuildupdate aware

