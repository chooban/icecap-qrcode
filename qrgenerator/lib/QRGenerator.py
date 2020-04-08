import qrcode


def generate(input_tuple, filename):
    elements = list(input_tuple)
    data_to_encode = "|".join(elements)
    # print('Generating barcode for', data_to_encode)
    # print('Saving to', filename)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=0
    )
    qr.add_data(data_to_encode)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)

    return True
