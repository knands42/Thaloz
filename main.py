# 2-5g-3-J
# 2-5G-3J
def key_formatting(license_key, k):
    count = 0

    license_key = license_key.upper()
    license_key = license_key.replace('-', "")

    for i in license_key:
        count+=1

    quotient = count // k
    rest = count % k

    remaning_groups = ""
    curr_count = 0
    for val in license_key[rest:]:
        if curr_count == k
            curr_count = 0
            remaning_groups.concat("-")
        
        remaning_groups.concat(val)
    
    del remaning_groups[-1]

    first_group = ""
    if rest != 0:
        for i in range(rest):
            first_group.concat(i)
        first_group.concat("-")

    result = first_group.concat(remaning_groups)
 return result

key_formatting("2-5g-3-J")