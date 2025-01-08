#notes app base

#notes app base
import os
import json

class NotesApp:

    def __init__(self, filename="notes.json"):
        
        self.filename = filename

        self.notes = self.load_notes()

    def load_notes(self):

        if os.path.exists(self.filename):

            with open(self.filename, "r") as file:

                return json.load(file)
            
        return {}
    
    def save_notes(self):

        with open(self.filename, "w") as file:

            json.dump(self.notes, file, indent = 4)

    def add_note(self, title, content):

        if title in self.notes:

            print("A note with this title already exists.")

        else:

            self.notes[title] = content
            
            self.save_notes()

            print("Note added successfully.")

    def view_notes(self):

        if not self.notes:

            print("No notes found.")

        else:

            print("\nYour Notes:")

            for title, content in self.notes.items():

                print(f"\nTitle: {title}\nContent: {content}")

    def delete_note(self, title):

        if title in self.notes:
            
            del self.notes[title]

            self.save_notes()

            print("Note deleted successfully")

        else:

            print("Note not found.")

        
    def update_note(self, title, new_content):

        if title in self.notes:

            self.notes[title] = new_content

            self.save_notes()

            print("Note updated successfully")

        else:

            print("Note not found.")

def main():

    app = NotesApp()

    while 1:

        print("\n--- Notes App ---")

        print("1. Add Note")
        
        print("2. View Notes")
        
        print("3. Delete Note")
        
        print("4. Update Note")

        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            title = input("Enter note title: ")

            content = input("Enter note content: ")

            app.add_note(title, content)

        elif choice == "2":

            app.view_notes()
        
        elif choice == "3":

            title = input("Enter note title to delete: ")

            app.delete_note(title)

        elif choice == "4":

            title = input("Enter note title to update: ")

            new_content = input("Enter new content: ")

            app.update_note(title, new_content)

        elif choice == "5":

            print("Exiting Notes App. Goodbye!")

            break
        
        else:

            print("Invalid choice! Please try again.")

    
    if __name__ == "__main__":
        
        main()
