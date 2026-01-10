chai_type = "Ginger Chai"
customer_name = "Aman"

print(f"Order for {customer_name} : {chai_type} Pleases!")
cha_description  = "Aromatic and Bold"
print(f"First Word: {cha_description[0:7]}") # First Word: Aromati
print(f"First Word: {cha_description[0:8]}") # First Word: Aromatic
print(f"First Word Every Character: {cha_description[0:8:1]}") # First Word: Aromatic --> Every character
print(f"First Word Every Second Character: {cha_description[0:8:2]}") # First Word Every Second Character: Aoai --> Every Second Character

print(f"Last Word: {cha_description[12:]}") # Last Word: Bold 
print(f"Last Word: {cha_description[::-1]}") # Last Word: dloB dna citamorA

label_text = "Chai Spècial"
encoded_label = label_text.encode("utf-8")
print(f"Encoded Label: {encoded_label}") # Encoded Label: b'Chai Sp\xc3\xa8cial'
print(f"Non Encoded Label: {label_text}") # Non Encoded Label: Chai Spècial
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label: {decoded_label}") # Decoded Label: Chai Spècial