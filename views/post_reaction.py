"""Post reaction view module."""
import sqlite3
import json
from datetime import datetime
from models import Post_Reaction



def get_all_post_reactions():
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pr.id,
            pr.user_id,
            pr.reaction_id
            pr.post_id
        FROM PostReaction pr
        """)
    post_reactions = []

    dataset = db_cursor.fetchall()

    for row in dataset:
        post_reaction = Post_Reaction(row['id'], row['user_id'], row['reaction_id'], row['post_id'])
        post_reactions.append(post_reaction.__dict__)

    return post_reactions

def get_single_post_reaction(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pr.id,
            pr.reaction_id,
            pr.user_id,
            pr.post_id
        FROM PostReaction pr
        WHERE pr.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        post_reaction = Post_Reaction(data['id'], data['reaction_id'], data['user_id'], data['post_id'])

        return post_reaction.__dict__
def create_post_reaction(new_post_reaction):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostReaction
            ( user_id, reaction_id, post_id )
        VALUES
            ( ?, ?, ?);
        """, (new_post_reaction['user_id'], new_post_reaction['reaction_id'], new_post_reaction['post_id'], ))

        id = db_cursor.lastrowid

        new_post_reaction['id'] = id

    return new_post_reaction







