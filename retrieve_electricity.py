import json

DATASHEET_JSON = 'compute_datasheet_info.json'
# Max Thermal Design Power (TDP) in Watts.
ELECRICITY_KEY = 'tdp'
datasheets = json.load(open(DATASHEET_JSON, 'r'))

def get_electricity(instance_type):
    return datasheets[instance_type][ELECRICITY_KEY]

if __name__ == "__main__":
    print("Printing stored details for all instance types")
    for instance_type in datasheets:
        print(instance_type)
        print("Max Thermal Design Power (TDP) in Watts: %s" %
              datasheets[instance_type][ELECRICITY_KEY])
        print("Full details:")
        print(datasheets[instance_type])