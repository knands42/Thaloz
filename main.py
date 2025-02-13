# 2-5g-3-J
# 2-5G-3J
def key_formatting(license_key, k):
    length = len(license_key)
    first_group_len = length % k

    license_key = license_key.upper().replace('-', "")
    first_group = license_key[:first_group_len+1] + '-'

    remaining_groups = ""
    for idx, val in enumerate(license_key[first_group_len+1:]):
        if (idx + 1) % k == 0:
            remaining_groups += val
            remaining_groups += '-'
        else:
            remaining_groups += val

    if (remaining_groups[-1] == '-'):
        remaining_groups = remaining_groups[:-1]

    return first_group + remaining_groups

if __name__ == '__main__':
    print(key_formatting("2-5g-3-J", 2))