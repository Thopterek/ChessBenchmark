# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qg3 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qc7 | True | c3c7 | -522 cp |
| google/gemini-2.5-flash-lite | 3 | Nc3 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qxe4 | False | None | None |
| google/gemini-2.5-flash-lite | 5 | Qg3 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Qe7 | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Qg3 | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Qb3 | True | c3b3 | -524 cp |
| google/gemini-2.5-flash-lite | 9 | Qf7 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Nhf4 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qh8 | False | None | None |
| openai/gpt-4.1-mini | 2 | Qe5 | True | c3e5 | -532 cp |
| openai/gpt-4.1-mini | 3 | Qxc7 | True | c3c7 | -522 cp |
| openai/gpt-4.1-mini | 4 | Qxc7 | True | c3c7 | -511 cp |
| openai/gpt-4.1-mini | 5 |  | False | None | None |
| openai/gpt-4.1-mini | 6 | Qxc7 | True | c3c7 | -497 cp |
| openai/gpt-4.1-mini | 7 |  | False | None | None |
| openai/gpt-4.1-mini | 8 | Qxc7 | True | c3c7 | -528 cp |
| openai/gpt-4.1-mini | 9 | Qxc7 | True | c3c7 | -519 cp |
| openai/gpt-4.1-mini | 10 | Qxc7 | True | c3c7 | -517 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Nf4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Qh4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | Qd7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qd4 | True | c3d4 | -443 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qc6 | True | c3c6 | -558 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qg3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qd4 | True | c3d4 | -477 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Qc6 | True | c3c6 | -564 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Bd6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Bc5 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Rh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Rf1e1 | True | f1e1 | 108 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Qxg7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qg3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qg3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qd2 | True | c3d2 | -199 cp |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qxg8 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qd3 | True | c3d3 | -159 cp |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nh2 | False | None | None |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -503 cp |
| qwen/qwen3-coder | 2 | Qe3 | True | c3e3 | -455 cp |
| qwen/qwen3-coder | 3 | Qe3 | True | c3e3 | -470 cp |
| qwen/qwen3-coder | 4 | Qe3 | True | c3e3 | -487 cp |
| qwen/qwen3-coder | 5 | Qe3 | True | c3e3 | -461 cp |
| qwen/qwen3-coder | 6 | Qe3 | True | c3e3 | -492 cp |
| qwen/qwen3-coder | 7 | Qe3 | True | c3e3 | -480 cp |
| qwen/qwen3-coder | 8 | Qe3 | True | c3e3 | -494 cp |
| qwen/qwen3-coder | 9 | Qe3 | True | c3e3 | -488 cp |
| qwen/qwen3-coder | 10 | Qe3 | True | c3e3 | -472 cp |
| meituan/longcat-flash-chat | 1 | Axg6 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qc8 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qc7 | True | c3c7 | -500 cp |
| meituan/longcat-flash-chat | 4 | Qc7 | True | c3c7 | -519 cp |
| meituan/longcat-flash-chat | 5 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qxg7 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 9 | Ng1-e2 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qxh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qxh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qxh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qxh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qxh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxg6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd4 | True | c3d4 | -449 cp |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Bd5 | False | None | None |