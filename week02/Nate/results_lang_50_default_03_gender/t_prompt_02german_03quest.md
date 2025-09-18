# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qxf7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Qh3 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 5 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Qf7 | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Bh5 | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Qg3 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Qg7 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Bh7 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qxf6 | True | c3f6 | Mate in 1 |
| openai/gpt-4.1-mini | 2 | Qxc7 | True | c3c7 | -528 cp |
| openai/gpt-4.1-mini | 3 | Qxc6 | True | c3c6 | -573 cp |
| openai/gpt-4.1-mini | 4 | Qc6 | True | c3c6 | -582 cp |
| openai/gpt-4.1-mini | 5 | Qxc6 | True | c3c6 | -559 cp |
| openai/gpt-4.1-mini | 6 | Qxc6 | True | c3c6 | -560 cp |
| openai/gpt-4.1-mini | 7 | Qxc6 | True | c3c6 | -555 cp |
| openai/gpt-4.1-mini | 8 | Qxc6 | True | c3c6 | -575 cp |
| openai/gpt-4.1-mini | 9 | Qxf6 | True | c3f6 | Mate in 1 |
| openai/gpt-4.1-mini | 10 | Qxc7 | True | c3c7 | -510 cp |
| openai/gpt-3.5-turbo-instruct | 1 | Qe3 | True | c3e3 | -463 cp |
| openai/gpt-3.5-turbo-instruct | 2 | D7-g8 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | Qe7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Qc8 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qd4 | True | c3d4 | -464 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qd4 | True | c3d4 | -448 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Nxf6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qd4 | True | c3d4 | -465 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Qh3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Bf6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qg6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qd4 | True | c3d4 | -449 cp |
| deepseek/deepseek-chat-v3.1 | 9 | Qh3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qd4 | True | c3d4 | -446 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qd2 | True | c3d2 | -178 cp |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qb3 | True | c3b3 | -472 cp |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qe3 | True | c3e3 | -487 cp |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qxd4 | True | c3d4 | -468 cp |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qd2 | True | c3d2 | -164 cp |
| qwen/qwen3-coder | 1 | Qe3 | True | c3e3 | -486 cp |
| qwen/qwen3-coder | 2 | Qe3 | True | c3e3 | -496 cp |
| qwen/qwen3-coder | 3 | Qe3 | True | c3e3 | -507 cp |
| qwen/qwen3-coder | 4 |  | False | None | None |
| qwen/qwen3-coder | 5 | Qe3 | True | c3e3 | -488 cp |
| qwen/qwen3-coder | 6 | Qe3 | True | c3e3 | -489 cp |
| qwen/qwen3-coder | 7 | Qe3 | True | c3e3 | -502 cp |
| qwen/qwen3-coder | 8 | Qe3 | True | c3e3 | -486 cp |
| qwen/qwen3-coder | 9 | Qe3 | True | c3e3 | -494 cp |
| qwen/qwen3-coder | 10 |  | False | None | None |
| meituan/longcat-flash-chat | 1 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qc7 | True | c3c7 | -495 cp |
| meituan/longcat-flash-chat | 4 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qc7 | True | c3c7 | -503 cp |
| meituan/longcat-flash-chat | 6 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qc3 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qc8 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qc5 | True | c3c5 | -621 cp |
| mistralai/mistral-medium-3.1 | 1 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qd6 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qd6 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 5 | Qf6 | True | c3f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 6 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qd6 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxh7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qa4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qf3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd4 | True | c3d4 | -465 cp |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd4 | True | c3d4 | -468 cp |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qe3 | True | c3e3 | -483 cp |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd4 | True | c3d4 | -471 cp |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd4 | True | c3d4 | -453 cp |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qe3 | True | c3e3 | -484 cp |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qe3 | True | c3e3 | -493 cp |