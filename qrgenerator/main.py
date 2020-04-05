import sys
import getopt
from lib.SheetReader import read as read_sheet
from lib.QRGenerator import generate as generate_qrcode

def main(argv):
    inputfile = ''
    outputfile = ''
    startrow = 3
    columns = [0,1,5,6]
    try:
        opts, args = getopt.getopt(argv, "hi:o:c:r:", ["ifile=", "ofile=", "columns=", "startrow="])
    except getopt.GetoptError:
        print("qrgenerator.py -i <inputfile> -o <outputfile>")
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print("qrgenerator.py -i <inputfile> -o <outputfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in("-c", "--columns"):
            print("Not supported yet")
            sys.exit(1)
        elif opt in("-r", "--startrow"):
            startrow = int(arg)

    rows = read_sheet(inputfile, startrow, columns)
    image = generate_qrcode(rows[0])

    image.save("testfile.svg")

if __name__ == "__main__":
    main(sys.argv[1:])
