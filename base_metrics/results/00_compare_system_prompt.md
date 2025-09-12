
----
First System Prompt *prompt_02.txt* Chess Grand Master
----

|google/gemini-2.5-flash-lite|openai/gpt-4.1-mini|
|------------------------------|------------------------------|
|            Qg5#              |           Qg8                |
|            Ngf6+             |           Qg8                |
| Ig6 |  Qxf7 |
| Nf7 | Qxf7 |
| Nf7+ | Qxd8 |
| Nxe7 | Qxf7 |
| Ngf5 | Qh5 |
| Nhf7  | Qd8+ |
| Ng8-f7 | Qg8# |
| Nf7+ | Qxd8 |


---
Second System Prompt *prompt_01.txt* FIDA Rules of Chess
---

|google/gemini-2.5-flash-lite|openai/gpt-4.1-mini|
|------------------------------|------------------------------|
| Queen to H5 | Queen Moves to d8 |
| Rook Moves to E1 | Queen Moves to D8 |
|  Knight Moves to F7 | Queen moves to d8 |
| Queen to h5 | Queen Moves to D8 |
|  Rook Moves to E1 | Queen Moves to D8 |
| Knight Moves to F7 | Queen Moves to D8 |
| Bishop takes Knight | Queen moves to g8 |
| Knight to F7 | Queen Moves to D8 |
| Rook to E1 | Queen Moves to D8 | 
| Rook Moves to E1 | Queen Moves to D8 |

-----
Third System Prompt *01questtxt* Giving the prompt as System And User prompt 
----

| google/gemini-2.5-flash-lite | openai/gpt-4.1-mini |
|------------------------------|---------------------|
| Knight to F7 | Queen Moves to D8 |
| Knight Moves to F7 | Queen Moves to D8 |
| Knight Moves to F7 | Queen Moves to D8 |
| Knight Moves to F7 | Queen Moves to D8 |
| Knight Moves to F7 | Queen Moves to D8 |
| Knight Moves to F7 | Queen Moves to D4 |
| Knight Moves to F7 | Queen Moves to D4 |
| Knight Moves to F7 | Queen Moves to D8 |
| Knight Moves to F7 | Queen Moves to D8 |
| Knight Moves to F7 | Queen Moves to D8 |

---
Fourth System Prompt, Making the LLMs GODS of Chess **god_prompt.txt**
---

| google/gemini-2.5-flash-lite | openai/gpt-4.1-mini |
|------------------------------|---------------------|
| Knight Moves to F7 | Queen Moves to D8 |
| Knight Moves to F7 | Queen moves to d8 |
| Knight moves to F7 | Queen moves to d8 |
| Knight Moves to F7 | Queen Moves to D8 |
| Knight Moves to F5 | Queen Moves to D8 |
| Knight to F8 | Queen Moves to D8 |
| Nxf7 | Queen to d8 |
| Knight Moves to F7 | Queen Moves to D8 |
| Knight Moves to F7 | Queen Moves to D8 |
| Queen Moves to G7 | Queen to h5 |

---
Testing more models to find a pattern using the *prompt_02.txt* Chess Grandmaster
---
A. Models:
1. google/gemini-2.5-flash-lite
2. openai/gpt-4.1-mini
3. anthropic/claude-sonnet-4
4. openai/gpt-3.5-turbo-instruct
5. nvidia/nemotron-nano-9b-v2:free
6. deepseek/deepseek-chat-v3.1:free
7. meta-llama/llama-3.3-8b-instruct:free

B. Syntax errors (called SE in table), example:

- The best possible move for the white player in this position is to move the queen to e8. 
- This will put black in check and set up a mate in two if black moves their king to f7.
- Hello, I am the chess grandmaster assistant. 
- Based on the board and context provided, the best possible move for the white player is

C. Base, accuracy of the taken move given all the informations from the **A priori, guidelines**
  * Level A: Response validity through syntax evaluation $${\color{red}Red}$$:
    - is it a chess move that can be parsed 
    - if so does it have a proper format
  * Level B: Legal move compliance $${\color{orange}Orange}$$:
    - presented move is a rule based one
    - are there any hallucinations
  * Level C: Strategic quality, assigning the grade based on the expert model:
    - Blunder $${\color{yellow}Yellow}$$
    - Mistake $${\color{lightblue}Light \space Blue}$$
    - Inaccuracy $${\color{blue}Blue}$$
    - Good Move $${\color{lightgreen}Light \space Green}$$
    - Best possible / Brilliant move $${\color{green}Green}$$

| gemini-2.5-flash-lite | gpt-4.1-mini | claude-sonnet-4 | gpt-3.5-turbo-instruct | nemotron-nano-9b-v2 | deepseek-chat-v3.1 | llama-3.3-8b-instruct |
|---|---|---|---|---|---|---|
| Nhf7# | Qg8# | Qf7+ | $${\color{red}SE}$$ | Queen Moves to G5 | Qd5xf7 | Qd2
| Nf7+ | Qg8# | Qg8+ | $${\color{red}SE}$$ | $${\color{orange}Re8}$$ | $${\color{orange}Qd8}$$ | $${\color{orange}Qf3}$$
| Nhf7+ | Qxd8 | Qf7+ | Qe7 | rook moves to a8 | Qd8 | Nf3
| Nf7 | Qf7# | Qf7+ | $${\color{red}SE}$$ | Queen Moves to E3 | Qd8 | Qa3
| Nhf7 | Qxd8 | Qg8+ | $${\color{red}SE}$$ | Queen Moves to D5 | Qd8 | Nf3
| Nhf7 | Qg8# | Qd8+ | $${\color{red}SE}$$ | Queen Moves to H5 | Qd8 | Qd3
| Ng8 | Qxd8 | Qf7+ | $${\color{red}SE}$$ | Queen Moves to H6 | Qd8 | Nf3
| Qh5# | Qg8# | Qg8+ | $${\color{red}SE}$$ | Queen Moves to H1 | Qd8 | Nh2
| Nf7 | Qxf7# | Qf7+ | $${\color{red}SE}$$ | Queen Moves to H4 | Qd8 | Queen moves to E3
| Qh5 | Qg8# | Qxf7+ | Bc4 | Queen Moves to E3 | Qd8 | Qf3

---
ONE TIME TEST Adding the: enforce chess rules to the prompt **prompt_02_enforce.txt**
---

| gemini-2.5-flash-lite | gpt-4.1-mini | claude-sonnet-4 | gpt-3.5-turbo-instruct | nemotron-nano-9b-v2 | deepseek-chat-v3.1 | llama-3.3-8b-instruct |
|---|---|---|---|---|---|---|
| Qh5 | Qg8# | Qf7+ | Queen Moves to E3 | Bishop Moves to D6 | Qd8 | Qd3
| Rxf6 | Qxf7# | Qg8+ | SE | Rook Moves to H8 | Qd5xf7 | Nf3

