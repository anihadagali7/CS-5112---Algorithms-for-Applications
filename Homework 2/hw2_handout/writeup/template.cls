\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{template}

\LoadClass[12pt]{article}
\RequirePackage{hw}

\AtBeginDocument{
    \fbox{
        \parbox{\courseheader}{
        CS 5112 Fall 2025\hfill HW\hwnum: {\it \title}  \\
        Name: \name \hfill \textbf{Due: \duedate}\\
        NetID: \netid \\
        Collaborators: \collaborators
        }
    }
    \vspace{5pt}
}

\NewEnviron{solution}[1][80pt]{
    \vspace{10pt} \textcolor{blue}{Answer: \BODY} \vspace{10pt}
}

% Challenge:
\newcommand{\challenge}{
    \newpage

    \fbox{
        \parbox{\courseheader}{
        CS 5112 Fall 2025\hfill HW\hwnum: Challenge Problem  \\
        Name: \name \hfill \textbf{Due: \duedate}\\
        NetID: \netid \\
        Collaborators: \collaborators
        }
    }
    \vspace{5pt}
}
