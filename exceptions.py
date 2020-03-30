#
def add_note(items, item):
    if len(item) < 5 or len(item) > 15:
        raise ValueError("Length should be between 5 and 15")
    
    items.append(item)

def get_from_db(note_id):
    # ...
        
    return note_id

def main():
    notes = ["Existing note"]
    while True:
        try:
            note = input("Enter your note: ")
            add_note(notes, note)

            print("\n".join(notes))
        except ValueError as err:
            print("Unexpected value:", err)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Done")
