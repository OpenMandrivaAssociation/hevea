%define name hevea 
%define version 1.09
%define release %mkrel 3

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	A fast LaTeX to HTML translator
License: 	QPL
Group: 		Publishing
URL: 		http://para.inria.fr/~maranget/hevea
Source0: 	ftp://ftp.inria.fr/INRIA/moscova/hevea/%{name}-%{version}.tar.bz2
Source1: 	ftp://ftp.inria.fr/INRIA/moscova/hevea/%{name}-%{version}-manual.tar.bz2
Requires:           tetex
Requires(post):     tetex
Requires(postun):   tetex
BuildRequires:	    ocaml >= 3.07
BuildRoot:          %{_tmppath}/%{name}-%{version}

%description
HEVEA is a LaTeX to HTML translator.  The input language is a fairly 
complete subset of LaTeX2e (old LaTeX style is also accepted) and 
the output language is HTML that is (hopefully) correct with respect 
to version 4.0 (transitional)
This package is a binary installation of the hevea system.
This software includes the Objective Caml run-time system, which is 
copyright 1995--1999 INRIA.

%prep
%setup -q
%setup -q -a 1

%build
%make LIBDIR=%{_datadir}/%{name}

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/texmf/tex/latex/%{name}
make \
	DESTDIR=%{buildroot} \
	PREFIX=%{_prefix} \
	LIBDIR=%{_datadir}/%{name} \
	LATEXLIBDIR=%{_datadir}/texmf/tex/latex \
	install

%clean
rm -rf %{buildroot}

%post -p %{_bindir}/mktexlsr

%postun -p %{_bindir}/mktexlsr


%files
%defattr(-,root,root)
%doc %{name}-%{version}-manual/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/texmf/tex/latex/%{name}.sty


