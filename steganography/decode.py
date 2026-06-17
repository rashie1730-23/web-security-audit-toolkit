from PIL import Image


def decode_message(
    image_path
):

    img = Image.open(
        image_path
    ).convert("RGB")

    pixels = img.load()

    width, height = img.size

    binary_data = ""

    for y in range(height):

        for x in range(width):

            r, g, b = pixels[x, y]

            binary_data += str(
                r & 1
            )

    chars = []

    for i in range(
        0,
        len(binary_data),
        8
    ):

        byte = binary_data[
            i:i + 8
        ]

        if len(byte) < 8:
            break

        chars.append(
            chr(
                int(byte, 2)
            )
        )

    message = ''.join(chars)

    return message.split(
        '\ufffe'
    )[0]