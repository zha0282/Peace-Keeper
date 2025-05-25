import time

#Base setting
class Base:


  def __init__(self):

    self.gold = 1200

    self.platforms = {'Mid' : 'core_platform'}


    #only use for print the map
    self.init_platform = [
        self.single_platform('offline'),                               # 北
        self.single_platform('offline'),                               # 西
        self.single_platform(self.platforms.get('Mid', 'offline')),    # 中
        self.single_platform('offline'),                               # 东
        self.single_platform('offline')                                # 南
    ]

  def show_platfroms_status(self):

    #print initat message

      

      print('Structural Platform Deployment Log:"')
      time.sleep(1)
      print('   ...scanning base layout...')
      time.sleep(1)
      print('   ...signal stable...')
      time.sleep(1)
      print('   .....')
      time.sleep(1)
      print('   .....')
      time.sleep(1)
      print('   .....')
      time.sleep(1)
      print('   .....')
      time.sleep(1)
      print('Current platform in mother base:')


      for direction,value in self.platforms.items():
        print(f'{direction} Sector :{value}')

  def build_platform (self, direction, name, cost):

    #check for platforms

    
    
    if direction in self.platforms:

      print(f'A platform already exists at {direction}: {self.platforms[direction]}')

      return False


    #check for gold
    if self.gold < cost:

      print(f'Insufficient funds! {cost} required, current gold: {self.gold}.')

      return False

    #success build
    self.platforms[direction] = name
    self.gold -= cost
    print(f'Platform [{name}] successfully constructed at {direction} direction! Remaining funds: {self.gold}')

    return 



  def single_platform(self,platform_name):
     
     #create ann print the platform in box
     
      width = 22
      centered = platform_name[:width].center(width)
      box = [
              "+" + "─" * width + "+",
              f"|{centered}|",
              "+" + "─" * width + "+"
          ]
      return box


  def show_platforms(self,init_platforms):
      #print it in a cross map
      box_width = 22
      total_width = box_width * 3 + 5
      
      for p in init_platforms[0]:
          print(p.center(total_width))

      for p1, p2, p3 in zip(*init_platforms[1:4]):
          print(p1 + p2 + p3)

      for p in init_platforms[4]:
          print(p.center(total_width))

  def run_build_menu(self):



    
    #show the current map, basic on current self.init_platform
    self.show_platforms(self.init_platform)


    # input test
    while True:

      direction = input("Please choose a direction: N, W, E, S, or enter Q to exit building mode.")

      if direction.upper() == 'Q':
        break

      if  direction.upper() not in ['N', 'W', 'E', 'S']:

        print('Invalid direction. Please choose N, W, E, or S.')
        continue
      
      #inital a building list


      building_options = [
              ("Intelligence Unit", 4200),
              ("Medic Unit", 1800),
              ("Support Unit", 2900),
              ("Development Unit", 3100)
      ]


      #print the build menu

      for i in range(len(building_options)):
        name,price = building_options[i]
        print(f"{i+1}: {name} - {price}")

      choice = input("Enter facility number (1-4), or Q to exit: ")

      if choice.upper() == 'Q':
        print('Exiting building mode.')
        break

      if not choice.isdigit():
        print('Invalid input. Please enter a number like 1, 2, 3, or 4.')
        continue

      choice_num = int(choice)

      if choice_num < 1 or choice_num > 4:
        print('Invalid choice. Please enter a number between 1 and 4.')
        continue


      building_name, cost = building_options[choice_num - 1]


      #check platform can build, and add it to list, adn new the gold.

      self.build_platform(direction, building_name, cost)

      

      #renew the Base.init_platform list

      direction_index = {'N': 0, 'W': 1, 'E': 3, 'S': 4}

      #try to get the 

      platform_display_name = self.platforms.get(direction.upper(), 'offline')

      new_box = self.single_platform(platform_display_name)

      index = direction_index[direction.upper()]

      self.init_platform[index] = new_box

      self.show_platforms(self.init_platform)




if __name__ == "__main__":
    base = Base()
    base.show_platfroms_status()
    base.run_build_menu()
