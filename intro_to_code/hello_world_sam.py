#Example Code for Team Coding Intro
#December 14th, 2018

print("hello world")

name_first = "Mahatma"
name_last = "Ghandi"
age = 100

print(type(age))
print(str(age))
print(type(str(age)))

print(name_first + name_last + str(age))

print(age, name_last, name_first)


#Calculate the volume of a box

height = 15
width = 80
length = 12.6

volume = height * width * length

print(str(volume))
print(type(volume))

def box_volume(height, width, length):
    return height*width*length

new_volume = box_volume(15,26.8,92)
print(new_volume)

class Box:

    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    def get_volume(self):
        return self.height * self.width * self.length



box = Box(5, 125, 5)
cube = Box(8,8,8)

print("GETTING VOLUME FROM MY BOX OBJECT!")
print(box.get_volume())
print(cube.get_volume())





