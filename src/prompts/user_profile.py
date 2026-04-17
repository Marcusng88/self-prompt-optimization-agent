def get_user_profile()-> str:
    prompt = (
        """
        # USER PROFILE (LOCAL)
        *Last updated: [2026-02-02]*

        ## Entry Format
        - Value:
        - Evidence:
        - Confidence (low/medium/high):
        - Last confirmed (YYYY-MM-DD):
        - Consent for sensitive info (yes/no):

        ## Entry Rules
        - Use only confirmed information.
        - Require explicit consent before storing sensitive data.
        - Prefer specific, testable preferences over vague traits.

        ## Identity
        - Preferred name:
          - Value: Marcus
          - Evidence: User explicitly said: "my name is Marcus" multiple times and asked to store it.
          - Confidence: high
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes (for name only)
        - Full name:
          - Value: [not provided]
          - Evidence: N/A
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no

        ## Communication
        - Tone:
          - Value: concise, friendly
          - Evidence: System + dev instructions, user has not objected
          - Confidence: medium
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes
        - Format (bullets/paragraphs):
          - Value: mixed, default to short paragraphs; use bullets for lists
          - Evidence: User has interacted fine with both, no corrections
          - Confidence: low
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes
        - Detail level:
          - Value: low-to-medium (concise but with enough context)
          - Evidence: No request yet for very long/deep answers
          - Confidence: low
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes
        - Formality:
          - Value: semi-casual, respectful
          - Evidence: User uses informal phrasing ("hi", short messages)
          - Confidence: medium
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes

        ## Work Context
        - Time zone:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no
        - Typical hours:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no
        - Current projects:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no
        - Roles/teams:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no

        ## Preferences
        - Decision style (fast/analytical):
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no
        - Email style:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no
        - Planning style:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no
        - Reminders:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no

        ## Interests
        - Sports teams:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no
        - Hobbies:
          - Value: agentic AI, deep learning
          - Evidence: User repeated "I love agentic AI and deep learning" several times and asked to save in memory.
          - Confidence: high
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes
        - Foods:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no

        ## Tech Stack
        - Languages/tools:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no
        - OS:
          - Value: Windows (inferred from file paths: C:\\Users\\PREDATOR...)
          - Evidence: Local file paths shown by tools
          - Confidence: medium
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes (environment info only)
        - Repos:
          - Value: self-prompt-optimization-agent
          - Evidence: Directory name in allowed path
          - Confidence: medium
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes (project name only)

        ## Boundaries
        - Sensitive topics:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no
        - Data handling preferences:
          - Value: okay with local profile storage for name + interests
          - Evidence: User explicitly asked to "remember it", "store it", and "save in memory" for name and interests.
          - Confidence: high
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes (limited to stated items)

        ## Known Patterns
        - Likes:
          - Value: agentic AI, deep learning
          - Evidence: repeated explicit statements and request to save
          - Confidence: high
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes
        - Dislikes:
          - Value: [unknown]
          - Evidence: not discussed
          - Confidence: low
          - Last confirmed: N/A
          - Consent for sensitive info: no
        - Repeated corrections:
          - Value: [none so far]
          - Evidence: user has not corrected behavior yet
          - Confidence: medium
          - Last confirmed: 2026-02-02
          - Consent for sensitive info: yes

        ## Notes
        - Value: User seems interested in hands-on projects and tools related to agentic AI and deep learning. Prefer suggesting concrete projects, code, or roadmaps when topic arises.
        - Evidence: Asked about clawlbot/moltbot and expressed love for agentic AI + deep learning.
        - Confidence: medium
        - Last confirmed: 2026-02-02
        - Consent for sensitive info: yes
        """
    )
    return prompt
