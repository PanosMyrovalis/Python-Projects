
# Η κατανάλωση (consumption) πρέπει να είναι θετικός, float αριθμός (π.χ. 6.6)
consumption = float(input("Δώσε την κατανάλωση του οχήματος ανά 100 χλμ σε λίτρα (float): "))

# Η απόσταση (distance) πρέπει να είναι θετικός, float αριθμός (π.χ. 215.5)
distance = float(input("Δώσε την απόσταση που θα καλύψει το όχημα σε χλμ (float) : "))

# Η ποσότητα καυσίμων (fuel) που απαιτείται για ένα δρομολόγιο δίνεται από την παρακάτω σχέση :
fuel = (consumption / 100) * distance

# Εμφάνιση τελικού μηνύματος και αποτελέσματος
print("Η απαιτούμενη ποσότητα που απαιτείται για το δρομολόγιο είναι", fuel, "λίτρα")

input()