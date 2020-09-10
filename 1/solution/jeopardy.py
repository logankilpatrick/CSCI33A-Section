import requests

url = "http://jservice.io/api/random"

def display_question(question):
    print("Category: " + question["category"]["title"])
    print("Q: " + question["question"])
    ans = input("Your Answer: ")
    print("A: " + question["answer"])
    if ans.lower() == question["answer"].lower():
        print("CORRECT!\n")
    else:
        print("INCORRECT\n")


while True:
    random_question = requests.get(url).json()[0]
    display_question(random_question)