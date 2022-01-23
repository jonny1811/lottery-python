import json


class Json:
    def write(file_name, save_json):
        with open(file_name, "w") as outfile:
            json.dump(save_json, outfile)

    def read(file_name):
        with open(file_name) as json_file:
            return json.load(json_file)
