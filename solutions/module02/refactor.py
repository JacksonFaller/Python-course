def active_emails(users):
    return [
        email.strip().lower()
        for user in users
        if user.get("active")
        if (email := user.get("email"))
    ]
