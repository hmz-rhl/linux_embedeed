from sense_hat import SenseHat

import sys

sense = SenseHat()


print((sys.argv))

if len(sys.argv) > 4:

  arguments = ""
  for i in range(4,len(sys.argv)):

    arguments += sys.argv[i] + " "

  sense.show_message(arguments,  text_colour=[int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])])
