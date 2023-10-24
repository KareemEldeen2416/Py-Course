
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


e = "I like Python, and Java"
c = "I-like-Python,-and-Java"
d = "Kareem"
f = "I am Iron man man"
m = "I AM THOR"
print(e.split())
print(type(e.split()))
print(c.split("-"))
print(c.split("-", 2))
print(c.rsplit("-"))
print(d.center(9))
print(d.center(10, "#"))
print(f.count("a"))
print(f.count("man"))
print(f.count("a", 14, len(f)-1))
print(m.swapcase())
print(f.startswith("i"))
print(f.endswith("n", 6, len(f)))
