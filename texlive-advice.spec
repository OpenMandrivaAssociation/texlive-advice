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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Like its namesake from the Emacs world, this cross-format package
implements a generic framework for extending the functionality of
selected commands and environments. It was developed as an auxiliary
package of Memoize. This is why it is, somewhat unconventionally,
documented alongside that package. This applies to both the manual and
the documented code listing.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/context
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/tex/plain
%dir %{_datadir}/texmf-dist/doc/generic/advice
%dir %{_datadir}/texmf-dist/source/generic/advice
%dir %{_datadir}/texmf-dist/tex/context/third
%dir %{_datadir}/texmf-dist/tex/generic/advice
%dir %{_datadir}/texmf-dist/tex/latex/advice
%dir %{_datadir}/texmf-dist/tex/plain/advice
%dir %{_datadir}/texmf-dist/tex/context/third/advice
%doc %{_datadir}/texmf-dist/doc/generic/advice/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/generic/advice/FILES
%doc %{_datadir}/texmf-dist/doc/generic/advice/INSTALL.md
%doc %{_datadir}/texmf-dist/doc/generic/advice/LICENCE
%doc %{_datadir}/texmf-dist/doc/generic/advice/README.md
%doc %{_datadir}/texmf-dist/source/generic/advice/Makefile
%doc %{_datadir}/texmf-dist/source/generic/advice/advice.edtx
%doc %{_datadir}/texmf-dist/source/generic/advice/advice.ins
%{_datadir}/texmf-dist/tex/context/third/advice/t-advice.tex
%{_datadir}/texmf-dist/tex/generic/advice/advice-tikz.code.tex
%{_datadir}/texmf-dist/tex/latex/advice/advice.sty
%{_datadir}/texmf-dist/tex/plain/advice/advice.tex
