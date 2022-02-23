import sys
import json
import os
from metabase import Metabase

if __name__ == "__main__":

    collection = sys.argv[1]
    card_ids   = sys.argv[2]

    if card_ids != 'all':
        card_ids = card_ids.strip().split(",")
        card_ids = list(map(int, card_ids))
    else:
        pass

    print(f"We will send cards_id={card_ids} collection={collection}")

    with open('json/map_values.json', 'r') as f:
        json_map_ids = json.load(f)

    sbx_collection_id, dev_collection_id, pro_collection_id = json_map_ids[collection]

    pro = Metabase(
        endpoint='https://metabase.sofia-sbx.adn.naturgy.com',
        email=os.environ['SBX_USR'],
        password=os.environ['SBX_PSW']
    )

    print(pro.get("/card/34"))    




    