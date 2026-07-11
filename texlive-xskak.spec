%global tl_name xskak
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	An extension to the skak package for chess typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xskak
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xskak.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xskak.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xskak.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Xskak, as its prime function, saves information about a chess game for
later use (e.g., to loop through a game to make an animated board). The
package also extends the input that the parsing commands can handle and
offers an interface to define and switch between indefinite levels of
styles.

