import os

header = """
\\documentclass[10pt]{article}
\\usepackage[papersize={8.5in,11in}]{geometry}
\\usepackage{graphicx}
\\usepackage{xcolor}
\\usepackage[breakwords]{truncate}
%--------------------------
\\usepackage[newdimens]{labels}
%\\LabelGridtrue
%\\LabelInfotrue
\\LabelCols=5%             Number of columns of labels per page
\\LabelRows=12%             Number of rows of labels per page

\\LeftPageMargin=4mm%      These four parameters give the
\\RightPageMargin=4mm%       page gutter sizes.  The outer edges of
\\TopPageMargin=12mm%        the outer labels are the specified
\\BottomPageMargin=32mm%     distances from the edge of the paper.
\\InterLabelColumn=2mm%    Gap between columns of labels
\\InterLabelRow=0mm%       Gap between rows of labels

\\LeftLabelBorder=3mm%     These four parameters give the extra
\\RightLabelBorder=0mm%      space used around the text on each
\\TopLabelBorder=4mm%        actual label.
\\BottomLabelBorder=0mm%
\\setlength{\\arrayrulewidth}{1mm}

%--------------------------
\\begin{document}
\\sf
"""

footer = """
\\end{document}\n
"""


def create_sheet(data, root_dir):
    labels = '\t'
    for d in data:
        labels += """
  \\boxedaddresslabel[\\fboxrule=0pt]{%
    \\includegraphics[width=1.5cm]{{./""" + root_dir + os.sep + str(d[1]) + """}.png}
    \\
    \\rotatebox{90} {
      \\footnotesize{""" + d[0] + """}
      \\hspace{5mm}
    }
    \\footnotesize{""" + d[1].replace('_', '\\_') + """}
    \\vspace{4mm}
  }"""

    return header + labels + footer
