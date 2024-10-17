Name:		texlive-xskak
Version:	51432
Release:	2
Summary:	An extension to the skak package for chess typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xskak
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xskak.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xskak.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xskak.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/xskak
%doc %{_texmfdistdir}/doc/latex/xskak
#- source
%doc %{_texmfdistdir}/source/latex/xskak

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
