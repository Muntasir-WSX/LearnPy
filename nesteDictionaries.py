family= {
    "Mom": {"name": "Jane", "age": 50, "job": "teacher"},
    "dad": { "name": "John", "age": 55, "job": "engineer"}}

for name,info in family.items():
    print(f"Parent type: {name}\n")
    # print (name,info)
    # for key, value in info.items():
    #     print (f"  {key}: {value}")
    parent_name = f"Name:{info['name']}"
    parent_age = f"Age:{info['age']}"
    
    print(f"\n{parent_name}")
    print(f"{parent_age}")