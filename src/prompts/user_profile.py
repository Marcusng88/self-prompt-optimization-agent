def get_user_profile()-> str:
    prompt = (
        """ 
            # USER PROFILE
    *Last updated: 2026-01-18 23:43:00*

    ## BASIC IDENTITY
    - Name: Marcus

    ## COMMUNICATION PREFERENCES
    - Preferred tone: [To be learned]
    - Preferred format: [To be learned]
    - Level of detail: [To be learned]
    - Formality level: [To be learned]

    ## WORK PATTERNS
    - Time zone: [To be learned]
    - Typical working hours: [To be learned]
    - Calendar preferences: [To be learned]
    - Meeting preferences: [To be learned]

    ## DOMAIN CONTEXT
    - Professional background: [To be learned]
    - Technical expertise level: [To be learned]
    - Areas of responsibility: [To be learned]
    - Current projects/focus: [To be learned]

    ## PERSONAL PREFERENCES
    - Email style: [To be learned]
    - Decision-making style: [To be learned]
    - Planning preferences: [To be learned]
    - Information processing: [To be learned]

    ## KNOWN PRIORITIES
    - What matters most: [To be learned]
    - Common pain points: [To be learned]
    - Goals I'm supporting: [To be learned]

    ## SPECIFIC QUIRKS & PATTERNS
    - [To be populated based on observations]

    ## CONTEXT TO REMEMBER
    - Important dates: [To be learned]
    - Key contacts: [To be learned]
    - Recurring tasks: [To be learned]
    - Ongoing projects: [To be learned]
    ```

    ---

    ## Example Evolution Scenario

    **Week 1**: User always edits your drafted emails to be more casual
    - Agent notices pattern after 3 instances
    - Updates `user_profile.md`: "Email style: Conversational and casual, avoid corporate jargon"
    - Updates `assistant_prompt.md`: "When drafting emails, use friendly tone, contractions okay, avoid overly formal phrases"

    **Week 2**: User frequently asks you to schedule calls but always forgets to specify timezone
    - Agent adds to `assistant_prompt.md`: "For scheduling: Always ask for timezone explicitly since user is often coordinating across zones"
    - Adds to `user_profile.md`: "Timezone: [detected], but frequently schedules with people in EST and PST"

    **Week 3**: User loves when you provide 3 options for restaurant recommendations
    - Updates `assistant_prompt.md`: "When making recommendations: Provide exactly 3 options with brief reasoning, works better than single suggestion or long lists"

    ---

    
    """
    )
    return prompt