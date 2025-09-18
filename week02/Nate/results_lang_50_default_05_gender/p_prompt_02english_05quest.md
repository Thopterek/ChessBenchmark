# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh6 | True | h5h6 | 175 cp |
| google/gemini-2.5-flash-lite | 2 | Qh6 | True | h5h6 | 389 cp |
| google/gemini-2.5-flash-lite | 3 | Qxh7 | True | h5h7 | -420 cp |
| google/gemini-2.5-flash-lite | 4 | Qh6 | True | h5h6 | 363 cp |
| google/gemini-2.5-flash-lite | 5 | Qh6 | True | h5h6 | 371 cp |
| google/gemini-2.5-flash-lite | 6 | Qh6 | True | h5h6 | 375 cp |
| google/gemini-2.5-flash-lite | 7 | Qxh7 | True | h5h7 | -456 cp |
| google/gemini-2.5-flash-lite | 8 | Qh6 | True | h5h6 | 357 cp |
| google/gemini-2.5-flash-lite | 9 | Qh6 | True | h5h6 | 372 cp |
| google/gemini-2.5-flash-lite | 10 | Qh6 | True | h5h6 | 368 cp |
| openai/gpt-4.1-mini | 1 | Qh6 | True | h5h6 | 387 cp |
| openai/gpt-4.1-mini | 2 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 3 | Qxh7 | True | h5h7 | -456 cp |
| openai/gpt-4.1-mini | 4 | Qg7 | False | None | None |
| openai/gpt-4.1-mini | 5 | Qh6 | True | h5h6 | 382 cp |
| openai/gpt-4.1-mini | 6 | Qg7 | False | None | None |
| openai/gpt-4.1-mini | 7 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 8 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 9 | Qh6 | True | h5h6 | 372 cp |
| openai/gpt-4.1-mini | 10 | Qxg7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | Qc7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qh5 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 3 | Bh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Rxe8 | True | e1e8 | -377 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Qh6 | True | h5h6 | 376 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Rfe1 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qd1 | True | h5d1 | -367 cp |
| deepseek/deepseek-chat-v3.1 | 8 | Qxg6 | True | h5g6 | -625 cp |
| deepseek/deepseek-chat-v3.1 | 9 | Qxf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 10 | Rxe8 | True | e1e8 | -412 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nh5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qf4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Qa3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qg4 | True | h5g4 | -588 cp |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nh7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qxd5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qd2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| qwen/qwen3-coder | 1 | Qh7 | True | h5h7 | -524 cp |
| qwen/qwen3-coder | 2 | Qxh7 | True | h5h7 | -522 cp |
| qwen/qwen3-coder | 3 | Qh7 | True | h5h7 | -536 cp |
| qwen/qwen3-coder | 4 | Qh6 | True | h5h6 | 381 cp |
| qwen/qwen3-coder | 5 | Qxh7 | True | h5h7 | -526 cp |
| qwen/qwen3-coder | 6 | Qxh7 | True | h5h7 | -511 cp |
| qwen/qwen3-coder | 7 | Qh7 | True | h5h7 | -525 cp |
| qwen/qwen3-coder | 8 | Qxh7 | True | h5h7 | -556 cp |
| qwen/qwen3-coder | 9 | Qh7 | True | h5h7 | -515 cp |
| qwen/qwen3-coder | 10 | Qh7 | True | h5h7 | -553 cp |
| meituan/longcat-flash-chat | 1 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qh7 | True | h5h7 | -545 cp |
| meituan/longcat-flash-chat | 4 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qh5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 4 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 5 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 10 |  | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd4 | False | None | None |