from collections import Counter

phones = ["Samsung", "Iphone", "Samsung", "Samsung", "Iphone", "LG"]

count = Counter(phones)
print(count)

text = "Ехал Грека через реку"
count_text = Counter(text.lower().replace(" ", ""))
print(count_text)