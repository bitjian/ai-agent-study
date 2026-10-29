dict = {"zzj": 29, 'zyg': 32}

print(dict["zyg"])

# print(dict["rpf"])

print(dict.get("rpf"))

print(dict.pop("zyg"), dict)
dict["rpf"] = 31
print( dict)
