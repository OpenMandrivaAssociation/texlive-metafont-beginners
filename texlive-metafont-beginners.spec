Name:		texlive-metafont-beginners
Version:	29803
Release:	1
Summary:	An introductory tutorial for Metafont
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/metafont/beginners
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont-beginners.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont-beginners.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
An old introduction to the use of Metafont, that has stood the
test of time. It focuses on using the program, rather than
designing fonts, but does offer advice about understanding
errors in other people's fonts.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/fonts/metafont-beginners/metafont-for-beginners.pdf
%doc %{_texmfdistdir}/doc/fonts/metafont-beginners/metafont-for-beginners.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
