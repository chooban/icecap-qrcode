import qrcode
import qrcode.image.svg

def generate(input_tuple):
    elements = list(input_tuple)
    data_to_encode = "|".join(elements)
    print('Generating barcode for', data_to_encode)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data_to_encode)

    img = qr.make_image(qrcode.image.svg.SvgPathFillImage, fill_color="black", back_color="white")

    return img
