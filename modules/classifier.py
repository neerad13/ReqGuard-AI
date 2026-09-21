import re


def classify_requirement(requirement):
    """
    Classifies a software requirement into a requirement category.

    Categories:
    - Functional
    - Performance
    - Security
    - Usability
    - Reliability
    - Non-Functional
    """

    text = requirement.lower()

    # Performance-related keywords
    performance_words = [
        "response time",
        "within",
        "seconds",
        "milliseconds",
        "performance",
        "latency",
        "throughput",
        "load time",
        "processing time",
        "response",
        "concurrent"
    ]

    # Security-related keywords
    security_words = [
        "password",
        "authentication",
        "authorization",
        "encrypt",
        "encryption",
        "secure",
        "security",
        "access control",
        "login",
        "permission",
        "credentials",
        "privacy"
    ]

    # Usability-related keywords
    usability_words = [
        "user-friendly",
        "easy to use",
        "intuitive",
        "interface",
        "usability",
        "accessible",
        "navigation",
        "understand"
    ]

    # Reliability-related keywords
    reliability_words = [
        "reliable",
        "availability",
        "available",
        "failure",
        "recover",
        "recovery",
        "fault",
        "backup",
        "uptime",
        "failover"
    ]

    # Functional-related keywords
    functional_words = [
        "shall allow",
        "shall provide",
        "shall enable",
        "shall display",
        "shall generate",
        "shall store",
        "shall send",
        "shall receive",
        "shall calculate",
        "shall process",
        "shall create",
        "shall update",
        "shall delete",
        "shall support",
        "shall maintain",
        "shall authenticate",
        "shall verify"
    ]

    # Check categories in priority order
    if any(word in text for word in performance_words):
        return "Performance"

    if any(word in text for word in security_words):
        return "Security"

    if any(word in text for word in usability_words):
        return "Usability"

    if any(word in text for word in reliability_words):
        return "Reliability"

    if any(word in text for word in functional_words):
        return "Functional"

    # Common functional requirement pattern
    if re.search(r"\bshall\b", text):
        return "Functional"

    return "Non-Functional"