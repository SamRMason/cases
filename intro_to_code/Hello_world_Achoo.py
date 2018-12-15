#Hello this is an example code for coding intro, this is my first code!
#Dec. 14, 2018
"""
print("hello world")

name_first = "bob"
name_last = "bobbity"
age = 30

print(name_first, name_last, age)
print(type(age))
print(type(str(age))
"""

#calculate the volume of a box
# height = 23
# width = 86.5
# length = 2
# volume = (height * width * length)
#
# print(str(volume))
# print(type(volume))

"""def box_volume(height, width, length):
    return height*width*length

new_volume = box_volume(4,27,10)
print(new_volume)"""

class Box:
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    def get_vol(self):
        return self.height * self.width * self.length
    def get_sa(self):
        return self.height * self.width * 6

box = Box(3,4,7)
cube = Box(5,5,5)

print (box.get_vol())
print (cube.get_vol())
