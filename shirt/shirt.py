import sys
from os.path import splitext
from PIL import Image, ImageOps


#main code
def main():
    check_command_line()
    try:
        image_file = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    fshirt = Image.open("shirt.png")
    size = fshirt.size
    puppet = ImageOps.fit(image_file, size)
    puppet.paste(fshirt, fshirt)
    puppet.save(sys.argv[2])


#cheking again
def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if check_file(file1[1]) == False:
        sys.exit("Invalid input")

    if check_file(file2[1]) == False:
        sys.exit("Invalid output")
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")


def check_file(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()
