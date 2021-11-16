thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color":"red"
}


thisdict["brand"] = "Opel"

print(thisdict["model"])
print(thisdict.values())
print(thisdict.keys())
print(thisdict.items())

for k,v in thisdict.items():
    print(str(k) + "=>" + str(v))

for val in thisdict.values():
    print(val)

