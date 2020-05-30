import tkinter as tk

#TODO add listbox
class Application(tk.Frame):

    """Represents the GUI of the TO-DO list/journal."""
    def __init__(self, master=None):
        """Constructor creates the widgets"""
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.item = []

    def create_widgets(self):
        """Creates and packs the entry field and 'add' button."""
        self.log_entry = tk.Entry(self, width=35, bg="gray")
        self.log_entry.pack()

        self.add_entry = tk.Button(self, text="Add Item", command=self.pack_entry)
        self.add_entry.pack()

        self.delete = tk.Button(self, text="Delete Entry", command=self.delete_entry)
        self.delete.pack()

    def pack_entry(self):
        """Adds the text in the entry field to the frame after the add_entry button is clicked."""
        self.item.append(tk.Label(self, text=self.log_entry.get()))
        self.item[len(self.item)-1].pack()

    def delete_entry(self):
        removable = self.item.pop()
        removable.destroy()

root = tk.Tk()
app = Application(master=root)
app.mainloop()