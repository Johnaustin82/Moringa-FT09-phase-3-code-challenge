import sqlite3
from .article import Article  
from .author import Author  

class Magazine:
    def __init__(self, name, category):
        self._id = None  
        self._name = None  
        self._category = None  
        self.name = name  
        self.category = category  

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:  
            self._name = value  
            try:
                self._update_name_in_database()  
            except Exception as e:
                print(f"Failed to update name in database: {e}")
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")  

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0: 
            self._category = value  
            try:
                self._update_category_in_database()  
            except Exception as e:
                print(f"Failed to update category in database: {e}")
        else:
            raise ValueError("Category must be a non-empty string.")  

    def _get_connection(self):
        return sqlite3.connect('database.db')

    def _execute_query(self, query, params=()):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def _update_name_in_database(self):
        query = "UPDATE magazines SET name = ? WHERE id = ?"
        self._execute_query(query, (self._name, self._id))

    def _update_category_in_database(self):
        query = "UPDATE magazines SET category = ? WHERE id = ?"
        self._execute_query(query, (self._category, self._id))

    

