# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Rxf6 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qg4 | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Bh7 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qxh7 | False | None | None |
| google/gemini-2.5-flash-lite | 5 | Nfg5 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Bh7 | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Rh8 | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Qh5 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Bh5 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Qh7 | False | None | None |
| openai/gpt-4.1-mini | 1 | Nh6 | False | None | None |
| openai/gpt-4.1-mini | 2 | Nh6 | False | None | None |
| openai/gpt-4.1-mini | 3 | Nf6 | False | None | None |
| openai/gpt-4.1-mini | 4 | Nh6 | False | None | None |
| openai/gpt-4.1-mini | 5 | Nh6 | False | None | None |
| openai/gpt-4.1-mini | 6 |  | False | None | None |
| openai/gpt-4.1-mini | 7 | Nh6 | False | None | None |
| openai/gpt-4.1-mini | 8 | Qh6 | False | None | None |
| openai/gpt-4.1-mini | 9 | Qg8 | False | None | None |
| openai/gpt-4.1-mini | 10 | Nh6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | Nf6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | Nf5 | True | g7f5 | Mate in 3 |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qd2 | True | d1d2 | 321 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qd2 | True | d1d2 | 312 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Rf8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Rh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Nh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Nf5 | True | g7f5 | Mate in 3 |
| deepseek/deepseek-chat-v3.1 | 8 | Qg4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qd8 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Qg3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nh6 | False | None | None |
| qwen/qwen3-coder | 1 | Qh5 | False | None | None |
| qwen/qwen3-coder | 2 | Qh5 | False | None | None |
| qwen/qwen3-coder | 3 | Qh5 | False | None | None |
| qwen/qwen3-coder | 4 | Qh5 | False | None | None |
| qwen/qwen3-coder | 5 | Qh5 | False | None | None |
| qwen/qwen3-coder | 6 | Qh5 | False | None | None |
| qwen/qwen3-coder | 7 | Qh5 | False | None | None |
| qwen/qwen3-coder | 8 | Qh5 | False | None | None |
| qwen/qwen3-coder | 9 | Qh5 | False | None | None |
| qwen/qwen3-coder | 10 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 1 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Ng5 | False | None | None |
| meituan/longcat-flash-chat | 3 | Ng5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Ng5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Bf6 | False | None | None |
| meituan/longcat-flash-chat | 9 | Bf6 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qd5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxh7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Bd5 | True | e6d5 | -167 cp |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Ndb3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Nf7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Nf7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Bd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Nf3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Ne4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Nf3 | False | None | None |