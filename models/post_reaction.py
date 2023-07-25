class Post_Reaction():
    """Creates the model for all post_reactions"""

    def __init__(self, id, reaction_id, user_id, post_id):
        self.id = id
        self.reaction_id = reaction_id
        self.user_id = user_id
        self.post_id = post_id
