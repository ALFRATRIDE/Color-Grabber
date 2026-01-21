def color_grabber(center_xCoord: float = 0, center_yCoord: float = 0, initial_r: float = 0, final_r: float = 0, circle: bool = True) -> str:
    """
    #### Tracks mouse position then gets the color name of the pixel

    :param center_xCoord: Center x-coordinate
    :type center_xCoord: float
    :param center_yCoord: Center y-coordinate
    :type center_yCoord: float
    :param initial_r: Initial radius
    :type initial_r: float
    :param final_r: Final radius
    :type final_r: float

    :param circle: If you want to use the circlescan function; this moves the mouse to the center to the screen.
    :type circle: bool

    **IF**
    circle is True, then change the parameters before the bools
    
    **ELSE**
    you don't need to do anything else
    
    
    :return color: The RGB color name (a string)

    ###### [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
    ###### [pixelscan](https://github.com/dpmcmlxxvi/pixelscan)
    ###### [mouse](https://pypi.org/project/mouse/)
    ###### [math](https://docs.python.org/3/library/math.html)
    ###### [colornames](https://github.com/rgson/python-colornames?tab=readme-ov-file)
    """

    import pyautogui
    import pixelscan
    import mouse
    import math
    import colornames

    if circle:
        mouse.move(960, 540)
        for x, y in pixelscan.circlescan(center_xCoord, center_yCoord, initial_r, final_r):
            x = math.ceil(x)
            y = math.ceil(y)

            x_mouse_pos, y_mouse_pos = mouse.get_position()
            print(f"Mouse Pos: X:({x_mouse_pos}) Y:({y_mouse_pos})")

            pyautogui.moveRel(x, y)

            color_rgb = pyautogui.pixel(x_mouse_pos, y_mouse_pos)
            #print(f"RGB: {color_rgb}")

            color_name = colornames.find(color_rgb)
            print(color_name)
    elif not circle:
        x_mouse_pos, y_mouse_pos = mouse.get_position()
        print(f"Mouse Pos: X:({x_mouse_pos}) Y:({y_mouse_pos})")

        color_rgb = pyautogui.pixel(x_mouse_pos, y_mouse_pos)
        #print(f"RGB: {color_rgb}")

        color_name = colornames.find(color_rgb)
        print(color_name)

    return color_name




