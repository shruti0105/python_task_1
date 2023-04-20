list_1 = [
    {"id": "11", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "20", "name": "World", "age": 24},
]

list_2 = [
    {"id": "11", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


#approach 1
def merge_lists(list_1, list_2):
    
    merged_dict = {}
    for d in list_1 + list_2:
        id = d.get('id')
        if id in merged_dict:
            merged_dict[id].update(d)
        else:
            merged_dict[id] = d.copy()
    return list(merged_dict.values())

#approach 2
def merge_lists1(list_1, list_2) -> list:
    merged_list = []
    for d1 in list_1:
        for d2 in list_2:
            if d1['id'] == d2['id']:
                d1.update(d2)
                merged_dict = d1
                merged_list.append(merged_dict)
                break
        else:
            merged_list.append(d1)
            
    for d2 in list_2:
        for d1 in list_1:
            if d2['id'] == d1['id']:
                break
        else:
            merged_list.append(d2)
    return merged_list



list_3 = merge_lists(list_1,list_2)

list_4=merge_lists1(list_1,list_2)

