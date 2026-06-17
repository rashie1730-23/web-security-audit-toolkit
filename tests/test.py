import os

BASE_DIR = os.path.dirname(__file__)
from steganography.encode import encode_message
from steganography.decode import decode_message
input_image = os.path.join(
    BASE_DIR,
    "input.png"
)

output_image = os.path.join(
    BASE_DIR,
    "output.png"
)

encode_message(
    input_image,
    "Cloud Counselage Internship Program",
    output_image
)

message = decode_message(
    output_image
)

print(message)