class Box:

  def add(self):
    raise NotImplementerError()

  def empty(self):
    raise NotImplementerError()

  def count(self):
    raise NotImplementerError()


class Item:

  def __init__(self, name, value):
    self.name = name
    self.value = value


class ListBox(Box):

  def __init__(self):
    self.box = []

  def add(self, *items):
    self.box.extend(items)

  def empty(self):
    temp = self.box.copy()
    self.box.clear()
    return temp

  def count(self):
    return len(self.box)


class DictBox(Box):

  def __init__(self):
    self.box = {}

  def add(self, *items):
    for item in items:
      self.box[item.name] = item
    #self.box.update(dict((item.name, item) for item in items))

  def empty(self):
    temp = [item for _, item in self.box.items()]
    self.box.clear()
    return temp

  def count(self):
    return len(self.box)


def repack_boxes(*args):
  no_of_boxes = len(args)

  items = []

  for box in args:
    items.extend(box.empty())

  while items:
    for box in args:
      box.add(items.pop())

if __name__ == '__main__':
  box1 = ListBox()
  box1.add(Item(str(i), i) for i in range(20))

  box2 = ListBox()
  box2.add(Item(str(i), i) for i in range(9))

  box3 = DictBox()
  box3.add(Item(str(i), i) for i in range(5))

  repack_boxes(box1, box2, box3)

  print(box1.count())
  print(box2.count())
  print(box3.count())
