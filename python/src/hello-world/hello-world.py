
#!/usr/bin/env python

# hello-world.py: Gimp plug-in to greet the user.

# You may use and distribute this plug-in under the terms of the GPL.
# This file is a basic example of a Python plug-in for GIMP.
#
# It can be executed by selecting the menu option: 'Filters/Test/My Hello World'


from gimpfu import *

def hello_world(img, layer) :
    ''' Inverts the colors of the selected layer.

    Parameters:
    img : image The current image.
    layer : layer The layer of the image that is selected.
    '''
    gimp.message("Hello world form a gimp script on python.")

register(
    "python_fu_my_hello_world",
    "Hello_world",
    "Greets the user.",
    "@xavrb",
    "Open source (BSD 3-clause license)",
    "2013",
    "<Image>/Filters/Test/My Hello World",
    "*",
    [],
    [],
    hello_world)

main()
