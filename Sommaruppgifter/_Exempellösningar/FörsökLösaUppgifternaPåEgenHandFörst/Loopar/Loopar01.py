# Skriv ett program som frågar användaren om ett tal och sen adderar ihop
# alla tal upp till och med det talet. När alla tal adderats så ska summan
# skrivas ut.

# Skriv programmet både med en for-loop och en while-loop. Det ska alltså
# räkna ut summan två gånger, en gång med en for-loop och en gång
# med en while-loop, resultatet ska också skrivas ut två gånger.

# T.ex.: Om man svarar att 10 ska vara sista talet i följden ska 55
# skrivas ut två gånger.

# Ett exempel på hur delar av programmet kan se ut finns nedan, ni
# är välkomna att ta bort det och skriva det helt annorlunda om ni vill.

n = int(input("Vilket tal ska vara det sista i följden? "))


summa = 0
i = 1
while i <= n:
    summa += i
    i += 1
print(summa)


summa = 0
for x in range(n + 1):
    summa += x

print(summa)
