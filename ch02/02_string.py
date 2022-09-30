name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# f-string
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

# format() method
full_name = "{} {}".format(first_name, last_name)
print(full_name)

# Adding Whitespace to Strings with Tabs or Newlines
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace
favorite_language = 'python '
print(len(favorite_language))
print(f'@{favorite_language}@')
print(f'@{favorite_language.rstrip()}@')
print(len(favorite_language))

favorite_language = favorite_language.rstrip()
print(len(favorite_language))

favorite_language = '  python   '
print(f'#{favorite_language}#')
print(f'#{favorite_language.rstrip()}#')
print(f'#{favorite_language.lstrip()}#')
print(f'#{favorite_language.strip()}#')


