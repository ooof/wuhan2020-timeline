yaml_file_name='_data/news.yml'
json_file_name='search/news.json'
json_file2_name='search/data.json'

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


#change format to match
list2=[]
for date in item:
    if date['items'] != None:
        for news in date['items']:
            dict2={}
            dict2['date']=date['date']
            dict2['content']=news['content']
            list2.append(dict2)
            
with open(json_file2_name,'w', encoding = "utf-8") as json_file2:
    json_file2.write('data=')
    json.dump(list2, json_file2, ensure_ascii=False, indent=2)               

print('input:'+yaml_file_name)        
print('output:'+json_file_name)
print('output:'+json_file2_name)


