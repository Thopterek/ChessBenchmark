# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 5 | Qg3 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Qg1 | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Rg1 | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Qxe4 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Qg3 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qxc7 | True | c3c7 | -522 cp |
| openai/gpt-4.1-mini | 2 | Qxc7 | True | c3c7 | -499 cp |
| openai/gpt-4.1-mini | 3 | Qb4 | True | c3b4 | -277 cp |
| openai/gpt-4.1-mini | 4 | Qxc7 | True | c3c7 | -516 cp |
| openai/gpt-4.1-mini | 5 | Qxc7 | True | c3c7 | -493 cp |
| openai/gpt-4.1-mini | 6 | Qxc6 | True | c3c6 | -539 cp |
| openai/gpt-4.1-mini | 7 | Qxc7 | True | c3c7 | -497 cp |
| openai/gpt-4.1-mini | 8 | Qc7 | True | c3c7 | -505 cp |
| openai/gpt-4.1-mini | 9 | Qxc7 | True | c3c7 | -509 cp |
| openai/gpt-4.1-mini | 10 | Qxc7 | True | c3c7 | -505 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Qxd6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Rd1 | True | f1d1 | -230 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qxf6 | True | c3f6 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 3 | Rd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qxf6 | True | c3f6 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 5 | Qxg4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Qxf6 | True | c3f6 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 7 | Qxg4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qg3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qxg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qd4 | True | c3d4 | -456 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nh4 | True | f3h4 | -287 cp |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nc6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nc6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nc5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nh5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nc6 | False | None | None |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -502 cp |
| qwen/qwen3-coder | 2 | Qe3 | True | c3e3 | -521 cp |
| qwen/qwen3-coder | 3 | Qe3 | True | c3e3 | -496 cp |
| qwen/qwen3-coder | 4 | Qe3 | True | c3e3 | -514 cp |
| qwen/qwen3-coder | 5 | Qe3 | True | c3e3 | -490 cp |
| qwen/qwen3-coder | 6 | Qe3 | True | c3e3 | -481 cp |
| qwen/qwen3-coder | 7 | Qe3 | True | c3e3 | -483 cp |
| qwen/qwen3-coder | 8 |  | False | None | None |
| qwen/qwen3-coder | 9 | Qe3 | True | c3e3 | -498 cp |
| qwen/qwen3-coder | 10 | Qe3 | True | c3e3 | -498 cp |
| meituan/longcat-flash-chat | 1 | Qc8 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qf3 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qc7 | True | c3c7 | -503 cp |
| meituan/longcat-flash-chat | 4 | Qc8 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qxc6 | True | c3c6 | -569 cp |
| meituan/longcat-flash-chat | 6 | Ng5 | True | f3g5 | -299 cp |
| meituan/longcat-flash-chat | 7 | Qc7 | True | c3c7 | -522 cp |
| meituan/longcat-flash-chat | 8 | Qc7 | True | c3c7 | -508 cp |
| meituan/longcat-flash-chat | 9 | Qc8 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qa5 | True | c3a5 | -467 cp |
| mistralai/mistral-medium-3.1 | 1 | Qf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 2 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 5 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxf7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Be2 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qa4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qe3 | True | c3e3 | -491 cp |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Be3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Bg5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Be2 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Nb3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Be3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Bd4 | False | None | None |