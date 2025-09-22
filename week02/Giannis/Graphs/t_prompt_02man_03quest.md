# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Rxf7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qd3 | True | c3d3 | -150 cp |
| google/gemini-2.5-flash-lite | 3 | Qe4 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Bh7 | False | None | None |
| google/gemini-2.5-flash-lite | 5 | Bh6 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Qh3 | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Nxe5 | True | f3e5 | -255 cp |
| google/gemini-2.5-flash-lite | 8 | Qb3 | True | c3b3 | -509 cp |
| google/gemini-2.5-flash-lite | 9 | Qxh7 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Qe1 | True | c3e1 | -124 cp |
| openai/gpt-4.1-mini | 1 | Qc6 | True | c3c6 | -555 cp |
| openai/gpt-4.1-mini | 2 | Qxf6 | True | c3f6 | Mate in 1 |
| openai/gpt-4.1-mini | 3 | Qxc6 | True | c3c6 | -548 cp |
| openai/gpt-4.1-mini | 4 | Qxc6 | True | c3c6 | -574 cp |
| openai/gpt-4.1-mini | 5 | Qxc7 | True | c3c7 | -520 cp |
| openai/gpt-4.1-mini | 6 | Qc6 | True | c3c6 | -560 cp |
| openai/gpt-4.1-mini | 7 | Qc6 | True | c3c6 | -582 cp |
| openai/gpt-4.1-mini | 8 | Qxc6 | True | c3c6 | -586 cp |
| openai/gpt-4.1-mini | 9 | Qxc7 | True | c3c7 | -480 cp |
| openai/gpt-4.1-mini | 10 | Qxf6 | True | c3f6 | Mate in 1 |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | Qh6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Qxb5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | Rf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qxg4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | e5 | True | e4e5 | -379 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qxg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qc8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qxg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Qxg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qg5 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Nf3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qc8 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qh4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nh7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nh7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | SE | False | None | None |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -479 cp |
| qwen/qwen3-coder | 2 | Qe3 | True | c3e3 | -466 cp |
| qwen/qwen3-coder | 3 | Qe3 | True | c3e3 | -502 cp |
| qwen/qwen3-coder | 4 | Qe3 | True | c3e3 | -502 cp |
| qwen/qwen3-coder | 5 | Qe3 | True | c3e3 | -490 cp |
| qwen/qwen3-coder | 6 | Qe3 | True | c3e3 | -486 cp |
| qwen/qwen3-coder | 7 | Qe3 | True | c3e3 | -505 cp |
| qwen/qwen3-coder | 8 | Qe3 | True | c3e3 | -473 cp |
| qwen/qwen3-coder | 9 | Qe3 | True | c3e3 | -485 cp |
| qwen/qwen3-coder | 10 | Qe3 | True | c3e3 | -469 cp |
| meituan/longcat-flash-chat | 1 | Qc8 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qc8 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 5 | Axc6 | False | None | None |
| meituan/longcat-flash-chat | 6 | Axf7 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qxg7 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qxf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 1 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qxh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qxg6 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qxh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxg6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Be4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Bd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Bc5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Bd5 | False | None | None |