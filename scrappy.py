from bs4 import BeautifulSoup
import requests

url = "https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

question_title = soup.find('a', class_='question-hyperlink').get_text()
print(f"Question Title: {question_title}")

answers = soup.find_all('div', class_='answer')

print("Answers:")
for i, answer in enumerate(answers, 1):
    answer_text = answer.find('div', class_='s-prose js-post-body').get_text()
    print(f"Answer {i}:\n{answer_text.strip()}\n{'-'*50}\n")
