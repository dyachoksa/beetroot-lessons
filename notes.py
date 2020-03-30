import io
import json
import pprint
import sys


class Note:
    pass


def get_next_id(notes):
    ids = [note["id"] for note in notes]
    return max(ids) + 1


def load_data(filename="notes.json"):
    with open(filename, "rt") as f:
        return json.load(f)


def save_data(notes, filename="notes.json"):
    with open(filename, "wt") as f:
        # data = json.dumps(notes)
        # f.write(data)
        json.dump(notes, f, sort_keys=True, indent=2)


def add_note(notes, note):
    if len(note) > 100 and len(note) < 2:
        return

    notes["notes"].append({
        "id": get_next_id(notes["notes"]),
        "note": note
    })
    save_data(notes)


def main():
    notes = load_data()
    pprint.pprint(notes)

    note = input("Enter text: ")
    add_note(notes, note)

    pprint.pprint(notes)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Done")
        sys.exit()

    print("Still working...")