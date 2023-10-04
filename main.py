"""
Erik Rutledge - 10/3/2023  - Pearagon Interview

"""

import requests
import json


def __main__():
    running = True
    while running:
        # Prompt user input
        user_input = input(str("\nPlease enter a book title or 'exit' to end: "))
        if user_input.lower() == "exit":
            running = False
        else:
            # Request data and parse response to JSON
            url = "https://ejditq67mwuzeuwrlp5fs3egwu0yhkjz.lambda-url.us-east-2.on.aws/api/books/search"
            payload = json.dumps({"title": user_input})
            headers = {'Content-Type': 'application/json'}
            response = requests.request("POST", url, headers=headers, data=payload) 
            # print(response.text)
            data = json.loads(response.text)

            if response.status_code == 200:
                # Print book information to console
                print(f"Title: {data['title']}")
                print(f"Description: {data['description']}")

                for author_id in data['authors']:
                    url = f"https://ejditq67mwuzeuwrlp5fs3egwu0yhkjz.lambda-url.us-east-2.on.aws/api/authors/{author_id}"
                    payload= {}
                    headers = {'Content-Type': 'application/json'}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    # print(response.text)
                    data = json.loads(response.text)
                    if 'middleInitial' in data:
                        full_name = f"{data['firstName']} {data['middleInitial']} {data['lastName']}"
                    else:
                        full_name = f"{data['firstName']} {data['lastName']}"
                    print(f"Author: {full_name}\n")

            else:
                print("\nBook not found, please try again.\n")


if __name__ == __main__():
    __main__()
