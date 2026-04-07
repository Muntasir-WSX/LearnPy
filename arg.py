def sum_numbers (*args):
    return sum(args)

print (sum_numbers(1, 2, 3, 4, 5))


def build_profile (first, last, **user_info):
    user_info["first_name"]=first
    user_info["last_name"]=last
    return user_info

print(build_profile("John", "Doe", location="New York", field="Software Development"))
   