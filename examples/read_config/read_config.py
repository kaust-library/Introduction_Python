#
# Reading a INI style configuration file

import configparser as CP

def main():
    """
    Read a configuration file similar to a Windows INI file.

    The purpose is to show how to read strings, booleans and numerical values. 

    You can also add comments to your file.
    """

    my_config = CP.ConfigParser(
        interpolation = CP.ExtendedInterpolation()
    )
    my_config.read('my_favorites.cfg')

    # You can query if the config file has a section before trying to read.

    if my_config.has_section('GAME'):
        my_fav_game = my_config['GAME']['favorite']
        print(f"My favorite game is '{my_fav_game}'.")
    else:
        print("No section GAME defined")
        # You can get all sections define
        print(f"We only have {', '.join(ss for ss in my_config.sections())}")
        my_fav_game = ""

    # fav_food = my_config['FOOD']

if __name__ == "__main__":
    main()