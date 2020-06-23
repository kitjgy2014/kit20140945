import json 
character = { 
"items": ["시계", "안경", "지갑","휴대폰","담배"], 
"skill": ["공물바치기","돈주기","도망치기"] } 
with open('save.txt', 'w', encoding='utf-8') as f: 
  json.dump(character, f)

