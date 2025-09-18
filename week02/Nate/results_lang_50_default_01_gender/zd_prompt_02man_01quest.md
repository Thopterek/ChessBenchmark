# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qf7 | True | d5f7 | -2 cp |
| google/gemini-2.5-flash-lite | 2 | Nf7 | True | h6f7 | 590 cp |
| google/gemini-2.5-flash-lite | 3 | Qh7 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qxh7 | False | None | None |
| google/gemini-2.5-flash-lite | 5 | g6 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Ngf5 | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Nhf7 | True | h6f7 | Mate in 3 |
| google/gemini-2.5-flash-lite | 8 | Ng8 | True | h6g8 | -574 cp |
| google/gemini-2.5-flash-lite | 9 | Qg5 | True | d5g5 | 406 cp |
| google/gemini-2.5-flash-lite | 10 | Rhe1 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 2 | Qd8 | False | None | None |
| openai/gpt-4.1-mini | 3 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 4 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 5 | Qd8 | False | None | None |
| openai/gpt-4.1-mini | 6 | Qd8 | False | None | None |
| openai/gpt-4.1-mini | 7 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 8 | Qd8 | False | None | None |
| openai/gpt-4.1-mini | 9 |  | False | None | None |
| openai/gpt-4.1-mini | 10 | Qd8 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | Rg5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qc5 | True | d5c5 | -119 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qg8 | True | d5g8 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 3 | Qxe8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | e5 | True | e4e5 | -525 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Qf7 | True | d5f7 | 0 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Rf8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qxg4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qd8 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qg5 | True | d5g5 | 417 cp |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qxa7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qd1 | True | d5d1 | 376 cp |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Qxd5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qd5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qd2 | True | d5d2 | 137 cp |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qd2 | True | d5d2 | 87 cp |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qd2 | True | d5d2 | 97 cp |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qa5 | True | d5a5 | -68 cp |
| qwen/qwen3-coder | 1 | Qe6 | True | d5e6 | -681 cp |
| qwen/qwen3-coder | 2 | Qe6 | True | d5e6 | -662 cp |
| qwen/qwen3-coder | 3 | Qe6 | True | d5e6 | -647 cp |
| qwen/qwen3-coder | 4 | Qe6 | True | d5e6 | -651 cp |
| qwen/qwen3-coder | 5 | Qe3 | False | None | None |
| qwen/qwen3-coder | 6 | Qe6 | True | d5e6 | -658 cp |
| qwen/qwen3-coder | 7 | Qe6 | True | d5e6 | -655 cp |
| qwen/qwen3-coder | 8 | Qe6 | True | d5e6 | -648 cp |
| qwen/qwen3-coder | 9 | Qe6 | True | d5e6 | -675 cp |
| qwen/qwen3-coder | 10 | Qe3 | False | None | None |
| meituan/longcat-flash-chat | 1 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Ng5 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qd8 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qd5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qh5 | True | d5h5 | -618 cp |
| mistralai/mistral-medium-3.1 | 3 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxh7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd4 | True | d5d4 | 376 cp |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd4 | True | d5d4 | 436 cp |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd4 | True | d5d4 | 452 cp |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd4 | True | d5d4 | 450 cp |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Nxc7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd4 | True | d5d4 | 477 cp |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd4 | True | d5d4 | 471 cp |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Nf7 | True | h6f7 | Mate in 3 |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd4 | True | d5d4 | 481 cp |