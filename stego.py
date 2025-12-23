import cv2
import struct

def encrypt_image(image_path, message, password, output_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found")

    data = password + "|" + message   # combine password + message
    rows, cols, _ = img.shape

    if len(data) + 4 > rows * cols:
        raise ValueError("Data too long")

    data_length = len(data)
    length_bytes = struct.pack("I", data_length)

    for i in range(4):
        img[i // cols, i % cols, 0] = length_bytes[i]

    for i, char in enumerate(data):
        img[(i + 4) // cols, (i + 4) % cols, 0] = ord(char)

    cv2.imwrite(output_path, img)
    return output_path


def decrypt_image(image_path, entered_password):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found")

    rows, cols, _ = img.shape

    length_bytes = bytearray()
    for i in range(4):
        length_bytes.append(img[i // cols, i % cols, 0])

    data_length = struct.unpack("I", length_bytes)[0]

    data = ""
    for i in range(data_length):
        data += chr(img[(i + 4) // cols, (i + 4) % cols, 0])

    stored_password, message = data.split("|", 1)

    if entered_password != stored_password:
        return None

    return message
