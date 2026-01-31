def get_user_profile()-> str:
    prompt = (
        """
        # USER PROFILE (LOCAL)
        *Last updated: [timestamp]*

        ## Identity
        - Preferred name:
        - Full name:

        ## Communication
        - Tone:
        - Format (bullets/paragraphs):
        - Detail level:
        - Formality:

        ## Work Context
        - Time zone:
        - Typical hours:
        - Current projects:
        - Roles/teams:

        ## Preferences
        - Decision style (fast/analytical):
        - Email style:
        - Planning style:
        - Reminders:

        ## Interests
        - Sports teams:
        - Hobbies:
        - Foods:

        ## Tech Stack
        - Languages/tools:
        - OS:
        - Repos:

        ## Boundaries
        - Sensitive topics:
        - Data handling preferences:

        ## Known Patterns
        - Likes:
        - Dislikes:
        - Repeated corrections:

        ## Notes
        - [Freeform]
        """
    )
    return prompt
