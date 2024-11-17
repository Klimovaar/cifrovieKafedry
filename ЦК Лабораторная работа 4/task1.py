# TODO решите задачу

import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    item1 = [item["weight"] for item in json_data]
    item2 = [item["score"] for item in json_data]
    umnozhenie = [item1[i] * x for i, x in enumerate(item2)]
    return(f"{sum(umnozhenie):.3f}")
print(task())
