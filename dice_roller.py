import random

dice_rolls = 2
dice_sum = 0

for i in range(0, dice_rolls):   # for every index in a range starting after 0 until the value is equal to dice_rolls, do this:
  
  # def main():
  roll = random.randint(1,6)   # range is inclusive
  dice_sum += roll   # same as dice_sum = dice_sum + roll
  if roll == 1:
    print(f'You rolled a {roll}! Critical Fail')
  elif roll == 6:
    print(f'You rolled a {roll}! Critical Success!')
  else:
    print(f'You rolled a {roll}')

print(f'You have rolled a total of {dice_sum}')

  # if __name__== "__main__":
  #   main()