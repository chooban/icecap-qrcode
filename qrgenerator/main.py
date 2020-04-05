import sys
import getopt
from lib.SheetReader import read as read_sheet


def main(argv):
    inputfile = ''
    outputfile = ''
    startrow = 3
    columns = [0,5,6]
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
            startrow = arg

    rows = read_sheet(inputfile, startrow, columns)

if __name__ == "__main__":
    main(sys.argv[1:])
