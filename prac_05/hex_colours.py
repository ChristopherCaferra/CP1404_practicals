""" Program to output colour codes for hexadecimal colours. """

HEX_COLOUR = {"AliceBlue": "#f0f8ff", "beige": "#f5f5dc", "black": "#000000", "BlueViolet": "#8a2be2",
              "brown": "#a52a2a", "chocolate": "#d2691e", "coral": "#ff7f50", "pink": "#ffc0cb",
              "sienna": "#a0522d", "turquoise": "#40e0d0"}


def main():
    colour = input("Enter the name of a colour: ")
    while colour != "":
        if colour in HEX_COLOUR:
            print("Colour code for {} is {}".format(colour, HEX_COLOUR[colour]))
        else:
            print("No colour by that name found")
        colour = input("Enter the name of a colour: ")


main()
