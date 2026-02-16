"""
3
Söka efter användare
Tänk dig en funktion som kan användas för att visa sökresultat medan användaren skriver i ett sökfält. Funktionen ska ta två parametrar: input är det användaren skriver, master_list är en lista med alternativ som kan hittas.
def autocomplete_list(input, master_list):

Börja med att formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
Välj sedan ut ett AK och skriv ett testfall. (red)
Skriv sedan kod som uppfyller testfallet. (green)
Städa i koden, så du känner dig nöjd med din kod hittills. Fortsätt sedan med nästa AK.

AK1: If input is an empty string, return an empty list.
AK2: If no elements in master_list start with input, return an empty list.
AK3: If input is not an empty string, return a list of all elements in master_list that start with input. The comparison should be case-insensitive.
AK4: If input is not an empty string, return a list of all elements in master_list that contain input, sorted first by those names which start with input, 
        then by alphabetical order. The comparison should be case-insensitive.

"""
def autocomplete_list(input, master_list):
    if input == "":
        return []
    elif master_list == []:
        return []
    else:
        input_lower = input.lower()
        starts_with_input = [item for item in master_list if item.lower().startswith(input_lower)]
        contains_input = [item for item in master_list if input_lower in item.lower() and not item.lower().startswith(input_lower)]
        return sorted(starts_with_input) + sorted(contains_input)