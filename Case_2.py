class BuildingTechnics:
  def __init__(self,model,manufacturer):
    self.model=model
    self.manufacturer=manufacturer

  def get_info(self):
    return f"{self.model} производитель {self.manufacturer}"
  
class Excavator(BuildingTechnics):
  def __init__(self, model, manufacturer, bucket_size,weight):
    super().__init__(model, manufacturer)
    self.bucket_size = bucket_size
    self.weight = weight

  def get_info(self):
    info = super().get_info()
    return f"{info} обьем ковша {self.bucket_size} м³ вес {self.weight} т"
  
class Bulldozer(BuildingTechnics):
  def __init__(self, model, manufacturer, blade_size,weight):
   super().__init__(model, manufacturer)
   self.blade_size = blade_size
   self.weight = weight

  def get_info(self):
   info = super().get_info()
   return f"{info} площадь отвала {self.blade_size} м² вес {self.weight} т"
  
excavator = Excavator("Komatsu PC200", "Komatsu", 0.6, 19)
bulldozer = Bulldozer("Caterpillar D6R", "Caterpillar", 3.2, 21)

print(excavator.get_info())
print(bulldozer.get_info())

