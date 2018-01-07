#!/usr/bin/python
# hello-world.py: Gimp plug-in to greet the user.

# You may use and distribute this plug-in under the terms of the GPL.
# This file is a basic example of a Python plug-in for GIMP.
#
# It can be executed by selecting the menu option: 'Filters/Test/My Hello World'


from gimpfu import *

def hello_world(img, layer) :
    ''' Greets the user.

    Parameters:
    img : image The current image.
    layer : layer The layer of the image that is selected.
    '''
    gimp.message("Hello world form a gimp script on python.")

register(
    "python_fu_my_hello_world",
    "hello_world",
    "Greets the user.",
    "xavrb",
    "GNU GLP 2.0",
    "2018",
    "<Image>/Filters/HELLO",
    "RGB*, GRAY*",
    [],
    [],
    hello_world)

main()
