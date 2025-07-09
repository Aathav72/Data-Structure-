brand = "MSI"
reversed_brand = brand[::-1]
print("Reversed brand:", reversed_brand)

sentence = "Popular brands are Dell, HP, and Lenovo"
if "Dell" in sentence:
    print("Found 'Dell' in the sentence.")
else:
    print("Did not find 'Dell' in the sentence.")

text = "HP, HP, Lenovo, Dell"
count_hp = text.count("HP")
print("HP appears", count_hp, "times.")

brands = ["Lenovo", "Dell", "HP", "Asus"]
brands.sort()
print("Sorted brands:", brands)


sentence = "Apple is a premium brand"
updated_sentence = sentence.replace("Apple", "MSI")
print("Updated sentence:", updated_sentence)
