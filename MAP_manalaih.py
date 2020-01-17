######################################################################
# Author: Hila Manalai
# Username: manalaih
#
# P01-Final Project: World at Your Fingertips
#
# Purpose:  To create a map of locations and provide user with the option to pin locations on the map.

######################################################################
# Acknowledgements:
#
# Original Authors: Dr. Scott Heggen and Dr. Jan Pearce

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle
import winsound


class Place:
    """ A class to manufacture Place objects."""

    def __init__(self, name, location, latitude, longitude, color="white", font="Courier"):
        """

        :param name: A string value representing user's name.
        :param location: A string value representing name of the place or country.
        :param latitude: A float value, latitude of the location.
        :param longitude: A float value, longitude of the location.
        :param color: User's color choice.
        :param font: User's chosen font style.
        """
        self.name = name
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.color = color
        self.turtle = turtle.Turtle()
        self.font = font

    def __str__(self):
        """
        Overridden string class which allows the user to use str() to print cleanly.

        :return: A formatted string
        """

        return "\n Name: {0}\n Location: {1}\n Latitude: {2}\n Longitude: {3}\n Color: {4}\n Text Font: {5}\n".format(self.name, self.location, self.latitude, self.longitude, self.color, self.font)

    def place_pin(self, window, image):
        """
        Places a pin on the map.
        :param window: The window object to place the pin.
        :param image: takes in a .gif file which will later be the shape of the pin.
        :return: None
        """
        pin = self.turtle
        pin.penup()
        pin.color(self.color)                # Set the pin to user's chosen color
        pin.shape(image)                     # Sets the pin to a user's image choice

        pin.goto((int(self.longitude) / 195) * window.window_width() / 2, (int(self.latitude) / 120) * window.window_height() / 2)  # goes on the location

        text = "{0}\n  {1}".format(self.name, self.location)   # Setting up pin label
        pin.write(text, font=(self.font, 8, "bold"))          # displays the text describing the location


def handler(x, y):
    """
    Creates a Place object and pins it on the map using x, y coordinates of mouse click for longitude and latitude
    values, and user input for Place object's parameters.
    :param x: x coordinate of mouse click
    :param y: y coordinate of mouse click
    :return: an object of the Place class.
    """

    name = input("Please enter your name:")
    location = input("HOWDY! " + name + "." + " Please write the name of the place you clicked on?")
    latitude = (y * 240) * (1/wn.window_height())
    longitude = (x * 390) * (1/wn.window_width())
    color = input("What color would you like your pin to be?")
    font = input("Which font would you like?\n [Arial, Courier, Comic Sans Ms, Fixedsys, MS Sans Serif,  MS Serif, Symbol, System, Times, Verdana]?\n")
    image = input("Which Pusheen character would you like to be your guide?\n [boss, cool, unicorn, mermaid, twilightsparkle, flying, sleeping, wizard]?\n Or do you prefer [spacecraft or airplane]?\n For Middle Earth [gandalf, gollum, evangeline, legolas, smaug, pin].")
    while not is_valid_pic(image):
        image = input("Invalid input. Please choose again.\n [boss, cool, unicorn, mermaid, twilightsparkle, flying, sleeping, wizard]?\n Or do you prefer [spacecraft or airplane]?\n For Middle Earth [gandalf, gollum, evangeline, legolas, smaug, pin].")
    image = image+".gif"      # automatically places a .gif after image name.
    new_object = Place(name, location, latitude, longitude, color, font)  # create new Place object using input values.
    print(str(new_object))     # Print the new object using the defined str method.
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # Play sound when object is created and placed on the map.
    new_object.place_pin(wn, image)  # Place the newly created Place object on the map with the image-pin.
    return new_object


def parse_file():
    """
    Iterates through the file, and creates the list of places

    :return: a list of Place objects representing multiple places
    """

    file_content = open("places.txt", 'r')           # Opens file for reading

    str_num = file_content.readline()           # The first line of the file, which is the number of entries in the file
    str_num = int(str_num[:-1])                 # The '/n' character needs to be removed

    places_list = []
    for i in range(str_num):
        places_list.append(extract_place(file_content))        # Assembles the list of places

    file_content.close()

    return places_list


def extract_place(file_content):
    """
    This function extracts five lines out of file_content,
    which is a variable holding all of the file content from the calling function. Each extracted line represents,
    in order, the place's name, location, latitude, longitude, and user color. The function returns the five elements
    to the function call as a Place object.

    :param file_content: contents of the file which represents all places
    :return: a Place object representing a single place.
    """
    name = file_content.readline().strip()
    location = file_content.readline().strip()
    latitude = file_content.readline().strip()
    longtitude = file_content.readline().strip()
    user_color = file_content.readline().strip()

    new_object = Place(name, location, float(latitude), float(longtitude), user_color)  # Create a Place object using file content.
    new_object.place_pin(wn, "wizard.gif")  # Pin the Place object on the map and use wizard.gif for pin image.
    return new_object


def close():
    """
    A function that closes the window object.
    :return:None
    """
    wn.bye()


def reset():
    """
    A function to reset the window object to its original state.
    :return:None
    """
    wn.reset()


def is_valid_pic(image):
    """
    Checks if the user is typing the correct image name.
    :param image: string value representing names of images
    :return: True if image is in the list of images
             False if image is not in the list of images
    """
    if image in ["boss", "cool", "unicorn", "mermaid", "twilightsparkle", "spacecraft", "airplane", "gandalf", "gollum", "evangeline", "legolas", "smaug", "pin", "flying", "wizard", "sleeping"]:
        return True
    return False



def main():
    """
    This program is designed to place pins on a world map.
    Each place is represented as a Place object.
    Each place is then pinned to the map.

    :return: None
    """
    global wn

    inpt = input("Which world do you wanna go to? [earth] / [middle earth]")
    wn = turtle.Screen()
    for i in ["boss.gif", "cool.gif", "unicorn.gif", "mermaid.gif", "twilightsparkle.gif", "spacecraft.gif", "airplane.gif", "gandalf.gif", "gollum.gif", "evangeline.gif", "legolas.gif", "smaug.gif", "pin.gif", "flying.gif", "sleeping.gif", "wizard.gif"]:
        wn.addshape(i)   # add all the images to the screen for later use
    wn.setup(width=1100, height=650, startx=0, starty=0)
    wn.title("World at Your Fingertips!")
    if inpt == "earth":
        # set up the world map
        wn.bgpic("world-map-color.gif")
        parse_file()  # Generates places from the file: places.txt, and pins them on the map.
        print("Map created!")
    elif inpt == "middle earth":
        wn.bgpic("middle-earth.gif")

    else:
        wn.bgcolor("white")
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.write("Invalid input. Try again. \nThere might be a typo.", align="center", font=("courier", 20, "normal"))

    wn.onclick(handler)
    wn.onkey(close, "q")  # binds the close function (event handler) to the q key.
    wn.onkey(reset, "r")  # binds the reset function (event handler) to the r key.
    wn.listen()           # listen for events.
    wn.mainloop()


if __name__ == "__main__":
    main()
