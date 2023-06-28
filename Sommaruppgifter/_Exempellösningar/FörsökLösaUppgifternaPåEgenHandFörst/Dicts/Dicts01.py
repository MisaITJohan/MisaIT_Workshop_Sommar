# Skriv ett program som lagar information i ett Dictionary och sen
# hämtar ut något som skrivs ut på skärmen.
# Ett sätt som kan användas är att användaren får en fråga om vilket värde
# som ska hämtas.

# Exempel på saker som kan lagras:
# Personer(längd, ålder, etc.)
# Böcker(författare, titel, ISBN, mängd sidor, etc.)
# Recept(ingredienser, tillagningstid, etc.)
# Länder(de tre största städerna, språk, namn på det egna språket, etc.)

personer = {
    "Anna": {"ålder": 30, "längd": 178},
    "Bertil": {"ålder": 31, "längd": 179},
    "Caesar": {"ålder": 32, "längd": 180}
    }

vem = input("Vems uppgifter ska jag hämta? ").capitalize()

print(personer[vem])
