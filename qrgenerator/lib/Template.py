from itertools import repeat
import os

header = """
\\documentclass[a4paper,10pt]{article}
\\usepackage{graphicx}
\\usepackage{xcolor}
%--------------------------
\\usepackage[newdimens]{labels}
\\LabelGridtrue
\\LabelInfotrue
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
    \\includegraphics[height=1.8cm]{{./""" + root_dir + os.sep + str(d[3]) + """}.png}
    \\rotatebox{90}{
      \\footnotesize{""" + d[1] + """\\hfill\\break """ + d[3].replace(d[1], '') + """}
    }
  }"""

    return header + labels + footer
