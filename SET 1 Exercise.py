#Exercise1 (Lists)
#1 Create a list with 5 items (names of people) and write a python program to output the 2nd item.
#Solution
students= ["David", "Samuel", "Peter", "John", "Prosper"]
print("The second student  is:", students[1])


#2 Write a python program to change the value of the first item to a new value
# Change the first item
students[0] = "Frank"

# Print the updated list
print("Updated list:", students)


#3.	Write a python program to add a sixth item to the list
students.append("Victor")
# Print the updated list
print(students)


#4.	Write a python program to add “Bathel” as the 3rd item in your list
students.insert(2, "Bathel")
print(students)

#5.	Write a python program to remove the 4th item from the list
# Remove the 4th item (index 3)
del students[3]
print(students)

#6.	Use negative indexing to print the last item in your list
# Print the last item using negative indexing
print("The last name in the list is:", students[-1])


#7.	Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
countries = ["Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi", "Nigeria", "Ghana"]
# Print the 3rd, 4th, and 5th items (indexes 2 to 4)
print(countries[2:5])

#8.	Write a list of countries and make a copy of it.
copied_list = countries.copy()
print(copied_list)


#9.	Write a python program to loop through the list of countries
# Loop through the list
for country in countries:
    print(country)


#10.Write a list of animal names and sort them in both descending and ascending order.
# List of animals
animals = ["Monkey", "lion", "eagle", "bear"]

# Sort in ascending order
animals.sort()
print("Ascending order:", animals)

# Sort in descending order
animals.sort(reverse=True)
print("Descending order:", animals)


#11.Using the list above, write a python program to output only animal names with the letter ‘a’ in them
for animal in animals:
    if 'a' in animal:
        print(animal)



#12.Write two lists, one containing your first names and the other your second names. Join the two lists.
# Lists of first and second names
first_name = ["David"]
second_name = ["Makwetta"]
full_name= first_name + second_name

print(full_name)

