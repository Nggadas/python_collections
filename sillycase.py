def sillycase(s):
    h = int(len(s) / 2)

    first_half = s[:h]
    last_half = s[h:]

    return first_half.lower() + last_half.upper()

print(sillycase("nggadas"))