#
# Berechnung des Maximums natuerlicher Zahlen
#

print("Bitte positive ganze Zahlen eingeben (negativ beendet): ")
user_input = 0  # minimalste positive Zahl
max_value = 0   # dito
while user_input >= 0:  # negative Zahl beendet
    user_input_text = input("Bitte Zahl eingeben: ")
    user_input = int(user_input_text)
    if max_value < user_input: # neues Maximum?
        max_value = user_input
        print("neues Maximum gefunden: " + user_input_text)

print("Maximum: " + str(max_value))
