# Phishing Awareness Analyzer

def analyze_message(text):

    text = text.lower()
    red_flags = []

    # 1. Urgency & Pressure
    urgency_words = [
        "immediate action required", "final notice", "act now",
        "limited time", "hurry", "urgent", "now"
    ]

    # 2. Account Warnings & Threats
    account_words = [
        "account suspended", "unauthorized access", "security breach",
        "verify your identity", "confirm your details",
        "account locked"
    ]

    # 3. Financial Gain & Enticement
    financial_words = [
        "free", "winner", "claim your prize",
        "payment status", "exclusive offer"
    ]

    # 4. Fake Greetings
    greeting_words = [
        "dear valued member", "dear customer",
        "dear account holder", "are you available"
    ]

    # 5. Social Engineering
    social_words = ["send me", "share your", "give me", "provide"]

    # 6. Threat words
    threat_words = ["kill", "die", "attack", "hack", "threat"]

    # 7. DOMAIN DETECTION
    real_domains = ["google.com", "amazon.com", "paypal.com", "microsoft.com"]

    words = text.split()

    for word in words:
        if "@" in word:
            domain = word.split("@")[-1]

            if domain in real_domains:
                continue

            detected = False

            for real in real_domains:
                if real.replace(".com", "") in domain:
                    red_flags.append(f"⚠ Possible fake domain: {domain} (looks like {real})")
                    detected = True
                    break

            if not detected:
                red_flags.append(f"⚠ Unknown/suspicious domain: {domain}")

    # Keyword checks
    for word in urgency_words:
        if word in text:
            red_flags.append(f"⚠ Urgency detected: {word}")

    for word in account_words:
        if word in text:
            red_flags.append(f"⚠ Account threat detected: {word}")

    for word in financial_words:
        if word in text:
            red_flags.append(f"⚠ Financial bait detected: {word}")

    for word in greeting_words:
        if word in text:
            red_flags.append(f"⚠ Generic greeting detected: {word}")

    for word in social_words:
        if word in text:
            red_flags.append(f"⚠ Sensitive request detected: {word}")

    for word in threat_words:
        if word in text:
            red_flags.append(f"⚠ Threat detected: {word}")

    # OTP DETECTION
    if "otp" in text:

        safe_patterns = ["don't share", "do not share", "for your security"]

        if not any(p in text for p in safe_patterns):
            red_flags.append("⚠ Suspicious OTP request detected")

    # NUMBER DETECTION
    if any(char.isdigit() for char in text):
        if "otp" in text or "bank" in text or "account" in text:
            red_flags.append("⚠ Contains sensitive numeric information")

    # Link detection
    if "http://" in text or "https://" in text or ".apk" in text:
        red_flags.append("⚠ Suspicious link detected")

    return red_flags


# main

print("🔍 Phishing Awareness Analyzer")

message = input("Enter email/message: ")

flags = analyze_message(message)

print("\n🔎 Analysis Result:")

if len(flags) == 0:
    print("✅ Safe Message")
else:
    print("❌ Suspicious Message Detected!\n")
    for f in flags:
        print(f)