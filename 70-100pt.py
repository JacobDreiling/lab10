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

#80pt
#rectangles, ellipses, and poly's
sky = drawpad.create_rectangle(0,0,800,600, fill = '#FFC663')
grass = drawpad.create_rectangle(0,520,800,600, fill = 'darkgreen')
forwaertshaus = drawpad.create_rectangle(160,350,400,540, fill = '#7300FF') #100pt- including fills now
rueckwaertshaus = drawpad.create_rectangle(400,390,640,540, fill = '#7300FF')
dome = drawpad.create_oval(400,120,640,350, fill = '#D1FAFF')
sciencepart = drawpad.create_rectangle(400,240,640,390, fill = '#7300FF')
roof = drawpad.create_polygon(80,350,140,300,410,300,470,350, fill = 'grey')

root.mainloop()