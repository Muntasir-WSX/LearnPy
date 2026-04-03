activities=["Running","Swimming","Cycling","Hiking","Yoga"]
group_interests=["Music","Art","Travel","Cooking","Sports"]

#chech if an activity aligns with group interests

if "Hiking" in activities and ("Hiking" in group_interests or "Sports" in group_interests):
    print("We should Hiking!")
    
elif "Yoga" in activities and ("Yoga" in group_interests or "Sports" in group_interests):
    print("Looks like a day in the pool is an order!")
    
    
    