from lightfinder import LightFinder

class Controller:
  def __init__(self):
    self.lights = []
  def add_light(self,l):
    self.lights.append(l)

if __name__ == "__main__":
  controller = Controller()
  lf = LightFinder()
  for light in lf.find_lights():
    controller.add_light(light)
