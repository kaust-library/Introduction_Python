#
# Reading a INI style configuration file
#
# We explore two ways of read the values in a section:
# 1. We can read everything as 'string', and deal with the type later.
# 2. We read the values using functions for each type like booleans,
#    or integers, etc.
#


import configparser as CP


def read_config(config):
    """
    Read a section of a ConfigParse and returns dictionary.
    Note: all values will be 'string', and you will have to 
    cast to the correct type later syourself.
    """
    my_dict = {}

    for kk, vv in config.items():
        my_dict.update({kk: vv})
    return my_dict


def read_food(config):
    """
    Read the 'FOOD' section respecting the type of the variables.
    """

    my_dict = {}

    my_dict.update({"food": config.get("favorite", "lasgna")})
    my_dict.update({"weekly": config.getboolean("weekly", True)})
    my_dict.update({"times": config.getint("how_often_wk", 5)})
    my_dict.update({"price": config.getfloat("price", 50.0)})

    return my_dict


def main():
    """
    Read a configuration file similar to a Windows INI file.

    The purpose is to show how to read strings, booleans and numerical values.

    You can also add comments to your file.
    """

    my_config = CP.ConfigParser(interpolation=CP.ExtendedInterpolation())
    my_config.read("my_favorites.cfg")

    # You can query if the config file has a section before trying to read.

    if my_config.has_section("GAME"):
        my_fav_game = my_config["GAME"]["favorite"]
        print(f"My favorite game is '{my_fav_game}'.")
    else:
        print("No section GAME defined")

        # You can get a list of all sections available
        print(f"We only have {', '.join(ss for ss in my_config.sections())}")
        my_fav_game = ""

    #
    # You can pass sessions to variables to make the code cleaner.
    #

    # Here we are using the "generic" function to read, and we have to
    # convert the 'price' from string to float.

    my_food = read_config(my_config["FOOD"])
    my_drinks = read_config(my_config["DRINK"])

    food_price = float(my_food["price"])
    drink_price = float(my_drinks["price"])

    print(f"The price of a meal is {food_price + drink_price} SAR")


    # Now we use the read function that return the correct type, so
    # no need to further convertion.

    my_food = read_food(my_config["FOOD"])

    food_price = my_food["price"]

    print(f"The price of a meal is {food_price + drink_price} SAR")


if __name__ == "__main__":
    main()
