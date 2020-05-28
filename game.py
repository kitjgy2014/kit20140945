import json
character = {
    "name" : "정건영",
    "level" : "만렙",
    "hp" : "100",
    "items" : ["시계", "안경", "지갑","휴대폰","담배"],
    "skill" : ["공물바치기","돈주기","도망치기"]
}
with open('save.txt','r', encoding='utf-8') as f:
  date = f.read()
  character = json.loads(date)

print(type(character))
print(character)