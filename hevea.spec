#hevea-debuginfo.x86_64: E: debuginfo-without-sources (Badness: 1)
%define debug_package	%{nil}

Summary:	A fast LaTeX to HTML translator
Name:		hevea
Version:	2.09
Release:	4
License:	QPL
Group:		Publishing
Url:		http://hevea.inria.fr/
Source0:	http://para.inria.fr/~maranget/hevea/distri/hevea-%{version}.tar.gz
Source1:	http://para.inria.fr/~maranget/hevea/distri/hevea-%{version}-manual.tar.gz
Source100:	%{name}.rpmlintrc
BuildRequires:	ocaml >= 3.07
Requires:	texlive-kpathsea.bin
Requires(post,postun):	texlive-kpathsea.bin

%description
HEVEA is a LaTeX to HTML translator.  The input language is a fairly
complete subset of LaTeX2e (old LaTeX style is also accepted) and
the output language is HTML that is (hopefully) correct with respect
to version 4.0 (transitional).

This package is a binary installation of the hevea system.
This software includes the Objective Caml run-time system, which is
copyright 1995--1999 INRIA.

%files
%doc %{name}-%{version}-manual/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/texmf-dist/tex/latex/%{name}.sty

%post
%{_bindir}/mktexlsr

%postun
%{_bindir}/mktexlsr

#----------------------------------------------------------------------------

%prep
%setup -q -a 1

%build
rm -f config.sh
make \
        DESTDIR=%{buildroot} \
        PREFIX=%{_prefix} \
        LIBDIR=%{_datadir}/%{name} \
        LATEXLIBDIR=%{_datadir}/texmf-dist/tex/latex

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/texmf-dist/tex/latex/%{name}
make install \
        DESTDIR=%{buildroot} \
        PREFIX=%{_prefix} \
        LIBDIR=%{_datadir}/%{name} \
        LATEXLIBDIR=%{_datadir}/texmf-dist/tex/latex

