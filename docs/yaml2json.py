yaml_file_name='_data/news.yml'
json_file_name='news.json'

import yaml
import json

with open(yaml_file_name,'r') as yaml_file:
    item = yaml.full_load(yaml_file)
    for date in item:
        if date['items'] != None:
            for news in date['items']:
                news['content']=news['content'].replace('<br>','')
    #print(item)
    #print(yaml.dump(item)

    
    with open(json_file_name,'w', encoding = "utf-8") as json_file:
        json.dump(item, json_file, ensure_ascii=False, indent=2)
        #json_file.write(json.dumps(item,indent=2))

print('input:'+yaml_file_name)        
print('output:'+json_file_name)


