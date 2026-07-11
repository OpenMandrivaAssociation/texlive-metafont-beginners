%global tl_name metafont-beginners
%global tl_revision 29803

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	An introductory tutorial for Metafont
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/metafont/beginners
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont-beginners.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont-beginners.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An old introduction to the use of Metafont, that has stood the test of
time. It focuses on using the program, rather than designing fonts, but
does offer advice about understanding errors in other people's fonts.

