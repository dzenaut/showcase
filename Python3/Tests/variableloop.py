items = []
item_count = int(input("How many items are we configuring? "))
for _ in range(item_count):
    item = {}
    item['color'] = input("What color is it?")
    if item['color'] == "blue":
        item['shape'] = input("What shape is it? ")
    item['size'] = input("What size is it? ")
    items.append(item)

print(items)
