import requests
import os
from dotenv import load_dotenv
import csv

load_dotenv()
key = os.getenv("KEY")

i = 0

with open("../tests/test01.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if not row:
            continue
        question = row[0]
        answer = row[1]

        print("======================= Test N", i, "=======================")
        print("Q:", question)

        # start a new conversation
        messages = [
            {"role": "user", "content": [{"type": "text", "text": question}]}
        ]

        # first request
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}"},
            json={
                "model": "openai/gpt-3.5-turbo-instruct",
                "messages": messages
            }
        )

        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            content = result["choices"][0]["message"]["content"]
            print("Answer:", content)
            print("Real Answer:", answer)

            if answer == content:
                print("Correct")
                i += 1
            else:
                print("Incorrect")
                # add follow-up "Why?"
                messages.append({
                    "role": "user",
                    "content": [{"type": "text", "text": "Why is this the best move?"}]
                })

                # second request with follow-up
                followup = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={"Authorization": f"Bearer {key}"},
                    json={
                        "model": "openai/gpt-3.5-turbo-instruct",
                        "messages": messages
                    }
                )

                followup_result = followup.json()
                if "choices" in followup_result and len(followup_result["choices"]) > 0:
                    explanation = followup_result["choices"][0]["message"]["content"]
                    print("Follow-up (Why?):", explanation)
                else:
                    print("No follow-up content in response:", followup_result)

        else:
            print("No content in response:", result)

        print("========================================================")

