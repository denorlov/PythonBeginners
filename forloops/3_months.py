colours = ['red', 'yellow', 'pink', 'green', 'purple', 'orange', 'blue']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
numbers = [2, 4, 10, 5, 87, 3, 15, 8, 1]

# Display all the colours.
for i in range(0, len(colours)):
  print('Colour number', i, 'is', colours[i])

# Display all the months.
for i in range(0, len(months)):
  print('Month number', i, 'is', months[i])

# Sum up the numbers and display result.
total = 0
for i in range(0, len(numbers)):
  total = total + numbers[i]
print('The sum of the numbers is', total)