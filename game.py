wumpusWorld = [
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', '']
]

wumpusWorld[0][3] = '💢'
wumpusWorld[1][0] = '👾'
wumpusWorld[1][2] = '💢'
wumpusWorld[3][0] = '🕵️‍♂️'
wumpusWorld[3][2] = '💢'
wumpusWorld[1][1] = '🏆'
wumpusWorld[0][2] = '🍃'
wumpusWorld[1][3] = '🍃'
wumpusWorld[2][2] = '🍃'
wumpusWorld[3][1] = '🍃'
wumpusWorld[3][3] = '🍃'
wumpusWorld[0][0] = '🤢'
wumpusWorld[2][0] = '🤢'


actions = ['up', 'down', 'left', 'right']
costs = [1, 1, 1, 1]  # Cost for each action: up, down, left, right

def update_location(move, x, y):
 cost = 0
 # check move to up
 if move == actions[0]:
     if x - 1 >= 0:
         if wumpusWorld[x - 1][y] != '👾' and wumpusWorld[x - 1][y] != '💢' and wumpusWorld[x - 1][y] != '🏆' and wumpusWorld[x - 1][y] != '🤢' and wumpusWorld[x - 1][y] != '🍃':
             wumpusWorld[x][y] = ''
             wumpusWorld[x - 1][y] = '🕵️‍♂️'
             cost = costs[0]
         elif wumpusWorld[x - 1][y] == '👾':
             wumpusWorld[x][y] = ''
             wumpusWorld[x - 1][y] = '👾'
             cost = costs[0]
         elif wumpusWorld[x - 1][y] == '💢':
             wumpusWorld[x][y] = ''
             wumpusWorld[x - 1][y] = '💢'
             cost = costs[0]
         elif wumpusWorld[x - 1][y] == '🏆':
             wumpusWorld[x][y] = ''
             wumpusWorld[x - 1][y] = '🏆'
             cost = costs[0]
         elif wumpusWorld[x - 1][y] == '🤢':
             print('\033[31mbe be careful there is wumps 👾 near you\033[0m')
             print('------------------------------------------------')
             wumpusWorld[x][y] = ''
             wumpusWorld[x - 1][y] = '🕵️‍♂️'
             cost = costs[0]
         elif wumpusWorld[x - 1][y] == '🍃':
             print('\033[31mbe be careful there is pit near you 💢\033[0m')
             print('------------------------------------------------')
             wumpusWorld[x][y] = ''
             wumpusWorld[x - 1][y] = '🕵️‍♂️'
             cost = costs[0]
         return x - 1, y, cost
# check move to down
 elif move == actions[1] and x + 1 < len(wumpusWorld):
     if wumpusWorld[x + 1][y] != '👾' and wumpusWorld[x + 1][y] != '💢' and wumpusWorld[x + 1][y] != '🤢' and wumpusWorld[x + 1][y] != '🏆' and wumpusWorld[x + 1][y] != '🍃':
         wumpusWorld[x][y] = ''
         wumpusWorld[x + 1][y] = '🕵️‍♂️'
         cost = costs[1]
     elif wumpusWorld[x + 1][y] == '👾':
         wumpusWorld[x][y] = ''
         wumpusWorld[x + 1][y] = '👾'
         cost = costs[1]
     elif wumpusWorld[x + 1][y] == '💢':
         wumpusWorld[x][y] = ''
         wumpusWorld[x + 1][y] = '💢'
         cost = costs[1]
     elif wumpusWorld[x + 1][y] == '🏆':
          wumpusWorld[x][y] = ''
          wumpusWorld[x + 1][y] = '🏆'
          cost = costs[1]
     elif wumpusWorld[x + 1][y] == '🤢':
             print('\033[31mbe be careful there is wumps 👾 near you\033[0m')
             print('------------------------------------------------')
             wumpusWorld[x][y] = ''
             wumpusWorld[x + 1][y] = '🕵️‍♂️'
             cost = costs[0]
     elif wumpusWorld[x + 1][y] == '🍃':
             print('\033[31mbe be careful there is pit near you 💢\033[0m')
             print('------------------------------------------------')
             wumpusWorld[x][y] = ''
             wumpusWorld[x + 1][y] = '🕵️‍♂️'
             cost = costs[0]
     return x + 1, y, cost
# check move to right
 elif move == actions[2] and y - 1 >= 0:
     if wumpusWorld[x][y - 1] != '👾' and wumpusWorld[x][y - 1] != '💢' and wumpusWorld[x][y - 1] != '🏆' and wumpusWorld[x][y - 1] != '🤢' and wumpusWorld[x][y - 1] != '🍃':
         wumpusWorld[x][y] = ''
         wumpusWorld[x][y - 1] = '🕵️‍♂️'
         cost = costs[2]
     elif wumpusWorld[x][y - 1] == '👾':
         wumpusWorld[x][y] = ''
         wumpusWorld[x][y - 1] = '👾'
         cost = costs[2]
     elif wumpusWorld[x][y - 1] == '💢':
         wumpusWorld[x][y] = ''
         wumpusWorld[x][y - 1] = '💢'
         cost = costs[2]
     elif wumpusWorld[x][y - 1] == '🏆':
          wumpusWorld[x][y] = ''
          wumpusWorld[x][y - 1] = '🏆'
          cost = costs[2]
     elif  wumpusWorld[x][y - 1] == '🤢':
             print('\033[31mbe be careful there is wumps 👾 near you\033[0m')
             print('------------------------------------------------')
             wumpusWorld[x][y] = ''
             wumpusWorld[x][y - 1] = '🕵️‍♂️'
             cost = costs[0]
     elif wumpusWorld[x][y - 1] == '🍃':
             print('\033[31mbe be careful there is pit near you 💢\033[0m')
             print('------------------------------------------------')
             wumpusWorld[x][y] = ''
             wumpusWorld[x][y - 1] = '🕵️‍♂️'
             cost = costs[0]     
     return x, y - 1, cost
# check move to left
 elif move == actions[3] and y + 1 < len(wumpusWorld[0]):
     if wumpusWorld[x][y + 1] != '👾' and wumpusWorld[x][y + 1] != '💢' and wumpusWorld[x][y + 1] != '🏆' and wumpusWorld[x][y + 1] != '🤢' and wumpusWorld[x][y + 1] != '🍃':
         wumpusWorld[x][y] = ''
         wumpusWorld[x][y + 1] = '🕵️‍♂️'
         cost = costs[3]
     elif wumpusWorld[x][y + 1] == '👾':
         wumpusWorld[x][y] = ''
         wumpusWorld[x][y + 1] = '👾'
         cost = costs[3]
     elif wumpusWorld[x][y + 1] == '💢':
         wumpusWorld[x][y] = ''
         wumpusWorld[x][y + 1] = '💢'
         cost = costs[3]
     elif wumpusWorld[x][y + 1] == '🏆':
          wumpusWorld[x][y] = ''
          wumpusWorld[x][y + 1] = '🏆'
          cost = costs[3]
     elif wumpusWorld[x][y + 1] == '🤢':
             print('\033[31mbe be careful there is wumps 👾 near you\033[0m')
             print('------------------------------------------------')
             wumpusWorld[x][y] = ''
             wumpusWorld[x][y + 1] = '🕵️‍♂️'
             cost = costs[0]
     elif wumpusWorld[x][y + 1] == '🍃':
             print('\033[31mbe be careful there is pit near you 💢\033[0m')
             print('------------------------------------------------')
             wumpusWorld[x][y] = ''
             wumpusWorld[x][y + 1] = '🕵️‍♂️'
             cost = costs[0]   
     return x, y + 1, cost
 else:
     return x, y, cost



def print_grid(wumpusWorld):
   for row in wumpusWorld:
       for cell in row:
           print(cell if cell != '' else '⬜', end='   ')
       print()

def main():
  x, y = 3, 0
  total_cost = 0 # Initialize total cost to 0
  print_grid(wumpusWorld) # Print the initial grid
  while True:
      move = input('Enter a move: ')
      x, y, cost = update_location(move, x, y)
      total_cost += cost # Update the total cost
      print_grid(wumpusWorld) # Print the grid after each move
      print('------------------------------------------------')
      if wumpusWorld[x][y] == '🏆':
          print('\033[33mYou found the gold 🎉🎊🏆\033[0m')
          print('Total cost:', total_cost)
          break
      elif wumpusWorld[x][y] == '👾':
          print('\033[34mYou were eaten by a Wumpus👾\033[0m')  
          break
      elif wumpusWorld[x][y] == '💢':
          print('\033[34mYou fell into a pit.\033[0m')
          break


main()



