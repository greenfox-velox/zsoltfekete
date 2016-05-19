# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate ():

  def __init__(self):
     self.rum = 0

  def drink_rum(self):
      self.rum += 1
      return self.rum

  def how_goin_mate(self):
    if self.rum <= 5:
        return('Nothin')
    else:
        return("Arrrrr!")

PirateJoe = Pirate()
print(PirateJoe.how_goin_mate())
PirateJoe.drink_rum()
PirateJoe.drink_rum()
PirateJoe.drink_rum()
PirateJoe.drink_rum()
PirateJoe.drink_rum()
PirateJoe.drink_rum()
print(PirateJoe.how_goin_mate())
