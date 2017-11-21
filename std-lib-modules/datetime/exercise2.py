import math


class Sphere:
  
  def __init__(self, radius):
    self.radius = radius

  def get_volume(self):
    return (4/3) * math.pi * math.pow(self.radius, 3)

  def get_area(self):
    return 4 * math.pi * math.pow(self.radius, 2)


if __name__ == '__main__':
  sphere = Sphere(10)
  print('Volume: ', sphere.get_volume())
  print('Area: ', sphere.get_area())
