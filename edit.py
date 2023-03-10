import json

# SECTION vars
f = open("board.json", "r")
# returns JSON object as
# a dictionary
albums = json.load(f)
accounts_ = []


array=[0,0,0,0,0,0,0,0,0,0,0,0]
setx = 0
sets=[]
while setx <12:
    sets.append(array)

for account in albums["albums"][0]["accounts"]:
    account_ = {}
    account_.update(
        {
            "name": account["name"],
            "code": account["code"],
            "bar": account["bar"],
            "percentage": account["percentage"],
            "progress": account["progress"],
            "total": account["total"],
            "extra": account["extra"],
            "missing": account["missing"],
            "spares": account["spares"],
            "sets": sets,
        }
    )
    accounts_.append(account_)
albums["albums"][0].update({"accounts": accounts_})


with open("neww.json", "w") as outfile:
    json.dump(albums, outfile)
