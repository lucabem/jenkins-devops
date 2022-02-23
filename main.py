import sys
import json
 

if __name__ == "__main__":

    collection = sys.argv[1]

    print(f"We will send collection={collection}")

    with open('json/map_values.json', 'r') as f:
        json_map_ids = json.load(f)


    for i in json_map_ids[collection]:
        print(i)

    