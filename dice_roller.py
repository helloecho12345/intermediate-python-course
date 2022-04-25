import random

dice_rolls = 2

for i in range(0, dice_rolls):   # for every index in a range starting after 0 until the value is equal to dice_rolls, do this:
  
  def main():
    roll = random.randint(1,6)   # range is inclusive
    print(f'You rolled a {roll}')

  if __name__== "__main__":
    main()