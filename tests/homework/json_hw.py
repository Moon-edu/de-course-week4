from typing import Tuple
import json

def summarize() -> Tuple:
    with open('hw_data/assets.json', encoding='utf-8') as f:
        list_json_data = json.load(f)
    nsum_est_asset_dollar = sum(json_data['est_asset_dollar'] for json_data in list_json_data)

    return (nsum_est_asset_dollar, nsum_est_asset_dollar / len(list_json_data), len(list_json_data))
