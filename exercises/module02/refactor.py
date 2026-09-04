def active_emails(users):
    result = []
    for user in users:
        if user.get("active"):
            email = user.get("email")
            if email:
                result.append(email.strip().lower())
    return result


if __name__ == "__main__":
    users = [
        {"email": " Ada@Example.com ", "active": True},
        {"email": "bob@example.com", "active": False},
        {"email": "carol@example.com", "active": True},
    ]
    print(active_emails(users))
