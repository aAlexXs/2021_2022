# Izveido klasi Rekins, kas saņem 4 parametrus un izveido attiecīgas īpašības ar dotajiem lielumiem:
    self.aprekins()
def izdrukat(self):

  print('n\n')
  print("\033[1m"+'pasūtītāja dati:'+'\033[0m')
  print('-'*50)
  print(f'\x1B[3m+pasūtītāja vārds un uzvārds:\x1B [0m \033[1;32m{self.klients}\033[1;0m')
  print(f"\x1B[3mVeltijuma teksts:\x1B[0m \033[1;32m{self.veltijums}\033[1;0m)
  print(f'\1B[3mLādītes izmēri:\x1B[0m \n\x1B[3mPlatums:\x1B
  [ 0m \033[1;32m{self.platums}\033')



class Rekins:
  def __init__(self,klients,veltijums,izmers,materials):
      self.klients = klients
      self.veltijums = veltijums
      self.izmers = izmers
      self.materials = materials
  def izdrukat(self):
    print(f'klienta vārds{self.klients}')
    print(f'veltijuma teksts{self.veltijums}')
    print(f'izmērs{self.izmers}')
    print(f'izmērs{self.izmērs}')
    print(f'lodītes metriāls{self.materials}')
    self.teksta_gar = len(self.veltijums)
    self.izmeri_sar = self.izmeri.split(',')

    
  def izdrukat(self):
    pass
  def aprekins(self):
    darba_samaksa = 15
    pvn = 21
pass

veltijums = input('uzraksti veltijumu:')
izmeri = input('ievade lādītes izmērus\n garums, platums,augstums (raksti veselus skaitļus ,atdalot tos ar komatiem\n)')

print(izmeri)
print(type(izmeri))
print(izmeri.split(','))
sadal = izmeri.split(',')
print(sadal[0])
print(sadal[1])
print(sadal[2])

