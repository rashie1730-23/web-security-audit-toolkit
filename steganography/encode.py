from PIL import Image


def encode_message(
    image_path,
    message,
    output_path
):

    img = Image.open(
        image_path
    ).convert("RGB")

    pixels = img.load()

    binary_message = ''.join(
        format(ord(char), '08b')
        for char in message
    )

    binary_message += "1111111111111110"

    data_index = 0

    width, height = img.size

    for y in range(height):

        for x in range(width):

            if data_index >= len(binary_message):
                break

            r, g, b = pixels[x, y]

            r = (
                r & ~1
            ) | int(
                binary_message[data_index]
            )

            data_index += 1

            pixels[x, y] = (
                r,
                g,
                b
            )

        if data_index >= len(binary_message):
            break

    img.save(
        output_path
    )

    return output_path