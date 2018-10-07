import json

def load_data(filepath):
    with open(filepath,'r') as myfile:
        return json.load(myfile)

def pretty_print_json(sample):
    for st in sample:
        print(json.dumps(st, indent=4, ensure_ascii=False, sort_keys=True))


pretty_print_json(load_data(filepath))
