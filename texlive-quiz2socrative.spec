Name:		texlive-quiz2socrative
Version:	52276
Release:	1
Summary:	Prepare questions for socrative quizzes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/quiz2socrative
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quiz2socrative.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quiz2socrative.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package for preparing multiple choice,
true/false, and short answer questions. Its main purpose is to
offer a tool to easily insert rather complicated mathematical
material in socrative quizzes (see https://socrative.com). The
package requires the following other LaTeX packages: calc,
etoolbox, graphicx, ifthen, listofitems, moresize, TikZ,
pgfmath, xcolor, and xparse.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/quiz2socrative
%doc %{_texmfdistdir}/doc/latex/quiz2socrative

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
