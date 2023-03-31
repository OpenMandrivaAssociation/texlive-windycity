Name:		texlive-windycity
Version:	61223
Release:	2
Summary:	A Chicago style for BibLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/windycity
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/windycity.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/windycity.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Windy City is a style for BibLaTeX that formats notes,
bibliographies, parenthetical citations, and reference lists
according to the 17th edition of The Chicago Manual of Style.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/windycity
%doc %{_texmfdistdir}/doc/latex/windycity

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
