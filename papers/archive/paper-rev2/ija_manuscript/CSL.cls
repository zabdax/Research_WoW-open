%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                                                                              %%                              
%% CUP Standard design Large format author CLS file                             %%
%%                                                                              %%
%% Developed by Nova Techset Pvt., Ltd.,                                        %%
%%                                                                              %%
%%                                                                              %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

 
\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{CUPLStd}
              [2019/01/22 v1.0
 Standard LaTeX document class]

\newif\if@numberedref\global\@numberedreffalse %
\newif\if@authyear %
\newif\if@endproofbox \@endproofboxtrue%
\newif\ifpreview%
\newif\if@draftruleson\@draftrulesonfalse%
\newif\ifrevised%
\newif\ifopenacc%
\newif\ifnostrip%
\newif\ifonecolumn%\global\onecolumnfalse%
\newif\if@printer\global\@printertrue% 
\newif\if@cropmarkson \@cropmarksontrue

\newif\ifnote@end\note@endfalse
\newif\ifxipt

\DeclareOption{xipt}{\xipttrue}
\DeclareOption{draftrules}{\global\@draftrulesontrue}
\DeclareOption{openacc}{\openacctrue}
\DeclareOption{onecolumn}{\onecolumntrue}
\DeclareOption{preview}{\previewtrue}
\DeclareOption{revised}{\revisedtrue}
\DeclareOption{draft}{\PassOptionsToPackage{draft}{graphicx}}
\DeclareOption{a3paper}{\PassOptionsToPackage{a3}{crop}}
\DeclareOption{centre}{\PassOptionsToPackage{center}{crop}}
\DeclareOption{crop}{\PassOptionsToPackage{cam}{crop}\global\@cropmarksontrue}
\DeclareOption{nocrop}{\PassOptionsToPackage{off}{crop}\global\@cropmarksonfalse}
\DeclareOption{info}{\PassOptionsToPackage{info}{crop}}
\DeclareOption{noinfo}{\PassOptionsToPackage{noinfo}{crop}}
\DeclareOption{numbered}{\global\@numberedreftrue}
\DeclareOption{authoryear}{\global\@authyeartrue}
\DeclareOption{noproofbox}{\global\@endproofboxfalse}
\DeclareOption{proofbox}{\global\@endproofboxtrue}

\DeclareOption{printer}{\global\@printertrue}

\DeclareOption{courier}{\def\verbatim@font{\normalfont\ttfamily}}
\DeclareOption{times}{\def\verbatim@font{\normalfont\rmfamily}}
\DeclareOption{endnotes}{\ProvidesPackage{endnotes}\note@endtrue}

\ExecuteOptions{info,proofbox,twoside}
\ProcessOptions
\LoadClass[twoside,onecolumn]{article}%

\RequirePackage{soul}
\RequirePackage{graphicx,array,amsmath,amsthm,amssymb,amsfonts,endnotes}
%%\RequirePackage{upref}
\RequirePackage{upgreek}
\RequirePackage{vruler,color}
\RequirePackage{tabularx}
\RequirePackage{array}
\RequirePackage{colortbl}
\RequirePackage{stfloats}
\RequirePackage{wrapfig}
\RequirePackage{textcomp}
\RequirePackage[figuresright]{rotating}
\RequirePackage[splitrule]{footmisc}
\RequirePackage{marginnote}
\RequirePackage{amsthm}

\RequirePackage{afterpage}
\RequirePackage[table]{xcolor}

\RequirePackage{url}
\urlstyle{rm}

% Not sure if needed.
%%%\newcommand\@ptsize{0}

\RequirePackage[T1]{fontenc}

\renewcommand{\rmdefault}{ptm}%
\renewcommand{\sfdefault}{phv}%


% Default font sizes

%%%%%%%%%%%%%%%%%%%%%Fonts%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\arttitlefont}{\@setfontsize\arttitlefont{18bp}{21\p@}\fontfamily{\sfdefault}\selectfont\sf\hsize=\majorcolumn}

\newcommand{\authorfont}{\@setfontsize\authorfont{10.50bp}{16\p@}\fontfamily{\sfdefault}\selectfont\sf\everymath{\sf}\hsize=\majorcolumn}

\newcommand{\addressfont}{\@setfontsize\addressfont{7.50bp}{10.5\p@}\fontfamily{\sfdefault}\selectfont\sf\everymath{\sf}\hsize=\majorcolumn}

\newcommand{\arttypefont}{\@setfontsize\arttypefont{11.50bp}{0\p@}\fontfamily{\sfdefault}\selectfont\sf\bfseries}

\newcommand{\abstractfont}{\@setfontsize\abstractfont{9.25bp}{11.25\p@}\selectfont\hsize=\majorcolumn}

\newcommand{\sectionfont}{\@setfontsize\sectionfont{9.50bp}{11\p@}\fontfamily{\sfdefault}\selectfont\sf\bfseries}

\newcommand{\boxtextfont}{\@setfontsize\boxtextfont{8.50bp}{11\p@}\fontfamily{\sfdefault}\selectfont\sf}

\newcommand{\bibfontsize}{\@setfontsize\bibfontsize{8bp}{10\p@}\selectfont}

\newcommand{\appendixfontsize}{\@setfontsize\appendixfontsize{8bp}{10\p@}\selectfont}

\newcommand{\subsectionfont}{\@setfontsize\subsectionfont{9.50bp}{11\p@}\fontfamily{\sfdefault}\selectfont\sf\bfseries\itshape}

\newcommand{\subsubsectionfont}{\@setfontsize\subsubsectionfont{9.50bp}{11\p@}\fontfamily{\sfdefault}\selectfont\sf\itshape}

\newcommand{\mincolfont}{\@setfontsize\mincolfont{7.25bp}{9.25\p@}\fontfamily{\sfdefault}\selectfont\sf}

\newcommand{\figurecaptionfont}{\@setfontsize\figurecaptionfont{7bp}{9\p@}\fontfamily{\sfdefault}\selectfont\sf}

\newcommand{\tablecaptionfont}{\@setfontsize\tablecaptionfont{7.5bp}{9\p@}\fontfamily{\sfdefault}\selectfont\sf}

\newcommand{\tablebodyfont}{\@setfontsize\tablebodyfont{7.5bp}{9\p@}\fontfamily{\sfdefault}\selectfont\sf}

\newcommand{\tablefootnotefont}{\@setfontsize\tablefootnotefont{6.5bp}{8\p@}\fontfamily{\sfdefault}\selectfont\sf}


\newdimen\majorcolumn%
\majorcolumn=127mm%

\newdimen\minorcolumn%
\minorcolumn=49mm%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\if@printer%
\definecolor{jourcolor}{cmyk}{0,0,0,1}
\definecolor{absbackcolor}{cmyk}{0,0,0,0.12}
\else
\definecolor{jourcolor}{cmyk}{0.9,0.42,0.55,0.21}
\definecolor{absbackcolor}{cmyk}{0.14,0.08,0.1,0}
\fi

\definecolor{Theadcolor}{cmyk}{0,0,0,0.40}

\definecolor{Tbodycolor}{cmyk}{0,0,0,0.10}

\renewcommand\normalsize{%
  \@setfontsize\normalsize{9.50bp}{11.50\p@}%
  \abovedisplayskip 10\p@ \@plus 3\p@ \@minus4\p@
  \abovedisplayshortskip 3\p@ \@plus 3\p@ \@minus1\p@
  \belowdisplayshortskip 6\p@ \@plus 3\p@ \@minus2\p@
  \belowdisplayskip \abovedisplayskip
  \let\@listi\@listI}

\normalsize\baselineskip11.50pt plus 0.10pt minus 0.10pt
\let\@bls\baselineskip

%\newcommand\small{%
%  \@setfontsize\small{9\p@}{11\p@}%
%  \abovedisplayskip 6\p@ \@plus1\p@ \@minus1\p@
%  \abovedisplayshortskip 3\p@ \@plus 2\p@ \@minus1\p@
%  \belowdisplayshortskip 2\p@ \@plus 1\p@ \@minus1\p@
%  \def\@listi{\leftmargin\leftmargini
%              \listparindent \parindent
%              \topsep 6\p@ \@plus2\p@ \@minus1\p@
%              \parsep \z@ \itemsep \z@}%
%  \belowdisplayskip \abovedisplayskip}

%\newcommand\footnotesize{%
%  \@setfontsize\footnotesize{8\p@}{9\p@}%
%  \abovedisplayskip 6\p@ \@plus2\p@ \@minus4\p@
%  \abovedisplayshortskip \z@ \@plus \p@
%  \belowdisplayshortskip 1\p@ \@plus2\p@ \@minus2\p@
%  \def\@listi{\leftmargin\leftmargini
%              \listparindent 1em
%              \topsep 5\p@ \@plus 2\p@ \@minus 1\p@
%              \parsep \z@ \itemsep \z@}%
%  \belowdisplayskip \abovedisplayskip}

\def\scriptsize{\@setfontsize\scriptsize{7\p@}{9\p@}}
\def\tiny{\@setfontsize\tiny{6\p@}{7\p@}}
\def\little{\@setfontsize\little{5\p@}{6\p@}}
\def\large{\@setfontsize\large{12\p@}{14\p@}}
\def\Large{\@setfontsize\Large{14\p@}{16\p@}}
\def\LARGE{\@setfontsize\LARGE{16\p@}{18\p@}}
\def\huge{\@setfontsize\huge{24\p@}{26\p@}}
\def\Huge{\@setfontsize\Huge{25\p@}{27\p@}}

\gdef\rec#1{\gdef\@rec{#1}}\rec{}
\gdef\rev#1{\gdef\@rev{#1}}\rev{}
\gdef\acc#1{\gdef\@acc{#1}}\acc{}


\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\DeclareOldFontCommand{\sl}{\normalfont\slshape}{\@nomath\sl}
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\@nomath\sc}


% Line spacing
\setlength\lineskip{1\p@}
\setlength\normallineskip{1\p@}
\renewcommand\baselinestretch{}

% Paragraph dimensions and inter-para spacing
\setlength\parskip{0\p@}
\setlength\parindent{4mm}

% Set inter-para skips
\setlength\smallskipamount{3\p@ \@plus 1\p@ \@minus 1\p@}
\setlength\medskipamount{6\p@ \@plus 2\p@ \@minus 2\p@}
\setlength\bigskipamount{12\p@ \@plus 4\p@ \@minus 4\p@}

% Page break penalties
\@lowpenalty   51
\@medpenalty  151
\@highpenalty 301

% Disallow widows and orphans
\clubpenalty 10000
\widowpenalty 10000

% Disable page breaks before equations, allow pagebreaks after
% equations and discourage widow lines before equations.
\displaywidowpenalty 100
\predisplaypenalty   10000
\postdisplaypenalty  2500

% Allow breaking the page in the middle of a paragraph
\interlinepenalty 0

% Disallow breaking the page after a hyphenated line
\brokenpenalty 10000

% Hyphenation; don't split words into less than three characters
\lefthyphenmin=3
\righthyphenmin=3

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Page layout%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage[height=280mm,width=210mm]{crop}
\RequirePackage[%
top=65pt,%
paperwidth=210mm,%
paperheight=280mm,%
textwidth=181mm,%
textheight=240mm,
headsep=20\p@,
headheight=7\p@,
left=14.5mm,%
right=14mm]{geometry}

\RequirePackage{framed}


\addtolength{\textwidth}{-2pt}

\setlength\columnsep{5mm}
\setlength\columnseprule{0\p@}

% Footnotes
\setlength\footnotesep{0\p@}
\setlength{\skip\footins}{12\p@ \@plus 6\p@ \@minus 1\p@}



% Float placement parameters

\setcounter{totalnumber}{10}
% The maximum number of floats at the top and bottom of a page.
\setcounter{topnumber}{5}
\setcounter{bottomnumber}{5}

% The maximum part of the top or bottom of a text page that can be
% occupied by floats. This is set so that at least four lines of text
% fit on the page.
\renewcommand\topfraction{.921}
\renewcommand\bottomfraction{.921}

% The minimum amount of a text page that must be occupied by text.
% This should accomodate four lines of text.
\renewcommand\textfraction{.079}

% The minimum amount of a float page that must be occupied by floats.
\renewcommand\floatpagefraction{.887}

% The same parameters repeated for double column output
\renewcommand\dbltopfraction{.88}
\renewcommand\dblfloatpagefraction{.88}

% Space between floats
\setlength\floatsep    {18\p@ \@plus 2\p@ \@minus 2\p@}
% Space between floats and text
\setlength\textfloatsep{20\p@ \@plus 2\p@ \@minus 4\p@}
% Space above and below an inline figure
\setlength\intextsep   {18\p@ \@plus 2\p@ \@minus 2\p@}

% For double column floats
\setlength\dblfloatsep    {12\p@ \@plus 2\p@ \@minus 2\p@}
\setlength\dbltextfloatsep{20\p@ \@plus 2\p@ \@minus 4\p@}

% Space left at top, bottom and inbetween floats on a float page.
\setlength\@fptop{0\p@}         % no space above float page figures
\setlength\@fpsep{12\p@ \@plus 2fil}
\setlength\@fpbot{0\p@ \@plus 1fil}

% The same for double column
\setlength\@dblfptop{0\p@}
\setlength\@dblfpsep{12\p@ \@plus 1fil}
\setlength\@dblfpbot{0\p@ \@plus 2fil}

%%%%%%%%%%%%%%%%%%%%%%%%%%%% Article Identification %%%%%%%%%%%%%%%%%%%%%%%%%%%%

\def\@default@journal@title{Journal Title}
\let\@journal@title\@default@journal@title
\def\art-id@info{}
\def\month@info{Month~}
\def\year@info{\the\year}
\def\vol@info{00}
\def\price@info{00}
\def\issue@info{00}
\def\@print@issn{0000-0000}
\def\@price{0000-0000}
\def\@jourid{}

\newcommand{\page@extent@info}{%
  \thepage--\pageref{LastPage}}

\newcommand{\totalpage}{%
  \pageref{LastPage}}

\newcommand{\issn@line}{\@print@issn}
\newcommand{\copyright@line}{{\mincolfont\textcopyright\ Cambridge University Press and the European Microwave Association \year@info}}
%%%%%%%%%%%%\newcommand{\webcommand}{{http:$//$www.informaworld.com}}%\href{mailto:http:$//$www.informaworld.com}
\gdef\doi@string{0000000000}

% Article information user commands
\def\Year#1{\gdef\year@info{#1}}
\def\Vol#1{\gdef\vol@info{#1}}
\def\Price#1{\gdef\price@info{#1}}
\def\Issue#1{\gdef\issue@info{#1}}
\def\art-id#1{\gdef\art-id@info{#1}}
\def\Month#1{\gdef\month@info{#1}}
\newcommand\DOI[2][\@doi@fixed@field]{%
  \gdef\@doi@variable@field{#1}%
  \setDOI{#1}{#2}}
\newcommand{\setDOI}[2]{%
  \gdef\doi@string{#1#2}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Firstpage %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\firstpage}[1]{%
  \setcounter{page}{#1}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



\newskip\mincolaftskip%

\mincolaftskip=9pt%

\def\cambridgeurl{\fontsize{9bp}{0}\selectfont\sf\textbf{\href{https://cambridge.org/\@jourid}{cambridge.org/\@jourid}}}

\def\@journame{}

\def\jname#1{\gdef\@journame{\fontsize{11.50bp}{15pt}\selectfont\sf\itshape\raggedright\textcolor{jourcolor}{#1}}}\jname{Journal name}%

%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%History %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\@received{}%
\def\received#1{\gdef\@received{\mincolfont\raggedright{Received:\ }#1}}%

\def\@revised{}%
\def\revised#1{\gdef\@revised{\mincolfont\raggedright{Revised:\ }#1}}%

\def\@accepted{}%
\def\accepted#1{\gdef\@accepted{\mincolfont\raggedright{Accepted:\ }#1}}%

\def\surname#1{#1}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\def\mincolumndefns{%
\vtop{\vbox to 249mm{\hsize=\minorcolumn\parindent0pt%
\@journame\par\vskip21pt%
\cambridgeurl\par\vskip41pt%
 \ifx\@supertitle\@empty\relax\else{\arttypefont\textcolor{jourcolor}{\@supertitle}}\par\vskip\mincolaftskip\fi%
\ifx\@selfcitation\@empty\relax\else\@selfcitation\par\vskip\mincolaftskip\fi%
\ifx\@received\empty\relax\else\@received\par\fi%
\ifx\@revised\empty\relax\else\@revised\par\fi%
\ifx\@accepted\empty\relax\else\@accepted\par\vskip\mincolaftskip\fi%
 \ifx\@keywords\@empty\relax\else{\mincolfont\raggedright\textbf{\keywordsname:}\break\@keywords}\par\vskip\mincolaftskip\fi%
\ifx\@JELcode\@empty\relax\else{\mincolfont\raggedright\textbf{JEL classification:}\break\@JELcode}\par\vskip\mincolaftskip\fi%
\ifx\@MSCcode\@empty\relax\else{\mincolfont\raggedright\textbf{MSC Codes:}\break\@MSCcode}\par\vskip\mincolaftskip\fi%
\ifx\@Abbrev\@empty\relax\else{\mincolfont\raggedright\textbf{Abbreviations:}\break\@Abbrev}\par\vskip\mincolaftskip\fi%
\ifx\@corres\empty\relax\else\@corres\fi%
\vfill%
\copyright@line\par\vskip\mincolaftskip\vskip10pt%
{\includegraphics{shcup_black_mono}}}}}


\def\ps@titlepage{%
 \let\@evenfoot\relax%
 \def\@evenhead{}
 \def\@oddhead{\mincolumndefns}%
 \def\@oddfoot{}%\numfont
% \def\authormark##1{\def\leftmark{##1}}%
% \def\titlemark##1{\markboth{##1}{##1}}
}

\def\ps@headings{%
  \let\@oddfoot\@empty%
  \let\@evenfoot\@empty%
  \def\@evenhead{\hbox to \textwidth{\fontsize{9}{0}\selectfont\sf\thepage\hfill\authormark}}%\numfontrun
  \def\@oddhead{\hbox to \textwidth{\fontsize{9}{0}\selectfont\sf\textit{\titlemark}\hfill\thepage}}%\numfontrun
%  \def\authormark##1{\def\leftmark{##1}}%
%  \def\titlemark##1{\markboth{##1}{##1}}
}

% Sectional units
%

% Counters
%\newcounter{part}
%\newcounter{section}
%\newcounter{subsection}[section]
%\newcounter{subsubsection}[subsection]
%\newcounter{paragraph}[subsubsection]
%\newcounter{subparagraph}[paragraph]
%\newcounter{asection}[section]
%\newcounter{refsection}[section]
%\newcounter{appsection}[section]
%\newcounter{appsubsection}[section]
%\newcounter{figure}
%\newcounter{scheme}
%\newcounter{table}

% Form of the numbers
%\newcommand\thepage{\arabic{page}}
%\renewcommand\thesection{\Roman{section}}
%\renewcommand\thesubsection{{\Alph{subsection}}}
%\renewcommand\thesubsubsection{{\arabic{subsubsection}}}
%\renewcommand\theparagraph{\thesubsubsection.\arabic{paragraph}}
%\renewcommand\thesubparagraph{\theparagraph.\arabic{subparagraph}}
\renewcommand\theequation{\arabic{equation}}

% Form of the words
%\newcommand\contentsname{Contents}
%\newcommand\guestname{GUEST EDITORS}
%\newcommand\listfigurename{List of Figures}
%\newcommand\listtablename{List of Tables}
%\newcommand\partname{Part}
\renewcommand\appendixname{Appendix}
\renewcommand\abstractname{Abstract}
\renewcommand\refname{References}
\newcommand\bibname{{REFERENCES}}
\newcommand\normsname{Norms}
\renewcommand\indexname{Index}
\renewcommand\figurename{Fig.}
\newcommand\schemename{Scheme}
\renewcommand\tablename{Table}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Titling Macros %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Reset default command signatures

\def\title{\@ifnextchar[{\@title@wst@}{\@title@nst@}}
\def\@title@wst@[#1]{\gdef\titlemark{#1}\@title@assign@}
\def\@title@nst@#1{\gdef \titlemark{#1}\@title@assign@{#1}}
\def\@title@assign@#1{\def\@title{#1}}

%\def\author{\@ifnextchar[{\@author@wst@}{\@author@nst@}}
%\def\@author@wst@[#1]{\authormark{#1}\@author@assign@}
%\def\@author@nst@#1{\authormark{#1}\@author@assign@{#1}}
%\def\@author@assign@#1{\gdef\@author{#1}\global\@author@providedtrue}

\renewcommand{\author}[2][]{\global\@author@providedtrue%
\gdef\authormark{#1}\gdef\@author{\raggedright{#2}}%
}

\newcommand{\address}[1]{\gdef\@address{#1}}\gdef\@address{}%
\newcommand{\corres}[1]{\gdef\@corres{\raggedright\mincolfont\textbf{Author for correspondence:}\break #1}}\gdef\@corres{}%

\def\name#1{#1\ignorespaces}
\def\affil#1{{\textsuperscript{#1}}}

\def\add#1#2{{\textsuperscript{#1}}{#2}}
\def\auadd#1#2{{\textsuperscript{#1}}{#2}}
\def\ladd#1#2{{\textsuperscript{#1}}{#2}\vspace*{1.5pt}}
\def\fadd#1#2{{\textsuperscript{#1}}{#2}\newline \protect\rule{82.5mm}{.5pt}}
\def\email#1{\ifx\@corres\empty\relax\else{\ignorespaces,\ }\fi Email: #1}

\newcommand\emailrule[1]{Email: #1\par\noindent\protect\rule{82.5mm}{.5pt}}


\def\and{\MakeLowercase{and}\space\ignorespaces}

% Ifs for titling commands
\newif\if@supertitle@provided \@supertitle@providedfalse
\newif\if@specialissue@provided \@specialissue@providedfalse
\newif\if@guesteditor@provided \@guesteditor@providedfalse
\newif\if@subtitle@provided \@subtitle@providedfalse
\newif\if@author@provided \@author@providedfalse
\newif\if@sauthor@provided \@sauthor@providedfalse
\newif\if@tauthor@provided \@tauthor@providedfalse
\newif\if@fauthor@provided \@fauthor@providedfalse
\newif\if@lauthor@provided \@lauthor@providedfalse
\newif\if@aauthor@provided \@aauthor@providedfalse
\newif\if@bauthor@provided \@bauthor@providedfalse
\newif\if@date@provided \@date@providedfalse
\newif\if@dedi@provided \@dedi@providedfalse
\newif\if@classification@provided \@classification@providedfalse
\newif\if@abstract@provided \@abstract@providedfalse %%5/7/2004
\newif\if@keywords@provided \@keywords@providedfalse

\def\keywordsname{Key words}

\def\date#1{\gdef\@date{#1}\global\@date@providedtrue}
\def\dedi#1{\def\@dedi{#1}\global\@dedi@providedtrue}
\def\keywords#1{\gdef\@keywords{#1}\global\@keywords@providedtrue}
\def\subtitle#1{\def\@subtitle{{#1}}\global\@subtitle@providedtrue}
\def\supertitle#1{\def\@supertitle{{\noindent #1}}\global\@supertitle@providedtrue}
\def\specialissue#1{\def\@specialissue{{\noindent SPECIAL ISSUE:~#1}}\global\@specialissue@providedtrue}
\def\guesteditor#1{\def\@guesteditor{{\noindent \guestname:~#1}}\global\@guesteditor@providedtrue}


\newbox\@abstractbox
\renewenvironment{abstract}{\global\@abstract@providedtrue%%% 5/7/2004
  \global\setbox\@abstractbox\vbox\bgroup\abstractfont\fboxsep8pt\hsize=124mm%%
  \@afterindentfalse\@afterheading\hbox{\sf\textbf{\abstractname}}\par\vskip3pt}{\par\egroup}%

\def\@selfcitation{}%

\def\selfcitation#1{\gdef\@selfcitation{\mincolfont\raggedright\textbf{Cite this article:\ }{#1}}}

\newif\ifFpagebreak%
\def\maketitle{\SPmaketitle\bgroup\par\hskip152pt\begin{minipage}{127mm}}
\def\Fpagebreak{\end{minipage}\global\Fpagebreaktrue{\eject}\egroup\noindent}

\definecolor{red}{cmyk}{0,1,1,0}

\def\@JELcode{}

\def\JELclassification#1{\gdef\@JELcode{#1}}

\def\@MSCcode{}

\def\MSCcodes#1{\gdef\@MSCcode{#1}}

\def\@Abbrev{}

\def\Abbreviations#1{\gdef\@Abbrev{#1}}

%\AtBeginDocument{\ifFpagebreak\else\ERROR{\textcolor{red}{Please insert \slash Fpagebreak tag at the end of first page}\fi}}

%% Reimplement Titling Layout
\newcommand\SPmaketitle{\par%
      \begingroup%
    \thispagestyle{titlepage}%
    \setcounter{footnote}{0}
    \renewcommand\thefootnote{}%
    \def\@makefnmark{\hbox{\rm\@thefnmark}}%
    \long\def\@makefntext##1{%\noindent
      {${\@thefnmark}$}{##1}}%
    \global\@topnum\z@   % Prevents figures from going at top of page.
%\ifonecolumn%
   \@maketitle%
 % \else%
%\twocolumn[\@maketitle]%
%\fi%
    \@thanks%
  \endgroup%
  \@afterindentfalse
  \@afterheading%\begin{minipage}{\textwidth}
    \setcounter{footnote}{0}%
  \global\let\thanks\relax
  \global\let\maketitle\relax
  \global\let\@maketitle\relax\afterpage{\twocolumn[]\ifFpagebreak\else\@latex@error{Please insert \ Fpagebreak tag at the end of first page}\fi}
    \global\let\@thanks\@empty}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%documentation%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand\SPDmaketitle{\par%
      \begingroup%
    \thispagestyle{titlepage}%
    \setcounter{footnote}{0}
    \renewcommand\thefootnote{}%
    \def\@makefnmark{\hbox{\rm\@thefnmark}}%
    \long\def\@makefntext##1{%\noindent
      {${\@thefnmark}$}{##1}}%
    \global\@topnum\z@   % Prevents figures from going at top of page.
%\ifonecolumn%
   \@maketitle%
 % \else%
%\twocolumn[\@maketitle]%
%\fi%
    \@thanks%
  \endgroup%
  \@afterindentfalse
  \@afterheading%\begin{minipage}{\textwidth}
    \setcounter{footnote}{0}%
  \global\let\thanks\relax
  \global\let\maketitle\relax
  \global\let\@maketitle\relax%\afterpage{\twocolumn[]\ifFpagebreak\else\@latex@error{Please insert \ Fpagebreak tag at the end of first page}\fi}
    \global\let\@thanks\@empty}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\def\@maketitle{%
  \ifx\@journal@title\@default@journal@title
  \fi%
\hspace*{130pt}\vbox{\hsize=124mm%\noindent\begin{minipage}{\textwidth}%
\vspace*{-28pt}%
\textcolor{jourcolor}{\arttitlefont\raggedright\vbox{\@title}}\par\vspace*{12pt}%
\vbox{\vbox{\textcolor{jourcolor}{\rule{\majorcolumn}{.4pt}}}\par\vspace*{4pt}%
\if@author@provided%
{{\raggedright\authorfont{\hskip12pt\vbox{\@author}}}\par\vspace*{-4pt}%
\else%
\vspace{0\p@}%
\fi%
{\textcolor{jourcolor}{\rule{\majorcolumn}{.4pt}}}\par\vskip2pt}}
       \ifx\@address\empty\else
       {{\addressfont\@address}\par\vspace*{11pt}}%
    \fi%
\if@abstract@provided%
    \colorbox{absbackcolor}{\hsize=\majorcolumn\copy\@abstractbox}%
    \else
       \vspace{0\p@}%
     \fi
  \vspace{2pc plus 6\p@ minus 4\p@}
}%\end{minipage}% \end{tabular} \par
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Lastpage %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\usepackage{lastpage}
%% Last page number - from lastpage.sty
%\def\lastpage@putlabel{\addtocounter{page}{-1}%
%   \immediate\write\@auxout{\string
%   \newlabel{LastPage}{{}{\thepage}}}%
%   \addtocounter{page}{1}}
%\AtEndDocument{%
%   \message{Setting LastPage}%
%   \clearpage\lastpage@putlabel}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%\sodef\strack{}{0.185em}{0.75em}{0pt}
%sodef\runtrack{}{0.05em}{0.35em}{0pt}
%\sodef\thmtrack{}{0.09em}{\z@}{\z@}


%%%%%%%%%%%%%%%%%%%%%%%%%%% Sectioning macros %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Lowest level heading that takes a number by default
\setcounter{secnumdepth}{0}

% Reset the default section macros to help with title casing
\def\@sect#1#2#3#4#5#6[#7]#8{%
  \ifnum #2>\c@secnumdepth
    \let\@svsec\@empty
  \else
    \refstepcounter{#1}%
    \protected@edef\@svsec{\@seccntformat{\textcolor{jourcolor}{#1}}\relax}%
  \fi
  \@tempskipa #5\relax
  \ifdim \@tempskipa>\z@
    \begingroup
      #6{%
        \noindent{\hskip #3\relax\@svsec}%
          \interlinepenalty \@M
% Modified to uppercase H1's and titlecase the rest
          \ifnum #2>1\relax
             \textcolor{jourcolor}{#8}%
          \else
            \textcolor{jourcolor}{#8}%
          \fi
        \@@par}%
    \endgroup
    \csname #1mark\endcsname{#7}%
    \addcontentsline{toc}{#1}{%
      \ifnum #2>\c@secnumdepth \else
        \protect\numberline{\csname the#1\endcsname}%
      \fi
      #7}%
  \else
    \def\@svsechd{%
      #6{\hskip #3\relax
      \@svsec #8.\enspace }%
      \csname #1mark\endcsname{#7}%
      \addcontentsline{toc}{#1}{%
        \ifnum #2>\c@secnumdepth \else
          \protect\numberline{\csname the#1\endcsname}%
        \fi
        #7}}%
  \fi
  \@xsect{#5}}

% H1
\renewcommand\section{\@startsection {section}{1}{\z@}%
                                   {-16.5\p@ plus -3\p@ minus -3\p@}%
                                   {6\p@}%
                                   {\sectionfont}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
                                     {-16.5\p@ plus -1\p@ minus -2\p@}%
                                     {5\p@}%
                                     {\subsectionfont}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
                                     {-9.5\p@ plus -1\p@ minus -2\p@}%
                                     {3\p@}%
                                     {\subsubsectionfont}}
\renewcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
                                    {11\p@ plus -1\p@}%
                                    {0\p@}%
                                    {\normalfont\normalsize\itshape}}
\renewcommand\subparagraph{\undefined\@startsection{subparagraph}{5}{\parindent}%
                                       {-11\p@ plus -1\p@}%
                                       {0\p@}%
                                      {\normalfont\normalsize\bfseries}}
\def\refsection{%
  \@startsection{section}{1}{\z@}
  {-22\p@ plus -3\p@ minus -3\p@}{5.5\p@}
  {\sectionfont}}

\def\appsection{%
  \@startsection{section}{1}{\z@}
  {-24\p@ plus -2\p@ minus -1\p@}{0.0001pt}
  {\fontsize{11.5}{13.5}\selectfont\bfseries}}

\def\appsections{%
  \@startsection{section}{1}{\z@}
  {-24\p@ plus -2\p@ minus -1\p@}{14pt}
  {\fontsize{11.5}{13.5}\selectfont\bfseries}}

\def\appsubsection{%
  \@startsection{section}{1}{\z@}
  {-12\p@ plus -2\p@ minus -1\p@}{0.0001\p@}
  {\fontsize{11.5}{13.5}\selectfont\itshape}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Footnotes %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\renewcommand\footnoterule{\begingroup\leftskip\z@
\noindent\vspace{0\p@}\endgroup}

\def\footnotealign{\hskip12pt}
    \renewcommand\thefootnote{\alph{footnote}}%
\renewcommand\@makefntext[1]{%
\fontsize{7bp}{9pt}\selectfont%
    \parindent 1em%
    \noindent%
    {\footnotealign\llap{\@makefnmark}}#1}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% From ifmtarg.sty
% Copyright Peter Wilson and Donald Arseneau, 2000
\begingroup
\catcode`\Q=3
\long\gdef\@ifmtarg#1{\@xifmtarg#1QQ\@secondoftwo\@firstoftwo\@nil}
\long\gdef\@xifmtarg#1#2Q#3#4#5\@nil{#4}
\long\gdef\@ifnotmtarg#1{\@xifmtarg#1QQ\@firstofone\@gobble\@nil}
\endgroup
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%% PostScript Rotation Macros %%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newif\if@rotate \@rotatefalse
\newif\if@rotatecenter \@rotatecenterfalse
\def\rotatecenter{\global\@rotatecentertrue}
\def\rotateendcenter{\global\@rotatecenterfalse}
\def\rotate{\global\@rotatetrue}
\def\endrotate{\global\@rotatefalse}
\newdimen\rotdimen
\def\rotstart#1{\special{ps: gsave currentpoint currentpoint translate
    #1 neg exch neg exch translate}}
\def\rotfinish{\special{ps: currentpoint grestore moveto}}
\def\rotl#1{\rotdimen=\ht#1\advance\rotdimen by \dp#1
    \hbox to \rotdimen{\vbox to\wd#1{\vskip \wd#1
    \rotstart{270 rotate}\box #1\vss}\hss}\rotfinish}
\def\rotr#1{\rotdimen=\ht #1\advance\rotdimen by \dp#1
    \hbox to \rotdimen{\vbox to \wd#1{\vskip \wd#1
    \rotstart{90 rotate}\box #1\vss}\hss}\rotfinish}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%% Figures and Tables %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\newlength{\abovecaptionskip}
%\newlength{\belowcaptionskip}
\setlength{\abovecaptionskip}{6\p@}
\setlength{\belowcaptionskip}{2\p@}

%\long\def\@makecaption#1#2{%
%  \vskip\abovecaptionskip
%  \sbox\@tempboxa{#1: #2}%
%  \ifdim \wd\@tempboxa >\hsize
%    #1: #2\par
%  \else
%    \global \@minipagefalse
%    \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
%  \fi
%  \vskip\belowcaptionskip}


\newbox\schemecaptionbox
\long\def\@schemecaption#1#2{\vspace{\abovecaptionskip}\par%
  \setbox\schemecaptionbox=\hbox{#1\enskip #2}%
  \ifdim\wd\schemecaptionbox<\hsize
{\box\schemecaptionbox}
  \else
\fontsize{8}{9}\selectfont
    \unhbox\schemecaptionbox
    \par
  \fi}

%\newbox\tablecaptionbox
%\long\def\@tablecaption#1#2{\par%
%\setbox\tablecaptionbox=\hbox{\centerline{\fontsize{8}{10}\selectfont\textbf{#1}\enskip{#2}}} %
%  \ifdim\wd\tablecaptionbox<\hsize%
%\centerline{\box\tablecaptionbox}%
%\vskip3pt%
%  \else%
%    \fontsize{8}{10}\selectfont%
%    \centering{\unhbox\tablecaptionbox}%
%\vskip3pt%
%    \par%
%  \fi}%

\def\FigName{figure}

\long\def\@makecaption#1#2{%
    \ifx\FigName\@captype
      \vskip\abovecaptionskip%
        \@figurecaption{#1}{#2}%
    \else
        \@tablecaption{#1}{#2}%
      \vskip\belowcaptionskip%
    \fi%
}

\newbox\figcapbox
\newbox\capbox
\long\def\@figurecaption#1#2{{\figurecaptionfont%
  \vspace*{-3\p@}%
\setbox\figcapbox\hbox{\bgroup{\bf #1}\space{#2}\egroup}%
\ifdim\wd\figcapbox>\hsize%
\begin{minipage}{\hsize}
    \raggedright%
  {\figurecaptionfont\bf #1}{\enspace}{#2\rlap{\vphantom{y}}\par}%
\end{minipage}
\else%
\begin{minipage}{\hsize}
  \raggedright%
  {\figurecaptionfont\bf #1}{\enspace}{#2\rlap{\vphantom{y}}\par}%\par%
\end{minipage}\fi%
}}%

\newbox\tabcapbox%
\long\def\@tablecaption#1#2{%
  {\tablecaptionfont%
  \setbox\tabcapbox\vbox{%
  \raggedright%
  \textbf{#1}\enspace {#2.}\vphantom{y}}%
  \raggedright%
  {\textbf{#1}\enspace {#2}\vphantom{y}}}%
}


\renewcommand{\thefigure}{\arabic{figure}}
\renewcommand{\thetable}{\arabic{table}}


\def\thefigure{\@arabic\c@figure}
\def\fps@figure{tbp}
\def\ftype@figure{1}
\def\ext@figure{lof}
\def\fnum@figure{\figurecaptionfont\textbf{\figurename} \textbf{\thefigure.}}
%\def\figure{\@float{figure}}
%\def\endfigure{\end@float}
%\@namedef{figure*}{\@dblfloat{figure}}
%\@namedef{endfigure*}{\end@dblfloat}

\def\thescheme{\@arabic\c@scheme}
\def\fps@scheme{h}
\def\ftype@scheme{2}
\def\ext@scheme{los}
\def\fnum@scheme{\MakeUppercase{\schemename}~\thescheme.}
\def\scheme{\let\@makecaption\@schemecaption\@float{scheme}}
\def\endscheme{\end@float}
\@namedef{scheme*}{\let\@makecaption\@schemecaption\@dblfloat{scheme}}
\@namedef{endscheme*}{\end@dblfloat}

\def\fps@table{tbp}
\def\ftype@table{3}
\def\ext@table{lot}
\def\fnum@table{{\tablename}\enspace\thetable.}
%\def\table{\let\@makecaption\@tablecaption\@float{table}}
%\def\endtable{\end@float}
%\@namedef{table*}{\let\@makecaption\@tablecaption\@dblfloat{table}}
%\@namedef{endtable*}{\end@dblfloat}

\newdimen\tempdime
\newbox\temptbox

\newlength{\abovefigskip}
\newlength{\belowfigskip}
\setlength{\abovefigskip}{\z@}
\setlength{\belowfigskip}{\z@}

\def\toprule{\noalign{\ifnum0=`}\fi
  \hrule \@height 0.5\p@
  \hrule \@height 0\p@ \@width \z@
  \futurelet \@tempa\@xhline}

\def\midrule{\noalign{\ifnum0=`}\fi
  \hrule \@height 4.5\p@ \@width \z@
  \hrule \@height 0.5\p@
  \hrule \@height 5\p@ \@width\z@
  \futurelet \@tempa\@xhline}

\def\botrule{\noalign{\ifnum0=`}\fi
  \hrule \@height 4\p@ \@width \z@
  \hrule \@height 1\p@
  \futurelet \@tempa\@xhline}

% Table and array parameters
%\setlength\arraycolsep{.5em}
\setlength\tabcolsep{0em}
\setlength\arrayrulewidth{.3pt}
\setlength\doublerulesep{2.5pt}
%\renewcommand\arraystretch{1}

%\def\hrulefill{\leavevmode\leaders\hrule height .25pt\hfill\kern\z@}

\newcolumntype{P}[1]{>{\raggedright\let\\\@arraycr\hangindent1em}p{#1}}

\def\nullbotrule{}%

\newdimen\httabcaptnbox%
\newdimen\tabcaphtdimen%
\newdimen\tabcaphtdimencalc%
\newbox\tabcabtbox%
\newif\ifOsidecap%
\newif\ifEsidecap%
\newdimen\tempdime
\newbox\temptbox
\newif\ifsidewaystable%
\newcommand\processtable[3]{\begingroup%
    \setbox\temptbox=\hbox{\tablebodyfont{#2}}%
    \tempdime\wd\temptbox%
    \ifdim\tempdime>1.01\textwidth%
      \global\sidewaystabletrue%
    \fi%
    \@processtable{#1}{#2}{#3}{\tempdime}%
   \global\sidewaystablefalse%
\endgroup}%

\def\raggedcenter{\leftskip=0pt plus 0.5fil\rightskip=0pt plus 0.5fil%
\parfillskip=0pt}%

\newenvironment{@processtable}[4]{\renewcommand\arraystretch{1.7}%
\setbox\tabcabtbox\hbox{\tablebodyfont{#2}}%
\tabcaphtdimencalc\wd\tabcabtbox%
\httabcaptnbox\ht\tabcabtbox%
\advance\httabcaptnbox by \dp\tabcabtbox%
\setbox4=\hbox to \hsize{\fboxsep0pt\hss%
    \begin{minipage}[t]{#4}%
    \raggedcenter%
    \caption{#1}\par%
    \colorbox{Tbodycolor}{{\tablebodyfont\noindent\ignorespaces #2}}\par\vspace*{0pt}%
    {\ifx!#3!\else{\tablefootnotefont#3}\fi}%
    \end{minipage}%
   \hss}
\box4\par}%


\def\Theadrule#1{%
\ifnum#1=1%
\toprule\noalign{\hbox{\smash{\textcolor{Theadcolor}{\rule[-15pt]{\hsize}{15pt}}}}}%
\else%
\ifnum#1=2%
\toprule\noalign{\hbox{\smash{\textcolor{Theadcolor}{\rule[-24pt]{\hsize}{24pt}}}}}%
\else%
\ifnum#1=3%
\hline\noalign{\hbox{\smash{\textcolor{Theadcolor}{\rule[-33pt]{\hsize}{33pt}}}}}%
\else%
\ifnum#1=4%
\hline\noalign{\hbox{\smash{\textcolor{Theadcolor}{\rule[-42pt]{\hsize}{42pt}}}}}%
\else%
\ifnum#1=5%
\hline\noalign{\hbox{\smash{\textcolor{Theadcolor}{\rule[-51pt]{\hsize}{51pt}}}}}%
\else%
\ifnum#1=6%
\hline\noalign{\hbox{\smash{\textcolor{Theadcolor}{\rule[-60pt]{\hsize}{60pt}}}}}%
\else\fi\fi\fi\fi\fi\fi}%


%%%%table notes%%%%
\newenvironment{tablenotes}{\list{}{\setlength{\labelsep}{0pt}%
\setlength{\labelwidth}{0pt}%
\setlength{\leftmargin}{0pt}%
\setlength{\rightmargin}{0pt}%
\setlength{\topsep}{2pt}%
\setlength{\itemsep}{0pt}%
\setlength{\partopsep}{0pt}%
\setlength{\listparindent}{0em}%
\setlength{\parsep}{0pt}}%
\item\relax%
}{\endlist}%

%\newbox\taheadbox%
%\newcommand{\btabhead}{\hbox\bgroup\smash\bgroup\begin{minipage}{\hsize}}%

%\newcommand{\etabhead}{\end{minipage}\egroup\egroup}%

%%\AtBeginEnvironment{tabular}{\\\noalign{\rowcolor{Theadcolor}}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Lists %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\labelenumi{({\rm\roman{enumi}})}
\def\theenumi{\arabic{enumi}}
\def\labelenumii{{\rm(\alph{enumii})}}
\def\theenumii{\alph{enumii}}
\def\p@enumii{\theenumi}
\def\labelenumiii{{\rm(\arabic{enumiii})}}
\def\theenumiii{\roman{enumiii}}
\def\p@enumiii{\theenumi(\theenumii)}
\def\labelenumiv{{\rm(\arabic{enumiv})}}
\def\theenumiv{\Alph{enumiv}}
\def\p@enumiv{\p@enumiii\theenumiii}
\def\labelitemi{$\bullet$}
\def\labelitemii{$\bullet$}
\def\labelitemiii{$\bullet$}
\def\labelitemiv{$\bullet$}

\setlength{\leftmargini}{11pt}
\setlength{\leftmarginii}{15pt}
\setlength{\leftmarginiii}{\z@}
\setlength{\leftmarginiv}{\z@}

\def\enumargs{%
   \partopsep     \z@
   \itemsep       0\p@
   \parsep        \z@
   \leftmargin    0pt
   \rightmargin   \z@
   \labelsep      -0.85em
   \listparindent \z@
   \itemindent    \z@}

\def\enumerate{%
    \@ifnextchar[{\@numerate}{\@numerate[(3)]}}

\def\@numerate[#1]{%
     \ifnum \@enumdepth >3 \@toodeep\else
     \advance\@enumdepth \@ne
     \edef\@enumctr{enum\romannumeral\the\@enumdepth}
     \list{\csname label\@enumctr\endcsname}{%
       \enumargs
       \setlength{\leftmargin}{\csname leftmargin\romannumeral\the\@listdepth\endcsname}
       \usecounter{\@enumctr}
       \settowidth\labelwidth{#1}
       \addtolength{\leftmargin}{\labelwidth}
       \addtolength{\leftmargin}{\labelsep}
       \def\makelabel##1{\llap{##1}}}%
     \fi
   }
\def\endenumerate{\endlist\advance \@listdepth -1}


\def\romenumargs{%
   \partopsep     \z@
   \itemsep       0\p@
   \parsep        \z@
   \leftmargin    15.2pt
   \rightmargin   \z@
   \labelsep      -1.2em
   \listparindent \z@
   \itemindent    \z@}

\def\romenumerate{%
    \@ifnextchar[{\@numerate}{\@romnumerate[(iii)]}}

\def\@romnumerate[#1]{%
     \ifnum \@enumdepth >3 \@toodeep\else
     \advance\@enumdepth \@ne
     \edef\@enumctr{enum\romannumeral\the\@enumdepth}
     \list{\csname label\@enumctr\endcsname}{%
       \romenumargs
       \setlength{\leftmarginii}{\csname leftmargin\romannumeral\the\@listdepth\endcsname}
       \usecounter{\@enumctr}
       \settowidth\labelwidth{#1}
       \addtolength{\leftmargin}{\labelwidth}
       \addtolength{\leftmargin}{\labelsep}
       \def\makelabel##1{\llap{##1}}}%
     \fi
   }
\def\endromenumerate{\endlist\advance \@listdepth -1}


% Changes to the list parameters for itemize
\def\itemargs{%
   \partopsep     \z@
   \itemsep       0pt
   \parsep        \z@
   \rightmargin   \z@
   \labelsep      0.5em
   \listparindent \parindent
   \itemindent    \z@}

\def\itemize{%
    \@ifnextchar[{\@itemize}{\@itemize[$\bullet$]}}

\def\@itemize[#1]{%
     \ifnum \@itemdepth >3 \@toodeep\else
     \advance\@itemdepth \@ne
     \edef\@itemctr{item\romannumeral\the\@itemdepth}
     \list{\csname label\@itemctr\endcsname}{%
       \itemargs
       \setlength{\leftmargin}{7.1pt}
       \def\makelabel##1{\hss \llap{##1}}}%
     \fi
   }
\let\enditemize\endlist

\setlength{\topsep}{6\p@}% \@plus 1\p@ \@minus 1\p@}
\setlength{\itemsep}{\z@}

\def\@listI{\leftmargin\leftmargini\topsep6.5\p@ plus 4\p@}
\let\@listi\@listI
\@listi
\def\@listii{\leftmargin\leftmarginii\topsep\z@}
\def\@listiii{\leftmargin\leftmarginiii\topsep\z@}
\def\@listiv{\leftmargin\leftmarginiv\topsep\z@}
\def\@listv{\leftmargin\leftmarginv\topsep\z@}
\def\@listvi{\leftmargin\leftmarginvi\topsep\z@}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% unnumbered list %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\renewenvironment{description}{%
  \begin{list}{}{%
      \usecounter{enumi}%
      \setlength{\itemsep}{\z@}%
      \setlength{\labelwidth}{\z@}%
      \setlength{\leftmargin}{1em}%
      \setlength{\itemindent}{-1em}}}%
{\end{list}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Extracts %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\quotation{\par\begin{list}{}{%\fontsize{9}{10}\selectfont%  Extracts in small type
      \setlength{\topsep}{\medskipamount}%
      \setlength{\itemsep}{\z@}%
      \setlength\labelwidth{\z@}%
      \setlength\labelsep{\z@}%
      \setlength\leftmargin{18pt}%
      \setlength\rightmargin{18pt}%
      \listparindent \parindent}%
  \item[\vrule width\z@ height 9\p@]}
\def\endquotation{\end{list}}
\let\quote\quotation
\let\endquote\endquotation
\newcommand{\source}[1]{\par{\textit{Source}: {\rm #1}}}
\newcommand{\note}[1]{\par{\textit{Note}: {\rm #1}}}
\newcommand{\notess}[1]{\par{\textit{Notes}: {\rm #1}}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% programs %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

{\obeyspaces\global\let =\ }

\newskip\cmskipamount%
\cmskipamount=12pt plus 6pt minus 3pt%

\def\cmskip{\removelastskip\vskip\cmskipamount}

\long\def\bCM{\begingroup\parindent=0pt\cmskip\ttfamily%
\obeylines\obeyspaces}%

\def\eCM{\cmskip\endgroup}%

\long\def\tbCM{\begingroup\parindent=0pt\cmskip%
\obeylines\obeyspaces}%

\def\teCM{\cmskip\endgroup}%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\renewcommand{\proofname}{\textit{Proof}}

\renewcommand{\qedsymbol}{\ensuremath{\square}}
\renewenvironment{proof}[1][\proofname]{\par
  \if@endproofbox\pushQED{\qed}\fi%
  \normalfont
  \topsep\bigskipamount
  \labelsep=0.5em\relax
  \trivlist
  \item[\quad\hskip\labelsep
        {#1}{\rm:}]\ignorespaces
}{%
  \if@endproofbox\popQED\fi
  \endtrivlist\@endpefalse
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Counter for saving the section numbering depth
\newcounter{savesecnumdepth}

%%%%%%%%%%%%%%%%%%%%%%%%%% Acknowledgments %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\providecommand{\ackname}{{\fontsize{8bp}{10pt}\fontfamily{\sfdefault}\selectfont\sf\bfseries\textcolor{jourcolor}{Acknowledgements.\ }}}

\newcommand{\ack}[2][]{\bgroup\par\vskip12pt plus2pt\parindent0pt{\fontsize{8bp}{10pt}\fontfamily{\sfdefault}\selectfont\sf\bfseries\textcolor{jourcolor}{#1.\ }} \fontsize{8bp}{10pt}\selectfont{#2}\egroup}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\ifnote@end\let\footnote\endnote\fi%

\renewcommand{\notesname}{{Notes}}

\newenvironment{notes}[1][Notes]{\par
\setcounter{secnumdepth}{0}
\section{{#1}}%
}{\par}

%%%%%%%%%%%%%%%%%%%%%%%%% Nomenclature %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\providecommand{\nomenname}{Nomenclature}
\newcommand{\nomen}[1][\nomenname]{%
  \setcounter{savesecnumdepth}{\value{secnumdepth}}%
  \setcounter{secnumdepth}{0}%
  \refsection{#1}%
\vspace*{5pt}
  \setcounter{secnumdepth}{\value{savesecnumdepth}}%
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{hyperref}
%%%\hypersetup{
%%%    colorlinks,%
%%%    citecolor=blue,%
%%%    filecolor=blue,%
%%%    linkcolor=blue,%
%%%    urlcolor=blue
%%%}
\if@numberedref\relax%
\RequirePackage[numbers,sort&compress]{natbib}%
\else%
\RequirePackage[authoryear]{natbib}\fi%

\if@numberedref\relax%
\bibpunct{[}{]}{,}{n}{,}{;}
\renewcommand\@biblabel[1]{#1}
\renewenvironment{thebibliography}[1]{%
  \begingroup%
  \bibfontsize%
  \setcounter{secnumdepth}{0}%
  \refsection*{\textcolor{jourcolor}{\refname}}%
  \begin{list}{\arabic{enumi}}{%
      \usecounter{enumi}%
      \setlength{\itemsep}{0pt}
      \setlength\leftmargin{\z@}%
      \setlength{\labelsep}{0.5em}%
      \setlength{\parsep}{0pt}%
      \settowidth{\labelwidth}{#1}%
      \addtolength{\leftmargin}{\labelwidth}%
      \addtolength{\leftmargin}{\labelsep}}}%
{\end{list}\endgroup}
\else%
\def\@biblabel#1{}
\renewenvironment{thebibliography}{%
  \begingroup%
  \bibfontsize%
  \setcounter{secnumdepth}{0}%
  \refsection*{\textcolor{jourcolor}{\refname}}%
  \begin{list}{}{%
 \setlength{\itemsep}{0pt}%
 \setlength{\parsep}{0pt}%
       \setlength{\labelwidth}{0pt}%
      \setlength{\leftmargin}{9pt}%
      \setlength{\itemindent}{-9pt}}}%
{\end{list}\endgroup}
\fi%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\newskip\normskip
\setlength\normskip{6pt}

\newenvironment{normes}{%
  \begingroup
  \footnotesize\parindent=0pt
  \setcounter{secnumdepth}{0}
  \vskip\normskip
  {\fontsize{10}{12}\selectfont\bf\normsname}%
  \begin{list}{}{%
      \usecounter{enumi}%
      \setlength{\itemsep}{\z@}%
      \setlength{\labelwidth}{0pt}%
      \setlength{\leftmargin}{2em}%
      \setlength{\itemindent}{-2em}}}%
{\end{list}\endgroup}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Index %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newif\if@restonecol
\def\theindex{\@mainmatterfalse
  \@restonecoltrue\if@twocolumn\@restonecolfalse\fi
  \begingroup\parindent \z@
  \addcontentsline{toc}{section}{Index}
  \columnseprule \z@
  \columnsep 1pc\section*{\indexname} %Subject or Author here
  \parskip\z@ plus .3\p@\relax\let\item\idxitem\fontsize{8\p@}{10\p@}\selectfont}
\def\idxitem{\par\raggedright\hangindent 3em}
\def\subitem{\par\penalty1000\raggedright\hangindent 3em\hspace*{1em}}
\def\subsubitem{\par\penalty1000\raggedright\hangindent 3em\hspace*{2em}}
\def\endtheindex{\if@restonecol\endgroup\onecolumn\else\clearpage\fi}
\def\indexspace{\par \vskip 18\p@ plus 12\p@ minus 12\p@\relax}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%% Appendix %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newif\ifappend % Are we in the Appendix?
\def\appendix{\par\appendixfontsize%
  \setcounter{secnumdepth}{0}%
  \renewcommand{\thesection}{\Alph{section}}
  \renewcommand{\@seccntformat}[1]{{\csname
  the##1\endcsname}\quad}
\def\thetable{\thesection\@arabic\c@table}
\def\thefigure{\thesection\@arabic\c@figure}
\renewcommand\theequation{\thesection\arabic{equation}}
        \setcounter{section}{0}
        \setcounter{table}{0}
        \setcounter{equation}{0}
        \setcounter{subsection}{0}
        \appendtrue}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Override settings in MathTime back to TeX defaults
\DeclareMathSizes{5}     {5}   {5}  {5}
\DeclareMathSizes{6}     {6}   {5}  {5}
\DeclareMathSizes{7}     {7}   {5}  {5}
\DeclareMathSizes{8}     {8}   {6}  {5}
\DeclareMathSizes{9}     {9}   {7}  {5}
\DeclareMathSizes{10}   {10}   {7}  {5}
\DeclareMathSizes{12}   {12}   {9}  {7}

%Math parameters
\setlength{\jot}{5\p@}
\skip\@mpfootins = \skip\footins
\fboxsep=6\p@
\fboxrule=.25\p@

\medmuskip=4mu% plus 2mu minus 4mu
\thickmuskip=5mu% plus 5mu

\vbadness=9999
\tolerance=9999
\doublehyphendemerits=10000
\doublehyphendemerits 640000
\finalhyphendemerits  1000000

\flushbottom
\frenchspacing
%%%\onecolumn
\pagestyle{headings}

% Author queries
\fboxsep=4\p@
\fboxrule=0.5\p@

\newcommand{\query}[2][0pt]{%
  \marginpar{%\vspace*{#1}%
    {\parbox{\marginparwidth}{%
     \raggedright\small{\bf #2}}}}}

\newcommand{\leftquery}[2][0pt]{%
  \marginpar{%\vspace*{#1}%
    {\parbox{\marginparwidth}{%
     \raggedright\small{\hskip5pc\bf #2}}}}}


\newenvironment{queries}[1][9.99]{%
  \begingroup
  \thispagestyle{empty}
  \advance\@enumdepth \@ne
  \edef\@enumctr{enum\romannumeral\the\@enumdepth}
  \def\labelenumi{\arabic{enumi})}
  \def\labelenumii{\alph{enumii})}
  \begin{list}{\csname label\@enumctr\endcsname}{%\small%
      \setlength{\topsep}{12\p@}%
    \setlength{\itemsep}{6\p@}%
      \setlength{\leftmargin}{\z@}%
      \settowidth{\labelwidth}{\bfseries#1}%
      \setlength{\labelsep}{1.5em}%
      \addtolength{\leftmargin}{\labelwidth}%
      \addtolength{\leftmargin}{\labelsep}
      \def\makelabel##1{\hss\llap{{##1}}}
    }}
{\end{list}\endgroup}

% Short-form coding
\newcommand\tetal{{{\rm et~al.}}}
\newcommand\etal{\textit{et~al.}}
\newcommand\eg{\textit{e.g.}}
\newcommand\ie{\textit{i.e.}}
\let\endash\textendash

\def\dbond{\raise0.18ex\hbox{$=$}}
\def\bond{\raise0.18ex\hbox{$-$}}

\def\endash{--}
\def\emdash{\,--\,}
\def\sdot#1{{\buildrel{\scriptscriptstyle\bullet}\over{\hbox{$#1$}}}}
\def\ssdot#1{{\buildrel{\scriptscriptstyle\bullet\bullet}\over{\hbox{$#1$}}}}

\def\refmsg{\noindent\hangindent=1em}%

\def\z{\phantom}

%%%For New Table

\newcount\mscount
\def\multispan#1{\omit \mscount#1\relax
  \loop\ifnum\mscount>\@ne \sp@n\repeat}
\def\sp@n{\span\omit\advance\mscount\m@ne}

\hyphenation{Table}
\hyphenation{Figure}
\hyphenation{Section}
\hyphenation{equation}
\hyphenation{Theorem}
\hyphenation{Lemma}
\hyphenation{Algorithm}
\hyphenation{Definition}
\hyphenation{Corollary}
\hyphenation{Proof}
\hyphenation{Remark}

\def\bcontinued{({\it continued\/})}
\def\tcontinued{Continued}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Draftrules %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%% To print grid lines on all pages
\newdimen\pageheight\global\pageheight=\textheight%
\newcount\rulecount\rulecount=1%
%
\newdimen\leftcolrulepos
\newdimen\rightcolrulepos
%
\edef\slugtoday{\two@digits{\the\day}/\two@digits{\the\month}/\the\year}%
%
\def\PrintGridLines{%
{\color{black!10}%
    {%
    \loop%
    \ifdim\pageheight>0pt%
        \ifnum\rulecount=1%
            \advance\pageheight by -1.5pt%
        \fi%
        \AtTextUpperLeft{%x
          \put(0,\LenToUnit{-\pageheight}){%
            \line(1,0){\LenToUnit{\leftcolrulepos}}}}%
%%14Mar16%%
        \AtTextUpperLeft{%
        \put(\LenToUnit{\rightcolrulepos},\LenToUnit{-\pageheight}){%
           \line(1,0){\LenToUnit{\leftcolrulepos}}}}%
        \advance\pageheight-11.5pt%baseline
        \advance\rulecount\@ne%
    \repeat%
}}}%
%
\RequirePackage{showframe}
\if@draftruleson%
%
\renewcommand\ShowFramePicture{%
\leftcolrulepos\columnwidth%
\rightcolrulepos\columnwidth%
\advance\rightcolrulepos by \columnsep%
  \begingroup
    \normalcolor\thinlines%
    \put(0,0){
%    \if@watermarkon\AtTextUpperLeft{%
%      \put(\LenToUnit{\textwidth},41){\llap{\fontsize{8}{10}\selectfont {\rm JrnlID\ \@JrnlID\_ArtID \@artid\_Proof\#1 - \slugtoday}}}}\fi%
    \AtTextLowerLeft{%
      \framebox(\LenToUnit{\textwidth},\LenToUnit{\textheight}){}}%
      \linethickness{.1pt}%
      \PrintGridLines%
    \AtTextLowerLeft{%
      \put(0,\LenToUnit{-\footskip}){%
        \line(1,0){\LenToUnit{\textwidth}}}}%
        \AtTextLowerLeft{%
          \put(\LenToUnit{\columnwidth},0){%
            \line(0,1){\LenToUnit{\textheight}}}}%
            %%For marginpar
%%14Mar16%%
        \AtTextLowerLeft{%
          \put(\LenToUnit{\rightcolrulepos},0){%
            \line(0,1){\LenToUnit{\textheight}}}}%
    \AtTextLowerLeft{%
      \@tempdima=\textwidth\advance\@tempdima\marginparsep%
      \if@twoside%
        \ifodd\c@page
          \if@mparswitch
            \@tempdima=-\marginparsep\advance\@tempdima-\marginparwidth%
          \fi
        \else%
          \@mparswitchfalse
          \if@mparswitch
            \@tempdima=-\marginparsep\advance\@tempdima-\marginparwidth%
          \fi
        \fi%
      \fi%
    }}%
  \endgroup
}%
\else
\renewcommand\ShowFramePicture{%
\leftcolrulepos\columnwidth%
\rightcolrulepos\columnwidth%
\advance\rightcolrulepos by \columnsep%
  \begingroup
    \normalcolor\thinlines%
    \put(0,0){
%    \if@watermarkon\AtTextUpperLeft{%
%      \put(\LenToUnit{\textwidth},41){\llap{\fontsize{8}{10}\selectfont {\rm JrnlID\ \@JrnlID\_ArtID \@artid\_Proof\#1 - \slugtoday}}}}\fi%
    }%
  \endgroup
}%
\fi%


\newdimen\p@renwd

\def\spbordermatrix#1{\begingroup \m@th
  \setbox\z@\vbox{\def\cr{\crcr\noalign{\kern2\p@\global\let\cr\endline}}%
    \ialign{$##$\hfil\kern2\p@\kern\p@renwd&\thinspace\hfil$##$\hfil
      &&\quad\hfil$##$\hfil\crcr
      \omit\strut\hfil\crcr\noalign{\kern-\baselineskip}%
      #1\crcr\omit\strut\cr}}%
  \setbox\tw@\vbox{\unvcopy\z@\global\setbox\@ne\lastbox}%
  \setbox\tw@\hbox{\unhbox\@ne\unskip\global\setbox\@ne\lastbox}%
  \setbox\tw@\hbox{$\kern\wd\@ne\kern-\p@renwd\left[\kern-\wd\@ne
    \global\setbox\@ne\vbox{\box\@ne\kern2\p@}%
    \vcenter{\kern-\ht\@ne\unvbox\z@\kern-\baselineskip}\,\hskip-\bmskip\right]$}%
  \null\;\vbox{\kern\ht\@ne\box\tw@}\endgroup}


\def\sqbordermatrix#1{\begingroup \m@th
  \setbox\z@\vbox{\def\cr{\crcr\noalign{\kern2\p@\global\let\cr\endline}}%
    \ialign{$##$\hfil\kern2\p@\kern\p@renwd&\thinspace\hfil$##$\hfil
      &&\quad\hfil$##$\hfil\crcr
      \omit\strut\hfil\crcr\noalign{\kern-\baselineskip}%
      #1\crcr\omit\strut\cr}}%
  \setbox\tw@\vbox{\unvcopy\z@\global\setbox\@ne\lastbox}%
  \setbox\tw@\hbox{\unhbox\@ne\unskip\global\setbox\@ne\lastbox}%
  \setbox\tw@\hbox{$\kern\wd\@ne\kern-\p@renwd\left[\kern-\wd\@ne
    \global\setbox\@ne\vbox{\box\@ne\kern2\p@}%
    \vcenter{\kern-\ht\@ne\unvbox\z@\kern-\baselineskip}\,\right]$}%
  \null\;\vbox{\kern\ht\@ne\box\tw@}\endgroup}

\def\llbordermatrix#1{\begingroup \m@th
  \setbox\z@\vbox{\def\cr{\crcr\noalign{\kern2\p@\global\let\cr\endline}}%
    \ialign{$##$\hfil\kern2\p@\kern\p@renwd&\thinspace\hfil$##$\hfil
      &&\quad\hfil$##$\hfil\crcr
      \omit\strut\hfil\crcr\noalign{\kern-\baselineskip}%
      #1\crcr\omit\strut\cr}}%
  \setbox\tw@\vbox{\unvcopy\z@\global\setbox\@ne\lastbox}%
  \setbox\tw@\hbox{\unhbox\@ne\unskip\global\setbox\@ne\lastbox}%
  \setbox\tw@\hbox{$\kern\wd\@ne\kern-\p@renwd\left[\kern-\wd\@ne
    \global\setbox\@ne\vbox{\box\@ne\kern2\p@}%
    \vcenter{\kern-\ht\@ne\unvbox\z@\kern-\baselineskip}\,\right.$}%
  \null\;\vbox{\kern\ht\@ne\box\tw@}\endgroup}

\def\lbordermatrix#1{\begingroup \m@th
  \setbox\z@\vbox{\def\cr{\crcr\noalign{\kern2\p@\global\let\cr\endline}}%
    \ialign{$##$\hfil\kern2\p@\kern\p@renwd&\thinspace\hfil$##$\hfil
      &&\quad\hfil$##$\hfil\crcr
      \omit\strut\hfil\crcr\noalign{\kern-\baselineskip}%
      #1\crcr\omit\strut\cr}}%
  \setbox\tw@\vbox{\unvcopy\z@\global\setbox\@ne\lastbox}%
  \setbox\tw@\hbox{\unhbox\@ne\unskip\global\setbox\@ne\lastbox}%
  \setbox\tw@\hbox{$\left[\kern\wd\@ne\kern-\p@renwd\kern-\wd\@ne
    \global\setbox\@ne\vbox{\box\@ne\kern2\p@}%
    \vcenter{\kern-\ht\@ne\unvbox\z@\kern-\baselineskip}\,\right.$}%
  \null\;\vbox{\kern\ht\@ne\box\tw@}\endgroup}

\newdimen\bmskip
\bmskip=0pt

\def\rbordermatrix#1{\begingroup \m@th
  \setbox\z@\vbox{\def\cr{\crcr\noalign{\kern2\p@\global\let\cr\endline}}%
    \ialign{\hfil$##$\hfil\kern6\p@\kern\p@renwd&\thinspace\hfil$##$\hfil
      &&\quad\hfil$##$\hfil\crcr
      \omit\strut\hfil\crcr\noalign{\kern-\baselineskip}%
      #1\crcr\omit\strut\cr}}%
  \setbox\tw@\vbox{\unvcopy\z@\global\setbox\@ne\lastbox}%
  \setbox\tw@\hbox{\unhbox\@ne\unskip\global\setbox\@ne\lastbox}%
  \setbox\tw@\hbox{$\left.\kern\wd\@ne\kern-\p@renwd\kern-\wd\@ne
    \global\setbox\@ne\vbox{\box\@ne\kern2\p@}
    \vcenter{\kern-\ht\@ne\unvbox\z@\kern-\baselineskip}\hskip-\bmskip\right]$}%
  \null\;\vbox{\kern\ht\@ne\box\tw@}\endgroup}

\chardef\permil="89%

\let\euro\texteuro

\definecolor{mag}{cmyk}{0,.36,0,0}

\newenvironment{wrapfig}[3]{\setlength\intextsep{0pt}\footnotesize\par
\begin{wrapfigure}[#1]{l}{65pt}{\includegraphics{#2}}\end{wrapfigure}
\noindent #3\vskip2pc}


\newcommand\aubio[2]{\vspace{1\baselineskip}\noindent{\begin{wrapfig}{10}{#1}{#2}\end{wrapfig}}\vspace{.1\baselineskip}}

\def\@print@issn{xxxx-xxxx/xx}
\def\@doi@fixed@field{xx.xxxx/}
\def\@doi@variable@field{00000000000000000000}
\def\jourinf{Vol.~\vol@info, No.~\issue@info, \month@info\space \year@info, \page@extent@info}

\Year{2019}

\definecolor{shadecolor}{cmyk}{0,0,0,.10}

\newenvironment{boxtext}{\begingroup\fboxsep5pt%
\begin{shaded}\reset@font\boxtextfont\hsize=239pt%
}{\end{shaded}\endgroup}


\endinput
