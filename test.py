import json

input_file = 'C:\\Users\\crawl\\Downloads\\specsavers.co.uk-iprules.json'
output_file = 'C:\\Users\\crawl\\OneDrive\\Desktop\\output.tsv'

with open(input_file) as json_file:
    data = json.load(json_file)

with open(output_file, "r+") as myfile:
    myfile.truncate(0)
    myfile.write("ID\tMode\tNotes\tTarget\tValue\tPaused\tModified\n")

for result in data['result']:
    result_str = result['id'] + '\t' + result['mode'] + '\t' + result['notes'] + '\t' + result['configuration']['target'] + '\t' + result['configuration']['value'] + '\t' + str(result['paused']) + '\t' + result['modified_on'] + '\n'
    
    with open(output_file, "a") as myfile:
        myfile.write(result_str)