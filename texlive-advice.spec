%global tl_name advice
%global tl_revision 70688

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.1
Release:	%{tl_revision}.1
Summary:	Extend commands and environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/advice
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/advice.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/advice.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/advice.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Like its namesake from the Emacs world, this cross-format package
implements a generic framework for extending the functionality of
selected commands and environments. It was developed as an auxiliary
package of Memoize. This is why it is, somewhat unconventionally,
documented alongside that package. This applies to both the manual and
the documented code listing.

