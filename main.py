myWebsite = {"name": None, "url": None, "desc": None, "rating": None}
for name in myWebsite.keys():
  myWebsite[name] = input(f"{name}: ")
print()
for name, value in myWebsite.items():
  print(f"{name}: {value}")