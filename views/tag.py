"""Tag views."""
import sqlite3
import json
from datetime import datetime
from models import Tag


def get_all_tags():
     # connnection to the database
    with sqlite3.connect("./db.sqlite3") as conn:
    # row_factory allows us to reference rows as dictionaries
     conn.row_factory = sqlite3.Row
     # cursor is the tool that allows us to interact with the database
     db_cursor = conn.cursor()
        # SQL query to get all tags
     db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        """)
        # initialize an empty list to hold all tag representations
    tags = []
        # convert rows of data into a Python list
    dataset = db_cursor.fetchall()
        # iterate list of data returned from database
    for row in dataset:
            # create a tag instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # tag class above.
        tag = Tag(row['id'], row['label'])
        tags.append(tag.__dict__)
            
    # return the tags list to the view
    return tags

def get_single_tag(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        WHERE t.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        tag = Tag(data['id'], data['label'])

        return tag.__dict__
def create_tag(new_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            ( label )
        VALUES
            ( ? );
        """, (new_tag['label'], ))

        id = db_cursor.lastrowid

        new_tag['id'] = id

    return new_tag

def delete_tag(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Tags
        WHERE id = ?
        """, (id, ))

        return ""

def update_tag(id, new_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Tags
            SET
                label = ?
        WHERE id = ?
        """, (new_tag['label'], id, ))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True

    
   
