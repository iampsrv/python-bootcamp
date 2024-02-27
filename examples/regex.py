import re

def extract_emails(text):
    """
    Extract email addresses from a given text using regular expressions.

    :param text: A string containing text that may include email addresses.
    :return: A list of extracted email addresses.
    """
    # Regular expression pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all occurrences of the pattern in the text
    emails = re.findall(email_pattern, text)

    return emails

# Example usage
text = "Please contact us at support@example.com or feedback@example.net for further information."
extracted_emails = extract_emails(text)

print(extracted_emails)
