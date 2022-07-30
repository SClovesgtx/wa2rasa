import json


def read_wa_object(file_path):
    with open(file_path, "r") as file:
        wa_object = json.load(file)
    return wa_object

if __name__=="__main__":
    file_path = "wa_example/My-WA-Skill-dialog.json"
    wa_object = read_wa_object(file_path=file_path)
    print(json.dumps(wa_object, sort_keys=False, indent=2))