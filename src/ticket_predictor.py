def predict_ticket(text):

    lower_text = text.lower()

    # Billing
    if any(word in lower_text for word in [
        "payment", "refund", "charged", "billing", "subscription"
    ]):
        return "Billing issue", "High"

    # Account
    if any(word in lower_text for word in [
        "login", "password", "account"
    ]):
        return "Account issue", "Medium"

    # Technical
    if any(word in lower_text for word in [
        "not turning on",
        "crash",
        "error",
        "bug",
        "network",
        "slow",
        "not working"
    ]):
        return "Technical issue", "High"

    return "General inquiry", "Medium"