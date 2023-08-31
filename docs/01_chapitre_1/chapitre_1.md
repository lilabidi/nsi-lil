---
author: Votre nom
title: Chapitre 1
---

## I. Paragraphe 1 :

texte 1

### 1. Sous paragraphe 1

Texte 1.1

### 2. Sous paragraphe 2

Texte 1.2

## II. Paragraphe 2 :

texte 1

### 1. Sous paragraphe 1

Texte 2.1

### 2. Sous paragraphe 2

Texte 2.2


Si $x_1, x_2, \ldots, x_p$ désignent les $p$ modalités du caractère d'une série statistique, et $f_1, f_2, \ldots, f_p$ désignent les fréquences correspondantes alors, $\vspace{-0.5em}$
$\overline{x}=f_1~\times~x_1~+~f_2~\times~x_2+~f_3~\times~x_3~+~\cdots~+~f_p~\times~x_p$


$$\begin{preuve}
Posons $N=n_1~+~n_2~+~n_3~+~\ldots~+~n_p

\renewcommand{\arraystretch}{1.5}\begin{array}{rcl}

 \overline{x}&=&\dfrac{\TopStrut n_1~\times~x_1~+~n_2~\times~x_2~+~n_3~\times~x_3~+~\cdots~+~n_p~\times~x_p}{\BotStrut n_1~+~n_2~+~n_3~+~\cdots~+~n_p}\\
 \overline{x}&=&\dfrac{n_1~\times~x_1}{N}~+~\dfrac{n_2~\times~x_2}{N}~+~\dfrac{n_3~\times~x_3}{N}~+~\cdots~+~\dfrac{n_p~\times~x_p}{N}
\\
 \overline{x}&=&f_1~\times~x_1~+~f_2~\times~x_2~+~f_3~\times~x_3~+~\cdots~+~f_p~\times~x_p
  \end{array}\renewcommand{\arraystretch}{1}$
\end{preuve}$$


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Welcome to Overleaf --- just edit your LaTeX on the left,
% and we'll compile it for you on the right. If you open the
% 'Share' menu, you can invite other users to edit at the same
% time. See www.overleaf.com/learn for more info. Enjoy!
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Document généré avec MathALEA sous licence CC-BY-SA
%
% https://coopmaths.fr/mathalea.html?ex=2N20-1,s=3-3-3,s2=8-10-12,s3=12,n=3,i=0&serie=JyO4&v=latex&z=1
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
\documentclass[12pt,svgnames]{article}
\usepackage[left=1.5cm,right=1.5cm,top=4cm,bottom=2cm]{geometry}
%\usepackage[utf8]{inputenc}        
%\usepackage[T1]{fontenc}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% EXIT WARNING DÛ À LA COMPILATION XETEX %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{ifxetex}

\ifxetex
  \usepackage{fontspec}
\else
  \usepackage[T1]{fontenc}
  \usepackage[utf8]{inputenc}
  \usepackage{lmodern}
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage[french]{babel}
\usepackage{hyperref}
\usepackage{multicol} 
\usepackage{calc} 
\usepackage{enumerate}
\usepackage{enumitem}
\usepackage{graphicx}
\usepackage{tabularx}
%\usepackage[autolanguage]{numprint}
\usepackage[autolanguage,np]{numprint}
\usepackage{amsmath,amsfonts,amssymb,mathrsfs} 
\usepackage{cancel}
\usepackage{textcomp}
\usepackage{gensymb}
\usepackage{eurosym}
%\DeclareUnicodeCharacter{20AC}{\euro{}} %Incompatible avec XeLaTeX
\usepackage{fancyhdr,lastpage}          
\pagestyle{fancy}                      
\usepackage{fancybox}
\usepackage{setspace}
\usepackage{xcolor}
\usepackage{pgf,tikz} % Pour les images et figures gÃ©omÃ©triques
\usetikzlibrary{babel,arrows,calc,fit,patterns,plotmarks,shapes.geometric,shapes.misc,shapes.symbols,shapes.arrows,
shapes.callouts, shapes.multipart, shapes.gates.logic.US,shapes.gates.logic.IEC, er, automata,backgrounds,chains,topaths,trees,petri,mindmap,matrix, calendar, folding,fadings,through,positioning,scopes,decorations.fractals,decorations.shapes,decorations.text,decorations.pathmorphing,decorations.pathreplacing,decorations.footprints,decorations.markings,shadows}

\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancyhead[L]{}
\fancyhead[R]{}

%%% COULEURS %%%

\definecolor{nombres}{cmyk}{0,.8,.95,0}
\definecolor{gestion}{cmyk}{.75,1,.11,.12}
\definecolor{gestionbis}{cmyk}{.75,1,.11,.12}
\definecolor{grandeurs}{cmyk}{.02,.44,1,0}
\definecolor{geo}{cmyk}{.62,.1,0,0}
\definecolor{algo}{cmyk}{.69,.02,.36,0}
\definecolor{correction}{cmyk}{.63,.23,.93,.06}
\usepackage{colortbl}
\arrayrulecolor{couleur_theme} % Couleur des filets des tableaux

%%% MISE EN PAGE %%%

\setlength{\parindent}{0mm}
\renewcommand{\arraystretch}{1.5}
\renewcommand{\labelenumi}{\textbf{\theenumi{}.}}
\renewcommand{\labelenumii}{\textbf{\theenumii{}.}}
\setlength{\fboxsep}{3mm}

\setlength{\headheight}{14.5pt}

\spaceskip=2\fontdimen2\font plus 3\fontdimen3\font minus3\fontdimen4\font\relax %Pour doubler l'espace entre les mots
\newcommand{\numb}[1]{ % Dessin autour du numéro d'exercice
\begin{tikzpicture}[overlay,yshift=-.3cm,scale=.8]
\draw[fill=couleur_numerotation,couleur_numerotation](-.3,0)rectangle(.5,.8);
\draw[line width=.05cm,couleur_numerotation,fill=white] (0,0)--(.5,.5)--(1,0)--(.5,-.5)--cycle;
\node[couleur_numerotation]  at (.5,0) { \large \bfseries #1};
\draw (-.4,.8) node[white,anchor=north west]{\bfseries EX}; 
\end{tikzpicture}
}

%%% NUMEROS DES EXERCICES %%%

\usepackage{titlesec} % Le titre de section est un numéro d'exercice avec sa consigne alignée à gauche.
\titleformat{\section}{}{\numb{\arabic{section}}}{1cm}{\hspace{0em}}{}
\newcommand{\exo}[1]{ % Un exercice est une nouvelle section avec la consigne écrite en caractêres normaux
  \section{\textmd{#1}}
  \medskip
}


%%% ENVIRONNEMENTS - CADRES %%%
\usepackage[framemethod=tikz]{mdframed}

\newmdenv[linecolor=couleur_theme, linewidth=3pt,topline=true,rightline=false,bottomline=false,frametitlerule=false,frametitlefont={\color{couleur_theme}\bfseries},frametitlerulewidth=1pt]{methode}


\newmdenv[startcode={\setlength{\multicolsep}{0cm}\setlength{\columnsep}{.2cm}\setlength{\columnseprule}{0pt}\vspace{0cm}},linecolor=white, linewidth=3pt,innerbottommargin=10pt,innertopmargin=5pt,innerrightmargin=20pt,splittopskip=20pt,splitbottomskip=10pt,everyline=true,tikzsetting={draw=couleur_theme,line width=4pt,dashed,dash pattern= on 10pt off 10pt},frametitleaboveskip=-.6cm,frametitle={\tikz\node[anchor= east,rectangle,fill=white]{\textcolor{couleur_theme}{\raisebox{-.3\height}{}\; \bfseries \Large Objectifs}};}]{objectif}

\newmdenv[startcode={\colorlet{couleur_numerotation}{correction}\renewcommand{\columnseprulecolor}{\color{correction}}
\setcounter{section}{0}\arrayrulecolor{correction}},linecolor=white, linewidth=4pt,innerbottommargin=10pt,innertopmargin=5pt,splittopskip=20pt,splitbottomskip=10pt,everyline=true,frametitle=correction,tikzsetting={draw=correction,line width=3pt,dashed,dash pattern= on 15pt off 10pt},frametitleaboveskip=-.4cm,frametitle={\tikz\node[anchor= east,rectangle,fill=white]{\; \textcolor{correction}{\raisebox{-.3\height}{}\; \bfseries \Large Corrections}};}]{correction}

\newmdenv[roundcorner=0,linewidth=0pt,frametitlerule=false, backgroundcolor=gray!40,leftmargin=8cm]{remarque}

% echelle pour le dé
\def \globalscale {0.04}
% abscisse initiale pour les chevrons
\def \xini {3}

\newcommand{\theme}[4]
{
  %\theme{nombres|gestion|grandeurs|geo|algo}{Texte (entrainement, évaluation, mise en route...}{numéro de version ou vide}{titre du thême et niveau}
  \fancyhead[C]{
    %Tracé du dé
    \begin{tikzpicture}[y=0.80pt, x=0.80pt, yscale=-\globalscale, xscale=\globalscale,remember picture, overlay, shift={(current page.north west)},xshift=17cm,yshift=9.5cm,fill=couleur_theme]
      %%%%Arc supérieur gauche%%%%
      \path[fill](523,1424)..controls(474,1413)and(404,1372)..(362,1333)..controls(322,1295)and(313,1272)..(331,1254)..controls(348,1236)and(369,1245)..(410,1283)..controls(458,1328)and(517,1356)..(575,1362)..controls(635,1368)and(646,1375)..(643,1404)..controls(641,1428)and(641,1428)..(596,1430)..controls(571,1431)and(538,1428)..(523,1424)--cycle;
      %%%%Dé face supérieur%%%%
      \path[fill](512,1272)..controls(490,1260)and(195,878)..(195,861)..controls(195,854)and(198,846)..(202,843)..controls(210,838)and(677,772)..(707,772)..controls(720,772)and(737,781)..(753,796)..controls(792,833)and(1057,1179)..(1057,1193)..controls(1057,1200)and(1053,1209)..(1048,1212)..controls(1038,1220)and(590,1283)..(551,1282)..controls(539,1282)and(521,1278)..(512,1272)--cycle;
      %%%%Dé faces gauche et droite%%%%
      \path[fill](1061,1167)..controls(1050,1158)and(978,1068)..(900,967)..controls(792,829)and(756,777)..(753,756)--(748,729)--(724,745)..controls(704,759)and(660,767)..(456,794)..controls(322,813)and(207,825)..(200,822)..controls(193,820)and(187,812)..(187,804)..controls(188,797)and(229,688)..(279,563)..controls(349,390)and(376,331)..(391,320)..controls(406,309)and(462,299)..(649,273)..controls(780,254)and(897,240)..(907,241)..controls(918,243)and(927,249)..(928,256)..controls(930,264)and(912,315)..(889,372)..controls(866,429)and(848,476)..(849,477)..controls(851,479)and(872,432)..(897,373)..controls(936,276)and(942,266)..(960,266)..controls(975,266)and(999,292)..(1089,408)..controls(1281,654)and(1290,666)..(1290,691)..controls(1290,720)and(1104,1175)..(1090,1180)..controls(1085,1182)and (1071,1176)..(1061,1167)--cycle;
      %%%%Arc inférieur bas%%%%
      \path[fill](1329,861)..controls(1316,848)and(1317,844)..(1339,788)..controls(1364,726)and(1367,654)..(1347,591)..controls(1330,539)and(1338,522)..(1375,526)..controls(1395,528)and(1400,533)..(1412,566)..controls(1432,624)and(1426,760)..(1401,821)..controls(1386,861)and(1380,866)..(1361,868)..controls(1348,870)and(1334,866)..(1329,861)--cycle;
      %%%%Arc inférieur gauche%%%%
      \path[fill](196,373)..controls(181,358)and(186,335)..(213,294)..controls(252,237)and(304,190)..(363,161)..controls(435,124)and(472,127)..(472,170)..controls(472,183)and(462,192)..(414,213)..controls(350,243)and(303,283)..(264,343)..controls(239,383)and(216,393)..(196,373)--cycle;
    \end{tikzpicture}
    \begin{tikzpicture}[remember picture,overlay]
      \node[anchor=north east,inner sep=0pt] at ($(current page.north east)+(0,-.8cm)$) {};
      \node[anchor=east, fill=white] at ($(current page.north east)+(-18.8,-2.3cm)$) {\footnotesize \bfseries{MathALEA}};
      \end{tikzpicture}
    \begin{tikzpicture}[line cap=round,line join=round,remember picture, overlay, shift={(current page.north west)},yshift=-8.5cm]
      \fill[fill=couleur_theme] (0,5) rectangle (21,6);
      \fill[fill=couleur_theme] (\xini,6)--(\xini+1.5,6)--(\xini+2.5,7)--(\xini+1.5,8)--(\xini,8)--(\xini+1,7)-- cycle;
      \fill[fill=couleur_theme] (\xini+2,6)--(\xini+2.5,6)--(\xini+3.5,7)--(\xini+2.5,8)--(\xini+2,8)--(\xini+3,7)-- cycle;  
      \fill[fill=couleur_theme] (\xini+3,6)--(\xini+3.5,6)--(\xini+4.5,7)--(\xini+3.5,8)--(\xini+3,8)--(\xini+4,7)-- cycle;   
      \node[color=white] at (10.5,5.5) {\LARGE \bfseries{ \MakeUppercase{ #4}}};
    \end{tikzpicture}
    \begin{tikzpicture}[remember picture,overlay]
      \node[anchor=north east,inner sep=0pt] at ($(current page.north east)+(0,-.8cm)$) {};
      \node[anchor=east, fill=white] at ($(current page.north east)+(-2,-1.5cm)$) {\Huge \textcolor{couleur_theme}{\bfseries{\#}} \bfseries{#2} \textcolor{couleur_theme}{\bfseries \MakeUppercase{#3}}};
    \end{tikzpicture}
  }
  \fancyfoot[R]{
    %\scriptsize Coopmaths.fr -- CC-BY-SA
    \begin{tikzpicture}[remember picture,overlay]
        \node[anchor=south east] at ($(current page.south east)+(-2,0.25cm)$) {\scriptsize {\bfseries \href{https://coopmaths.fr/}{Coopmaths.fr} -- \href{http://creativecommons.fr/licences/}{CC-BY-SA}}};
      \end{tikzpicture}
    \begin{tikzpicture}[line cap=round,line join=round,remember picture, overlay,xscale=0.5,yscale=0.5, shift={(current page.south west)},xshift=35.7cm,yshift=-6cm]
      \fill[fill=couleur_theme] (\xini,6)--(\xini+1.5,6)--(\xini+2.5,7)--(\xini+1.5,8)--(\xini,8)--(\xini+1,7)-- cycle;
      \fill[fill=couleur_theme] (\xini+2,6)--(\xini+2.5,6)--(\xini+3.5,7)--(\xini+2.5,8)--(\xini+2,8)--(\xini+3,7)-- cycle;  
      \fill[fill=couleur_theme] (\xini+3,6)--(\xini+3.5,6)--(\xini+4.5,7)--(\xini+3.5,8)--(\xini+3,8)--(\xini+4,7)-- cycle;  
    \end{tikzpicture}
  }
  \fancyfoot[C]{}
  \colorlet{couleur_theme}{#1}
  \colorlet{couleur_numerotation}{couleur_theme}
  \def\iconeobjectif{icone-objectif-#1}
  \def\urliconeomethode{icone-methode-#1}
}

\newcommand{\version}[1]{
  \fancyhead[R]{
    \begin{tikzpicture}[remember picture,overlay]
    \node[anchor=north east,inner sep=0pt] at ($(current page.north east)+(-.5,-.5cm)$) {\large \textcolor{couleur_theme}{\bfseries V#1}};
    \end{tikzpicture}
  }
}

\newcommand\dotfills[1][4cm]{\makebox[#1]{\dotfill}}



%%%%%%%%%%%%%%%%%%%%%%%%
%%% Fin du préambule %%%
%%%%%%%%%%%%%%%%%%%%%%%%
    



\theme{nombres}{}{}{}
\begin{document}

\exo{}


\marginpar{\footnotesize 2N20-1}\begin{enumerate}
	\item Compléter le tableau suivant et faire la liste de tous les diviseurs de 273.$\medskip$\\
$\begin{array}{|c|c|c|}
\hline
\text{Facteur n°1} & \text{Facteur n°2} & \text{Produit donnant } 273 \\
\hline
1 & 273& 273 \\
\hline
\ldots & \ldots& 273 \\
\hline
7 & 39& \ldots \\
\hline
13 & \ldots& 273 \\
\hline
\end{array}
$\\
	\item Compléter le tableau suivant et faire la liste de tous les diviseurs de 162.$\medskip$\\
$\begin{array}{|c|c|c|}
\hline
\text{Facteur n°1} & \text{Facteur n°2} & \text{Produit donnant } 162 \\
\hline
\ldots & 162& \ldots \\
\hline
2 & 81& 162 \\
\hline
3 & \ldots& \ldots \\
\hline
6 & \ldots& 162 \\
\hline
9 & 18& 162 \\
\hline
\end{array}
$\\
	\item Écrire la liste de tous les diviseurs de 812.
\end{enumerate}




%%%%%%%%%%%%%%%%%%%%%%
%%%   CORRECTION   %%%
%%%%%%%%%%%%%%%%%%%%%%

\newpage
\begin{correction}
\mdfsetup{frametitle=}\mdfsetup{tikzsetting={draw=correction,line width=3pt}}

\exo{}

\begin{enumerate}
	\item Le tableau suivant contient tous les couples de facteurs dont le produit vaut 273.$\medskip$\\
$\begin{array}{|c|c|c|}
\hline
\text{Facteur n°1} & \text{Facteur n°2} & \text{Produit donnant } 273 \\
\hline
1 & 273& 273 \\
\hline
3 & 91& 273 \\
\hline
7 & 39& 273 \\
\hline
13 & 21& 273 \\
\hline
\end{array}
$$\medskip$\\
273 a donc 8 diviseurs qui sont : 1 ; 3 ; 7 ; 13 ; 21 ; 39 ; 91 ; 273.
	\item Le tableau suivant contient tous les couples de facteurs dont le produit vaut 162.$\medskip$\\
$\begin{array}{|c|c|c|}
\hline
\text{Facteur n°1} & \text{Facteur n°2} & \text{Produit donnant } 162 \\
\hline
1 & 162& 162 \\
\hline
2 & 81& 162 \\
\hline
3 & 54& 162 \\
\hline
6 & 27& 162 \\
\hline
9 & 18& 162 \\
\hline
\end{array}
$$\medskip$\\
162 a donc 10 diviseurs qui sont : 1 ; 2 ; 3 ; 6 ; 9 ; 18 ; 27 ; 54 ; 81 ; 162.
	\item Pour trouver la liste des diviseurs de 812, on cherche tous les produits de deux facteurs qui donnent 812, en écrivant toujours le plus petit facteur en premier.\\
On vérifie si les nombres de 1 à 28 sont des diviseurs de 812 (inutile d’aller au-delà car $29 \times 29 = 841)$, on trouve alors :\\
1$\times $812 = 812\\
2$\times $406 = 812\\
4$\times $203 = 812\\
7$\times $116 = 812\\
14$\times $58 = 812\\
28$\times $29 = 812\\
Chacun des facteurs de la liste ci-dessus est un diviseur de 812.\\
La liste des diviseurs de 812 est donc 1 ; 2 ; 4 ; 7 ; 14 ; 28 ; 29 ; 58 ; 116 ; 203 ; 406 ; 812.
\end{enumerate}


\end{correction}

\end{document}