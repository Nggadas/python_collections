# def sillycase(s):
#     h = int(len(s) / 2)
#
#     first_half = s[:h]
#     last_half = s[h:]
#
#     return first_half.lower() + last_half.upper()


def sillycase(text):
    start_stop = (len(text) // 2)
    new_text = text[:start_stop].lower()
    new_text += text[start_stop:].upper()
    return new_text


print(sillycase("Treehouse"))












