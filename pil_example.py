from PIL import Image


def main():
    # Load the image
    im = Image.open('img/watermelon-cat.jpg')

    # Take a look at Pillow docs to learn how to work with Images
    # docs: https://pillow.readthedocs.io/en/stable/reference/Image.html
    im = im.convert('1')

    # We can also rotate the image
    im = im.rotate(-90)

    im.show()


if __name__ == "__main__":
    main()
