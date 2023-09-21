import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        valid_extensions = ['.jpg', '.jpeg', '.png']
        input_ = os.path.splitext(sys.argv[1])
        output_ = os.path.splitext(sys.argv[2])

        if input_[1] not in valid_extensions:
            sys.exit("Invalid input")
        elif input_[1] != output_[1]:
            sys.exit("Input and output have different extensions")
        elif not os.path.exists(sys.argv[1]):
            sys.exit("Input does not exist")
        else:
            shirt = Image.open("shirt.png")
            with Image.open(sys.argv[1]) as img:
                input_edited = ImageOps.fit(img, shirt.size)
                input_edited.paste(shirt, mask = shirt)
                input_edited.save(sys.argv[2])


if __name__ == "__main__":
    main()