import sqlite3

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name


        if self.name is not None and self.id is None:
            self._save_to_db()

    def _save_to_db(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
            self.id = cursor.lastrowid  
            conn.commit()
        except Exception as e:
            print(f"Failed to insert author: {e}")
            conn.rollback()
        finally:
            conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name after the author is instantiated.")
        elif isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

    