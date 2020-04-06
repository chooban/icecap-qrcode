import os
import sys
import getopt
import subprocess
from lib.SheetReader import read as read_sheet
from lib.QRGenerator import generate as generate_qrcode
from lib.Template import create_sheet


def main(argv):
    inputfile = ''
    startrow = 3
    columns = [0, 1, 5, 6]
    try:
        opts, args = getopt.getopt(
            argv,
            "hi:o:c:r:",
            ["ifile=", "columns=", "startrow="]
        )
    except getopt.GetoptError:
        print("qrgenerator.py -i <inputfile> -o <outputfile>")
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print("qrgenerator.py -i <inputfile> -o <outputfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in("-c", "--columns"):
            print("Not supported yet")
            sys.exit(1)
        elif opt in("-r", "--startrow"):
            startrow = int(arg)

    rows = read_sheet(inputfile, startrow, columns)

    # Create a <Kit ID>-<Owner ID> directory
    dir_name = rows[0][0] + '-' + rows[0][1]
    file_name = dir_name

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    for r in rows:
        code = generate_qrcode(r)
        filename = os.path.join(r[0] + '-' + r[1], r[3] + '.png')
        code.save(filename)

    tex_file = create_sheet(rows, dir_name)
    with open(os.path.join(dir_name, file_name + '.tex'), 'w') as fh:
        fh.write(tex_file)

    subprocess.call(
        ['pdflatex', os.path.join(dir_name, file_name + '.tex')]
    )
    os.unlink(file_name + '.aux')
    os.unlink(file_name + '.log')


if __name__ == "__main__":
    main(sys.argv[1:])
