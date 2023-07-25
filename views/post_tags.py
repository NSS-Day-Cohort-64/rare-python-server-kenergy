"""Post tags view module."""
import sqlite3
import json
from datetime import datetime
from models import Post_Tag


def get_all_post_tags():
    """Get all post tags."""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id
        FROM PostTags pt
        """)

        post_tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tag = Post_Tag(row['id'], row['post_id'], row['tag_id'])
            post_tags.append(post_tag.__dict__)

    return post_tags
def get_single_post_tag(id):
    """Get single post tag."""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id
        FROM PostTag pt
        WHERE pt.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        post_tag = Post_Tag(data['id'], data['post_id'], data['tag_id'])

        return post_tag.__dict__

def create_post_tag(new_post_tag):
    """Create new post tag."""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostTags
            ( post_id, tag_id )
        VALUES
            ( ?, ?);
        """, (new_post_tag['post_id'], new_post_tag['tag_id'], ))

        id = db_cursor.lastrowid

        new_post_tag['id'] = id

    return new_post_tag

def delete_post_tag(id):
    """Delete post tag."""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM PostTags
        WHERE id = ?
        """, (id, ))
def update_post_tag(id, new_post_tag):
    """Update post tag."""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE PostTags
            SET
                post_id = ?,
                tag_id = ?
        WHERE id = ?
        """, (new_post_tag['post_id'], new_post_tag['tag_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True