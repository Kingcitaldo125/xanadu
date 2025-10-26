import json

class Light:
  def __init__(self,name,ip):
    self.name = name
    self.ip_address = ip
  def __str__(self):
    return f"({self.ip_address}): " + self.name

class LightFinder:
  def __init__(self):
    self.name = "LightFinder"
  def find_from_file(self,fname):
    data = {}

    try:
      with open(fname,'r') as f:
        data = json.loads(f.read())
    except FileNotFoundError as e:
      print(e)

    return []
  def find_from_ip(self):
    return []

if __name__ == "__main__":
  lf = LightFinder()
