ICC = ["AUS", "IND", "PAK", "NZ", "SA", "ENG", "BAN", "AFG", "SL", "NED", "WI", "ZIM"]

country = input("Your team: ")

if country in ICC:
    print(country, "is in ICC ranking")
else:
    print("Sorry")