import json 

with open("C:\\Users\Huawei\\Desktop\PP2_TSIS\\TSIS4\\json.py\\sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file) # преобразуем JSON -> словарь Python
 

object = data["imdata"]
print()
print(f"{'Interface Status'}")
print("=" * 83)
print(f"{'DN':<45} {'Description':<15} {'Speed':<9} {'MTU'}")
print('-'*43,'','-'*13,' ', '-'*7, ' ', '-'*6)


for item in object:
    attributes = item["l1PhysIf"]["attributes"]  
    dn_ = attributes["dn"]  
    description = attributes["descr"] 
    speed = attributes["speed"]  
    mtu = attributes["mtu"]  

    print(f"{dn_:<44} {description:<15} {speed:<10} {mtu}")