import sqlite3

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        
    def __repr__(self):
        return f'<Article {self.title}>'    
        
    def insert_into_database(self):
        """Inserts the article into the database."""
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        try:
            cursor.execute('''INSERT INTO articles (id, title, content, author_id, magazine_id) VALUES (?,?,?,?,?)''',
                            (self.id, self.title, self.content, self.author_id, self.magazine_id))
            connection.commit()
        except Exception as e:
            print(f"Failed to insert article: {e}")
            connection.rollback()
        finally:
            connection.close()

    def update_in_database(self):
        """Updates the article in the database."""
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        try:
            cursor.execute('''UPDATE articles SET title =?, content =? WHERE id =?''',
                            (self.title, self.content, self.id))
            connection.commit()
        except Exception as e:
            print(f"Failed to update article: {e}")
            connection.rollback()
        finally:
            connection.close()

    @classmethod
    def get_by_author(cls, author_id):
        """Retrieves articles by a specific author."""
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM articles WHERE author_id =?''', (author_id,))
        articles = [cls(*row) for row in cursor.fetchall()]
        return articles

    @classmethod
    def get_by_magazine(cls, magazine_id):
        """Retrieves articles by a specific magazine."""
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM articles WHERE magazine_id =?''', (magazine_id,))
        articles = [cls(*row) for row in cursor.fetchall()]
        return articles

    @classmethod
    def get_all(cls):
        """Retrieves all articles."""
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM articles''')
        articles = [cls(*row) for row in cursor.fetchall()]
        return articles

