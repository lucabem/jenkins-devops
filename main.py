import sys
import json

import argparse




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Send collection from SBX to all ENV.')
    parser.add_argument('--collection_name', 
        type=str,  
        help='Collection where graphs are saved on origin', 
        required=True
    )
    parser.add_argument('--card_ids',
        type=str,
        help='ID to send',
        required=False
    )


    args = parser.parse_args()
    collection_name = args.collection_name

    if args.card_ids != 'all':
        ids = args.card_ids.split(',')
        ids = [int(id) for id in ids]
    else:
        ids = [i for i in range(1, 10)]

    print(f"Collection: {collection_name}")
    print(f"Cards ID: {ids}")



    