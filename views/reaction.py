"""Reaction views."""
import sqlite3
import json
from datetime import datetime
from models import Reaction

def get_all_reactions():
    """Get all reactions."""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            r.id,
            r.label,
            r.image_url
        FROM Reactions r
        """)

        reactions = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            reaction = Reaction(row['id'], row['label'], row['image_url'])
            reactions.append(reaction.__dict__)

    return reactions

def get_single_reaction(id):
    """Get single reaction."""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            r.id,
            r.label,
            r.image_url
        FROM Reactions r
        WHERE r.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        reaction = Reaction(data['id'], data['label'], data['image_url'])

        return reaction.__dict__
