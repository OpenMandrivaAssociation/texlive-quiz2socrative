%global tl_name quiz2socrative
%global tl_revision 52276

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Prepare questions for socrative quizzes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/quiz2socrative
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quiz2socrative.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quiz2socrative.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX package for preparing multiple choice, true/false, and
short answer questions. Its main purpose is to offer a tool to easily
insert rather complicated mathematical material in socrative quizzes
(see https://socrative.com). The package requires the following other
LaTeX packages: calc, etoolbox, graphicx, ifthen, listofitems, moresize,
TikZ, pgfmath, xcolor, and xparse.

