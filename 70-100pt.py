##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#70pt
#rek'd's
forwaertshaus = drawpad.create_rectangle(160,350,400,540, fill = 'purple') #100pt- including fills now
rueckwaertshaus = drawpad.create_rectangle(400,390,640,540, fill = 'purple')
#lines -painful..
unterline = drawpad.create_line(80,350,480,350, fill = 'gray')
ueberline = drawpad.create_line(140,300,420,300, fill = 'gray')
linkeline = drawpad.create_line(80,350,140,300, fill = 'gray')
rechtline = drawpad.create_line(420,300,480,350, fill = 'gray')
cylrecht = drawpad.create_line(640,240,640,540, fill = 'lightblue')
cylueber = drawpad.create_line(400,240,640,240, fill = 'lightblue')
cyltopl = drawpad.create_line(400,240,400,300, fill = 'lightblue')

root.mainloop()