import json 
character = { 
"items": ["시계", "안경", "지갑","휴대폰","담배"], 
"skill": ["발차기","주먹지르기"] } 
with open('save.txt', 'w', encoding='utf-8') as f: 
  json.dump(character, f)

