Name:		texlive-metafont-beginners
Version:	20091009
Release:	1
Summary:	An introductory tutorial for MetaFont
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/metafont/beginners
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont-beginners.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont-beginners.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
An old introduction to the use of MetaFont, that has stood the
test of time. It focuses on using the program, rather than
designing fonts, but does offer advice about understanding
errors in other people's fonts.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/fonts/metafont-beginners/metafont-for-beginners.pdf
%doc %{_texmfdistdir}/doc/fonts/metafont-beginners/metafont-for-beginners.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
