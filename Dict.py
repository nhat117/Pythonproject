phone = {
    "John" : 1,
    "Jake" : 2,
    "Jill" : 3
}

phone["Jim"] = 4
del phone["Jill"]
if "Jake" in phone:
    print("Jake is listed in the phonebook.")

if "Jill" not in phone:
    print("Jill is not listed in the phonebook.")