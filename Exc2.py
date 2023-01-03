
# Διάβασμα της κατανάλωσης (consumption) ανά 100 χλμ. από το χρήστη (θετικός, float αριθμός)
consumption = float(input("Δώσε την κατανάλωση του οχήματος ανά 100 χλμ σε λίτρα (float): "))

# Διάβασμα της απόστασης (distance), που θα διανύσει το όχημα, από το χρήστη
distance = float(input("Δώσε την απόσταση που θα καλύψει το όχημα σε χλμ (float) : "))

# Η ποσότητα καυσίμων (fuel) που απαιτείται για ένα δρομολόγιο δίνεται από την παρακάτω σχέση :
fuel = (consumption / 100) * distance

# Εμφάνιση τελικού μηνύματος και αποτελέσματος
print(f"Για κατανάλωση ίση με {consumption} λίτρα ανά 100 χλμ, και για απόσταση ίση με {distance} χλμ, απαιτείται ποσότητα καυσίμων ίση με {fuel} λίτρα")

input()