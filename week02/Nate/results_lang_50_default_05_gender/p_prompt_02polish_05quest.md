# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh3 | True | h5h3 | -401 cp |
| google/gemini-2.5-flash-lite | 2 | Qg6 | True | h5g6 | -643 cp |
| google/gemini-2.5-flash-lite | 3 | Qh5 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qh7 | True | h5h7 | -461 cp |
| google/gemini-2.5-flash-lite | 5 | Qh6 | True | h5h6 | 364 cp |
| google/gemini-2.5-flash-lite | 6 | Qh7 | True | h5h7 | -529 cp |
| google/gemini-2.5-flash-lite | 7 | Qh7 | True | h5h7 | -535 cp |
| google/gemini-2.5-flash-lite | 8 | Qh7 | True | h5h7 | -540 cp |
| google/gemini-2.5-flash-lite | 9 | Qh5 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Qh7 | True | h5h7 | -519 cp |
| openai/gpt-4.1-mini | 1 | Qxf7 | True | h5f7 | Mate in 1 |
| openai/gpt-4.1-mini | 2 | Qh6 | True | h5h6 | 375 cp |
| openai/gpt-4.1-mini | 3 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 4 | Qh6 | True | h5h6 | 381 cp |
| openai/gpt-4.1-mini | 5 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 6 | Qh6 | True | h5h6 | 374 cp |
| openai/gpt-4.1-mini | 7 | Qh6 | True | h5h6 | 363 cp |
| openai/gpt-4.1-mini | 8 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 9 | Bxf7 | True | c4f7 | 0 cp |
| openai/gpt-4.1-mini | 10 | Qxg7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | Qe3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | R1h4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | D5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Rd8 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Rh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qxf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 5 | Qh6 | True | h5h6 | 386 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Qxh7 | True | h5h7 | -521 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qxf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 9 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qh6 | True | h5h6 | 369 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nc4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nc6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qc4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nc6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| qwen/qwen3-coder | 1 | Qxh7 | True | h5h7 | -450 cp |
| qwen/qwen3-coder | 2 |  | False | None | None |
| qwen/qwen3-coder | 3 | Qxh7 | True | h5h7 | -522 cp |
| qwen/qwen3-coder | 4 | Qxh7 | True | h5h7 | -515 cp |
| qwen/qwen3-coder | 5 | Qxh7 | True | h5h7 | -519 cp |
| qwen/qwen3-coder | 6 | Qxh7 | True | h5h7 | -531 cp |
| qwen/qwen3-coder | 7 | Qxh7 | True | h5h7 | -530 cp |
| qwen/qwen3-coder | 8 |  | False | None | None |
| qwen/qwen3-coder | 9 | Qg6 | True | h5g6 | -640 cp |
| qwen/qwen3-coder | 10 | Qxh7 | True | h5h7 | -548 cp |
| meituan/longcat-flash-chat | 1 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qh6 | True | h5h6 | 367 cp |
| meituan/longcat-flash-chat | 4 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qh6 | True | h5h6 | 377 cp |
| meituan/longcat-flash-chat | 8 | Qh7 | True | h5h7 | -544 cp |
| meituan/longcat-flash-chat | 9 | Qh7 | True | h5h7 | -546 cp |
| meituan/longcat-flash-chat | 10 | Qh5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qh7 | True | h5h7 | -456 cp |
| mistralai/mistral-medium-3.1 | 2 | Qh7 | True | h5h7 | -534 cp |
| mistralai/mistral-medium-3.1 | 3 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qh7 | True | h5h7 | -554 cp |
| mistralai/mistral-medium-3.1 | 9 | Qh7 | True | h5h7 | -555 cp |
| mistralai/mistral-medium-3.1 | 10 | Qh8 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qf3 | True | h5f3 | -28 cp |