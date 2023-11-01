
# print("I love python")
# print("I love programming")

# print(type(10))
# print(type("Kareem"))
# print(type(1.3))
# print(type([1, 2, 3]))  # List
# print([1, 2, 3])
# print((1, 2, 3))
# print(type((1, 2, 3)))  # Tuple
# print({"One": 1, "Two": 2})
# print(type({"One": 1, "Two": 2}))  # dict -> dictionary
# print ( 2 == 2)


# ---------------------------------------------------#


# name = "Kareem"
# print(name)
# help("keywords")  # To show reserved words
# a, b, c = 1, 2, 3
# print(a, b, c)


# ---------------------------------------------------#


# print("Hello\bworld")
# print("Hello\nworld")
# print("This is a\"Quote\"")
# print("Fifa 24\rfc  ")
# print("Python\tLanguage")
# print("\x4f")


# ---------------------------------------------------#


# msg = "I like"
# lang = "Python"
# print(msg + " " + lang)


# ---------------------------------------------------#


# myStr = """This
# is multiple line
# string with "Quote"
# """
# print(myStr)


# --------------------------------------------#

# myStr = "%^I like Python###"
# # print(myStr[0])
# # print(myStr[0: 6])
# # print(myStr[:10])
# # print(myStr[:])
# # print(myStr[0::1])
# # print(myStr[0::2])
# # print(myStr[0::3])

# print(len(myStr))
# print(myStr)
# print(myStr.strip("%^"))
# print(myStr.rstrip("#"))
# print(myStr.lstrip())

# newStr = "I like 2d graphics and 3d technololgy and python"
# print(newStr.title())
# print(newStr.capitalize())

# c = "1"
# print(c.zfill(2))
# print(myStr.upper())
# print(myStr.lower())

# ---------------------------------------------------#


# e = "I like Python, and Java"
# # c = "I-like-Python,-and-Java"
# d = "Kareem"
# f = "I am Iron man man"
# m = "I AM THOR"
# print(e.split())
# print(type(e.split()))
# print(c.split("-"))
# print(c.split("-", 2))
# print(c.rsplit("-"))
# print(d.center(9))
# print(d.center(10, "#"))
# print(f.count("a"))
# print(f.count("man"))
# print(f.count("a", 14, len(f)-1))
# print(m.swapcase())
# print(f.startswith("i"))
# print(f.endswith("n", 6, len(f)))
# print(e.index("P", 0, 10))
# # print(e.index("P", 0, 3))
# print(e.find("p", 0, 3))
# print(d.rjust(10))
# print(d.rjust(10, "$"))
# print(d.ljust(10, "$"))
# g = """First Line
# Second Line
# Third Line
# """
# print(g.splitlines())
# h = "Hello\tworld\tfrom\tpython"
# print(h.expandtabs(10))
# one = "I Like Python 3g"
# two = " "
# three = "hello world"
# four = "KAREEM4"
# five = "@yahoo"
# seven = "one one two one one two two"
# myList = ["More", "Than", "A Club"]
# print(one.istitle())
# print(two.isspace())
# print(three.islower())
# print(four.isidentifier())
# print(five.isidentifier())
# print(three.isalpha())
# print(four.isalpha())
# print(five.isalpha())
# print(one.isalnum())
# print(four.isalnum())
# print(seven.replace("one", "1"))
# print(seven.replace("one", "O", 2))
# print(" ".join(myList))


# ---------------------------------------------------#


# name = "Kareem"
# age = 35
# rank = 10
# print("My name is %s and my age is %d and my rand is %d" % (name, age, rank))

# %s string
# %d numbre
# %f float

# n = "Osama"
# l = "Arabic"
# y = 10
# print("My name is %s and I speak %s and I am %d year's old" % (n, l, y))
# print("My number is %.2f" % y)

# longString = "Hello from every where in the world"
# money = 123342342
# a, b, c = "One", "Two", "Three"
# # print("Message is %.5s" % longString)

# print("My name is {}".format(name))
# print("My name is {} and I am {} year's old".format(name, age))
# print("Name: {:s}, Age: {:d}, Rank: {:f}".format(name, age, rank))
# print("Rank is: {:.2f}".format(rank))
# print("Message is: {:.5s}".format(longString))
# print("My bank account has: {:,d}".format(money))
# print("Hello {2:s} {1} {0}".format(a, b, c))
# print(f"My name is {name}, and my age is {age}")


# ---------------------------------------------------#

# complextNumber = 1+2j
# print(type(1))
# print(type(2.1))
# print(type(5+6j))
# print("Real part is :{}".format(complextNumber.real))
# print("Imaginary part is :{}".format(complextNumber.imag))
# print(float(100))
# print(complex(100))
# print(int(10.4))
# print(complex(10.4))

# ---------------------------------------------------#

# print(1+2)
# print(-10+2)
# print(10-2)
# print(10/2)
# print(6*2)
# print(11 % 2)
# print(10 % 2)
# print(3**3)
# print(16//3)


# ---------------------------------------------------#

# myList = ["One", 1, "Two", 2, "Three", 3]
# print(myList)
# print(myList[-1])
# print(myList[1])
# print(myList[1:4])
# print(myList[1:4][0])
# print(type(myList[1:4][0]))
# myList[0] = "ONE"
# print(myList)
# myList[0:2] = []
# print(myList)
# myList[0:2] = [1, 2, 3]
# print(myList)


# ---------------------------------------------------#


# myFriends = ["Mitsuha", "Taki", "Suzume"]
# myList = ["Ran", "Mori"]
# myFriends.append("Conan")
# myFriends.append(True)
# myFriends.append(12.3)
# print(myFriends)
# myFriends.append(myList)
# print(myFriends)
# print(myFriends[len(myFriends)-1][0])
# myFriends.extend(myList)
# print(myFriends)
# myFriends.remove(myList)
# print(myFriends)

# nums = [100, 2, -10, -2, 4]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)

# chars = ["c", "z", "a"]
# chars.sort()
# print(chars)
# chars.reverse()
# print(chars)
# myFriends.reverse()
# print(myFriends)


# ---------------------------------------------------#


# a = ["Mitsuha", "Taki", "Suzume"]
# a.clear()
# print(a)
# b = ["Conan", "Ran"]
# c = b.copy()
# print(b)
# print(c)
# b.append(5)
# print(b)
# print(c)
# f = [1, 1, 3, 4, 36, 3, 6]
# print(f.count(1))
# print(f.index(1))
# f.insert(1, 199)  # insert(index , object)
# print(f)
# print(f.pop(1))
# print(f)


# ---------------------------------------------------#

# myTuple = (1, 2, "Two", "Two", True)
# simpleTuple = "Kareem", "Osama"
# print(myTuple)
# print(simpleTuple)
# print(myTuple[0])
# print(len(myTuple))
# col = myTuple + simpleTuple
# print(col)

# print("Hello" * 4)
# print([1, True] * 2)
# print(myTuple * 2)
# print(myTuple.count("Two"))
# print(myTuple)
# print(myTuple.index(True))
# x, y = simpleTuple
# print(x)
# print(y)

# ---------------------------------------------------#


# mySet = {"Osama", "Ahmed", 100}
# setOne = {1, "Osama", True, (1, 2, 3)}
# setTwo = {1, "Mitsuha", False, False}
# print(mySet)
# print(setOne)
# print(setTwo)
# mySet.clear()
# print(mySet)
# print(setOne | setTwo)
# print(setOne.union(setTwo, mySet))
# mySet.add(4)
# print(mySet)
# e = {1, 2, 3, 4}
# f = e.copy()
# print(f)
# print(type(f))
# f.remove(1)
# print(f)
# e.discard(1)
# e.discard(9)  # does not give error
# print(e)
# print(setTwo.pop())
# g = {1, "One", 2, "Two"}
# g.update(setOne, setTwo)
# print(g)
# g.update(["Japan", "China"])
# print(g)

# a = {1, 2, 3, 4}
# b = {"Ran", "Conan", 1, 2}
# print(a.difference(b))
# # a.difference_update(b)
# print(a)
# print(a.intersection(b))
# # a.intersection_update(b)
# print(a)
# print(a.symmetric_difference(b))

# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# print(a.issuperset(b))
# print(b.issubset(a))
# print(a.isdisjoint(b))

# ---------------------------------------------------#

# user = {
#     "name": "Taki",
#     "age": 36,
#     "country": "Tokyo",
#     (1, 2, 3, 4): "Test",
#     "skills": ["HTML", "CSS", "JS"],
#     "Nationality": True
# }

# print(user)
# print(user["country"])
# print(user.get("skills"))
# print(user.keys())
# print(user.values())

# languages = {
#     "One": {
#         "name": "HTML",
#         "Progress": 90
#     },

#     "Two": {
#         "name": "CSs",
#         "Progress": 80
#     },

#     "Three": {
#         "name": "JS",
#         "Progress": 100
#     }
# }

# print(languages["One"]["name"])
# print(languages["Two"]["Progress"])
# print(len(languages))
# print(len(languages["Two"]))

# overAll = {
#     "Programming languages": languages,
#     "Users": user
# }
# print(overAll)


# user = {
#     "name": "Taki",
#     "age": 36,
#     "country": "Tokyo",
#     (1, 2, 3, 4): "Test",
#     "skills": ["HTML", "CSS", "JS"],
#     "Nationality": True
# }

# user.clear()
# print(user)
# user["newKey"] = "newValue"
# user.update({"newKeyMethod": "newValueMethod"})
# print(user)

# e = user.copy()
# print(e)
# e.update({"Skill": "Resistance"})
# print(e)
# print(user)


# user = {
#     "name": "Mitsuha",
#     "age": 30
# }
# print(user)
# print(user.setdefault("name", "Taki"))
# print(user)
# user.setdefault("age", 19)
# print(user)

# member = {
#     "name": "Conan",
#     "skill": "Detection"
# }
# print(member)
# print(member.popitem())
# print(type(member.popitem()))
# print(member)

# view = {
#     "name": "Conan",
#     "skill": "Detection"
# }

# allItems = view.items()
# print(view)
# print(type(allItems))
# print(allItems)
# view["age"] = 39
# print(allItems)

# a = ("myKeyOne", "myKeyTwo", "myKeyThree")
# b = "x"
# print(dict.fromkeys(a, b))


# ---------------------------------------------------#


# name = " "
# print(name.isspace())
# print(100 > 200)
# print(10 > 0)
# print(bool("Osama"))
# print(bool(100))
# print(bool(True))
# print(bool([1, 2, 3]))
# print(bool((1, 2, 3)))
# print(bool(0))
# print(bool(False))
# print(bool([]))
# print(bool({}))
# print(bool(None))


# age = 36
# country = "Egypt"
# rank = 2
# print(age > 10 and country == "Egypt")
# print(age > 40 or country == "Egypt" or rank > 1)
# print(age > 40 or country == "Egypt" or rank < 1)
# print(not (age > 10))


# ---------------------------------------------------#

# age = 10
# age += 2
# print(age)  # 12
# age -= 10
# print(age)  # 2
# age *= 3
# print(age)  # 6
# age /= 2
# print(age)  # 3
# age **= 3
# print(age)  # 27
# age %= 4
# print(age)  # 3
# age = 34
# age //= 3
# print(age)  # 11


# ---------------------------------------------------#

# print(100 == 100)
# print(100 == 200)
# print(100 == 100.0)
# print(100 != 100)
# print(100 != 200)
# print(10 > 5)
# print(2 > 5)
# print(10 >= 10)
# print(2 >= 5)
# print(2 < 5)
# print(2 <= 2)


# ---------------------------------------------------#


# a = 10
# print(type(a))
# print(type(str(a)))
# c = "Osama"
# d = [1, 2, 3, 4, 5]
# e = {"A", "B", "c"}
# f = {"one" , "two"}
# print(tuple(c))
# print(tuple(d))
# print(tuple(e))
# print(tuple(f))
# print(list(c))
# print(list(d))
# print(list(e))
# print(list(f))
# print(set(c))
# print(set(d))
# print(set(e))
# print(set(f))


# ---------------------------------------------------#


# fname = input("Enter your first name\n")
# print(f"Your name is: {fname}")


# ---------------------------------------------------#

# email = input("Enter your email address\n").
# print(f"User name is: {email[:email.index("@")]} ")
# print(f"Your website is: {email[email.index("@")+1: email.index(".")]}")


# ---------------------------------------------------#

# age = int(input("What is your age?\n").strip())

# months = age * 12
# week = age * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# print(f"Your age is {months} months\n, {week} weeks\n, {days} days\n, {hours} hours\n, {minutes} minutes\n, and {seconds} seconds\n")


# ---------------------------------------------------#


# userName = "Osama"
# course = "Python Course"
# country = "Egypt"
# job = "Student"
# cPrice = 100
# cDiscount = 0

# if country == "Egypt":
#     if job == "Student":
#         cDiscount = 90
#     else:
#         cDiscount = 70
# elif country == "Makka":
#     cDiscount = 10
# else:
#     cDiscount = 20
# print(f"Hello {userName} {course} is {cPrice-cDiscount}$")


# ---------------------------------------------------#


# country = "Egypt"
# print("A beautiful country" if country ==
#       "Egypt" else "Not more beautiful than Egypt")


# ---------------------------------------------------#

# age = input("Please, type your age\n").strip()
# unit = input("Please choose time unit: Months, Weeks, Days\n").strip().lower()
# months = int(age) * 12
# weeks = months * 4
# days = int(age) * 365
# if unit == "months" or unit == "m":
#     print(f"You choose months\nYou live for {months} months")
# elif unit == "days" or unit == "d":
#     print(f"You choosed days\nYou lived for {days} days")
# elif unit == "weeks" or unit == "w":
#     print(f"You choosed weeks\nYou lived for {weeks} weeks")
# else:
#     print("Wrong unit")

# ---------------------------------------------------#

# name = "Osama"
# print("s" in name)
# print("a" in name)
# print("o" in name)
# friends = ["Ahmed", "Sayed", "Mahmoud"]
# print("Osama" in friends)
# print("Ahmed" not in friends)
# print("Osama" not in friends)

# countriesOne = ["Egypt", "Makka", "Tunisia"]
# countriesTwo = ["Bahrain", "Sudan"]
# discount = 0
# country = "Sudan"
# if country in countriesOne:
#     discount = 30
# elif country in countriesTwo:
#     discount = 10
# else:
#     discount = 0

# print(f"Discount is {discount}")


# ---------------------------------------------------#

# admins = ["Kareem", "Osama", "Saif", "Ahmed"]
# name = input("Enter your name\n").strip().capitalize()

# if name in admins:
#     print(f"Welcome {name} to the system")
#     option = input("Delete or Update your name\n").strip().capitalize()
#     if option == "Update":
#         newName = input("Enter your new name\n").strip().capitalize()
#         print(f"Your new name is {newName}")
#         admins[admins.index(name)] = newName
#         print("Name updated successfully")
#         print(admins)
#     elif option == "Delete":
#         admins.remove(name)
#         print("Name deleted successfully")
#         print(admins)
#     else:
#         print("This is not an option")
# else:
#     print(f"{name}, you are not authorized to access the system")
#     status = input(
#         "You are not an admin would you like to be added\n").strip().capitalize()
#     if status == "Yes":
#         admins.append(name)
#         print("You were added successfully")
#         print(admins)
#     elif status == "No":
#         print("Okay, Thank you")
#     else:
#         print("This is not an option")


# ---------------------------------------------------#
