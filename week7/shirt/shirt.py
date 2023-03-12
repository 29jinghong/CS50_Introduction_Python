import os
import sys
from PIL import Image, ImageOps


def main():

    # Check command-line arguments
    argc = len(sys.argv)
    argc_expected = 3

    if argc < argc_expected:
        sys.exit("Too few command-line arguments")

    if argc > argc_expected:
        sys.exit("Too many command-line arguments")

    # Get file names from command-line
    fn_before = sys.argv[1]
    fn_after = sys.argv[2]

    # Check if jpg, or png
    valid_types = (".jpg", ".png")

    if not fn_before.endswith(valid_types):
        sys.exit("Invalid input")

    if not fn_after.endswith(valid_types):
        sys.exit("Invalid output")

    # Check two files are of the same type
    useless, fn_before_ext = os.path.splitext(fn_before)
    useless, fn_after_ext = os.path.splitext(fn_after)

    if fn_before_ext != fn_after_ext:
        sys.exit("Input and output have the different extensions")

    # Open inputs
    fn_shirt = "shirt.png"

    try:
        before = Image.open(fn_before)
        shirt = Image.open(fn_shirt)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    size = shirt.size

    # Resize and crop
    before = ImageOps.fit(before, size)

    # Overlay shirt on image
    before.paste(shirt, mask=shirt)

    # Save into the after
    before.save(fn_after)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
