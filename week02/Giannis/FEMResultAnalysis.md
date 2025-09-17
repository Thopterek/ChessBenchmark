#PROMPT

8  .  .  .  .  .  .  Q  .
7  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  K  .
3  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .
1  .  .  .  .  .  k  .  .
   a  b  c  d  e  f  g  h

Create the FEN notation for the board

#Findings
Only Claude sonnet 4 could actually translate it to FEN.

---

#PROMPT

White king is at g4
Black king is at f1
White Queen is at g8

Create me the FEN notation for the board

#Findings
Claude and gpt 4.1 mini seams to understand and create the FEN accurately.

---

#PROMPT

Considering the FEN notation of this match: 6Q1/8/8/8/6K1/8/8/5k2 w - - 0 1
I want you to list every active piece and its location

#SystemPrompt

You are a chess GRANDMASTER.

You are helpful to answer everything considering chess.
ALWAYS THINK about the answer.
Just answer with the positions of the pieces


#Findings

|gemini2.5|gpt 4.1 | claude 4 | gpt 3.5 | nvidia | deepseek-chat-v3.1:free | llama-3.3-8b-instruct:free |
|---------|--------|----------|---------|--------|-------------------------|----------------------------|
| No response | OK | OK | ko | OK | OK | ko |


___

## Previous PROMPT in steroids

Only change: FEN 3qr2k/pbpp2pp/1p5N/3Q4/2P1P1b1/P7/1PP2PPP/R3RK2 b - - 0 1

## Findings

|gemini2.5|gpt 4.1 | claude 4 | gpt 3.5 | nvidia | deepseek-chat-v3.1:free | llama-3.3-8b-instruct:free |
|---------|--------|----------|---------|--------|-------------------------|----------------------------|
| No response | ko | ko | ko | ko | ko | ko |


---


## Previous PROMPT with BUZZWORDS SystemPrompt

|gemini2.5|gpt 4.1 | claude 4 | gpt 3.5 | nvidia | deepseek-chat-v3.1:free | llama-3.3-8b-instruct:free |
|---------|--------|----------|---------|--------|-------------------------|----------------------------| 
| ko | ko | OK | ko | ko | ko | ko |


## EASY PROMPT with BUZZWORDS SystemPrompt
|gemini2.5|gpt 4.1 | claude 4 | gpt 3.5 | nvidia | deepseek-chat-v3.1:free | llama-3.3-8b-instruct:free |
|---------|--------|----------|---------|--------|-------------------------|----------------------------|  
| ko | OK | OK | ko | OK | ko | ko |


## Same exact thing include Nates Findings about temperature at 0.3 yields concistand and better results
|gemini2.5|gpt 4.1 | claude 4 | gpt 3.5 | nvidia | deepseek-chat-v3.1:free | llama-3.3-8b-instruct:free |
|---------|--------|----------|---------|--------|-------------------------|----------------------------|
| ko | OK | OK | ko | ko | OK | ko |

---

# TESTING THE BIG BOYS WITH EASY PROMPT

|grok-code-fast-1|claude-sonnet-4|gemini-2.5-flash|gpt-4.1-mini|gemini-2.5-pro|deepseek-chat-v3-0324|gpt-5|deepseek-chat-v3.1|qwen3-coder|llama-3.3-70b-instruct|
|---|---|---|---|---|---|---|---|---|---|
|OK|OK|OK|OK|OK|OK|OK|OK|OK|ko|


# TESTING THE BIG BOYS WITH HARD PROMPT
## Caviats
  1.
|grok-code-fast-1|claude-sonnet-4|gemini-2.5-flash|gpt-4.1-mini|gemini-2.5-pro|deepseek-chat-v3-0324|gpt-5|deepseek-chat-v3.1|qwen3-coder|llama-3.3-70b-instruct|
|---|---|---|---|---|---|---|---|---|---|
|OK|ko|ko|ko|OK|
