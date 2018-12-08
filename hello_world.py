favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

msg = "Albert Einstein once said, \"A person who never made a mistake never tried anything new.\""
print(msg)

print(3 ** 2)

age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)

# import this

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

print(bicycles[-1])

# List operation
magicians = ['alice', 'david', 'carolina']
for mag in magicians:
    print(mag)
    print(mag.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + mag.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

for value in range(1, 5):
    print(value)
numbers = list(range(1, 6))
print(numbers)

# even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = [value ** 2 for value in range(1, 11)]
print(squares)

# slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:])
print(players[:4])
print(players[-3:])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


