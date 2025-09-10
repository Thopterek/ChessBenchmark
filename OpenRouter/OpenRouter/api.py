#
# import requests
# import json
# import os
# from dotenv import load_dotenv
# import csv
#
# load_dotenv()
# key = os.getenv("KEY")
#
# i = 0
#
#
# with open("../tests/test.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if not row:
#             continue
#         question = row[0]
#         answer = row[1]
#
#         print("=======================Test N",i, "=======================")
#         print(question)
#
#         # Keep conversation history
#         messages = [
#             {"role": "user", "content": [{"type": "text", "text": question}]}
#         ]
#
#         response = requests.post(
#         url="https://openrouter.ai/api/v1/chat/completions",
#         headers={
#             "Authorization": f"Bearer {key}",
#         },
#         data=json.dumps({
#             "model": "anthropic/claude-sonnet-4",
#             "messages": [
#             {
#                 "role": "user",
#                 "content": question
#                 }
#             ]
#         })
#         )
#         result = response.json()
#         if "choices" in result and len(result["choices"]) > 0:
#             content = result["choices"][0]["message"]["content"]
#             # content = result["choices"][0]["message"]["content"][0]["text"]
#             print("Answer:", content)
#             print("Real Answer:", answer)
#             if answer == content:
#                 print("True")
#                 i += 1
#                 continue
#             else:
#                 print("False")
#                 messages.append({"role": "user", 
#                                 "content": [{"type": "text", "text": "Why?"}]
#                                 })
#         else:
#             print("No content in response:", result)
#         print("========================================================")

import requests
import os
from dotenv import load_dotenv
import csv

load_dotenv()
key = os.getenv("KEY")

i = 0

with open("../tests/test.csv", "r") as file:
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
                "model": "anthropic/claude-sonnet-4",
                "messages": messages
            }
        )

        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            content = result["choices"][0]["message"]["content"]
            print("Answer:", content)
            print("Real Answer:", answer)

            if answer == content:
                print("✅ Correct")
                i += 1
            else:
                print("❌ Incorrect")
                # add follow-up "Why?"
                messages.append({
                    "role": "user",
                    "content": [{"type": "text", "text": "Why?"}]
                })

                # second request with follow-up
                followup = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={"Authorization": f"Bearer {key}"},
                    json={
                        "model": "anthropic/claude-sonnet-4",
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
            print("⚠️ No content in response:", result)

        print("========================================================")

