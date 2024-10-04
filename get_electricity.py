import json

DATASHEET_JSON_FID = 'compute_datasheet_info.json'
# Max Thermal Design Power (TDP) in Watts.
ELECRICITY_KEY = 'tdp'
DATASHEETS = json.load(open(DATASHEET_JSON_FID, 'r'))

def get_electricity(instance_type):
    return DATASHEETS[instance_type][ELECRICITY_KEY]

def print_supported_instances():
    return DATASHEETS.keys()

if __name__ == "__main__":
    print("Printing stored details for all instance types")
    for instance_type in DATASHEETS:
        print(instance_type)
        print("Max Thermal Design Power (TDP) in Watts: %s" %
              DATASHEETS[instance_type][ELECRICITY_KEY])
        print("Full details:")
        print(DATASHEETS[instance_type])