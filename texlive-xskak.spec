# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/xskak
# catalog-date 2008-10-20 22:21:01 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-xskak
Version:	1.2
Release:	6
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


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 757669
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719950
- texlive-xskak
- texlive-xskak
- texlive-xskak

