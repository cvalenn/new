x = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '4b', 'scores': [3,5,4,5,3]}, {'school_class': '4g', 'scores': [3,3,4,5,2]}]

y = []
for i in x:
    y += i['scores']
    print("Cредний бал класса", i['school_class'], "равен", sum(i['scores'])/len(i['scores']))
print("Средний бал по всей школе равен", sum(y)/len(y))