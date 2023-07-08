import re
import requests

def search_email(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

def search_phone(text):
    pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    phone_numbers = re.findall(pattern, text)
    return phone_numbers

def search_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        emails = search_email(response.text)
        phone_numbers = search_phone(response.text)

        print("Email Addresses:")
        for email in emails:
            print(email)

        print("\nPhone Numbers:")
        for phone_number in phone_numbers:
            print(phone_number)

    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

url = input("Enter the website URL: ")
search_webpage(url)
