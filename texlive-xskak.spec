# revision 33602
# category Package
# catalog-ctan /macros/latex/contrib/xskak
# catalog-date 2014-04-21 13:18:36 +0200
# catalog-license lppl
# catalog-version 1.3a
Name:		texlive-xskak
Version:	1.3a
Release:	2
Summary:	An extension to the skak package for chess typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xskak
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xskak.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xskak.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xskak.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Xskak, as its prime function, saves information about a chess
game for later use (e.g., to loop through a game to make an
animated board). The package also extends the input that the
parsing commands can handle and offers an interface to define
and switch between indefinite levels of styles.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xskak/xskak-keys.sty
%{_texmfdistdir}/tex/latex/xskak/xskak-nagdef.sty
%{_texmfdistdir}/tex/latex/xskak/xskak.sty
%doc %{_texmfdistdir}/doc/latex/xskak/README
%doc %{_texmfdistdir}/doc/latex/xskak/README.TEXLIVE
#- source
%doc %{_texmfdistdir}/source/latex/xskak/xskak-src.dtx
%doc %{_texmfdistdir}/source/latex/xskak/xskak.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
