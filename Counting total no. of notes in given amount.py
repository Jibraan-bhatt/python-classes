#To count total number of notes in given amount
def count_notes(amount):
    denominations = [1000, 400, 100, 70, 40, 30, 20, 15, 2, 1]
    note_counter = {}
    for note in denominations:
        if amount >= note:
            count = amount // note  # Number of notes of the current denomination
            amount = amount % note  # Remaining amount after taking those notes
            note_counter[note] = count
    return note_counter
amount = int(input("Enter the amount: "))
note_counter = count_notes(amount)
print("\nCurrency notes breakdown:")
for note, count in note_counter.items():
    print(f"{note} : {count}")