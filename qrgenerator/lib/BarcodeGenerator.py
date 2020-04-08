from barcode import Code39
from barcode.writer import ImageWriter


def generate(input_tuple, filename):
    elements = list(input_tuple)
    data_to_encode = "-".join(elements)
    data_to_encode = data_to_encode.replace('_', '-')
    print('Generating barcode for', data_to_encode)
    print('Saving to', filename)

    with open(filename, 'wb') as fh:
        Code39(data_to_encode, writer=ImageWriter()).write(fh)
