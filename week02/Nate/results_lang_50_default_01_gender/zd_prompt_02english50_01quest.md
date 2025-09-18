# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qxh7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qg5 | True | d5g5 | 430 cp |
| google/gemini-2.5-flash-lite | 3 | Qxh7 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Nhf7 | True | h6f7 | Mate in 3 |
| google/gemini-2.5-flash-lite | 5 | Qf7 | True | d5f7 | -22 cp |
| google/gemini-2.5-flash-lite | 6 | Qh6 | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Qxf7 | True | d5f7 | -1 cp |
| google/gemini-2.5-flash-lite | 8 | Qxh7 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Qh6 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Hg6 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 2 | Qf7 | True | d5f7 | 14 cp |
| openai/gpt-4.1-mini | 3 | Qxd8 | False | None | None |
| openai/gpt-4.1-mini | 4 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 5 | Qh5 | True | d5h5 | -646 cp |
| openai/gpt-4.1-mini | 6 | Qd8 | False | None | None |
| openai/gpt-4.1-mini | 7 | Qf6 | False | None | None |
| openai/gpt-4.1-mini | 8 | Qh5 | True | d5h5 | -640 cp |
| openai/gpt-4.1-mini | 9 | Qh5 | True | d5h5 | -631 cp |
| openai/gpt-4.1-mini | 10 | Qd4 | True | d5d4 | 400 cp |
| openai/gpt-3.5-turbo-instruct | 1 | Qh6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | Qe3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | D5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qh5 | True | d5h5 | -623 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qg8 | True | d5g8 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 3 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qe6 | True | d5e6 | -650 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Qd7 | True | d5d7 | -545 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Rxf8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qf7 | True | d5f7 | 39 cp |
| deepseek/deepseek-chat-v3.1 | 8 | Rf8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qh5 | True | d5h5 | -623 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Qd6 | True | d5d6 | 93 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qd2 | True | d5d2 | 91 cp |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qd2 | True | d5d2 | 93 cp |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qxf7 | True | d5f7 | 19 cp |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qxd5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qd2 | True | d5d2 | 89 cp |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qd2 | True | d5d2 | 110 cp |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nh3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qd2 | True | d5d2 | 106 cp |
| qwen/qwen3-coder | 1 | Qe3 | False | None | None |
| qwen/qwen3-coder | 2 | Qxg7 | False | None | None |
| qwen/qwen3-coder | 3 | Qe3 | False | None | None |
| qwen/qwen3-coder | 4 | Qe6 | True | d5e6 | -655 cp |
| qwen/qwen3-coder | 5 | Qe6 | True | d5e6 | -653 cp |
| qwen/qwen3-coder | 6 | Qg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 7 | Qxh7 | False | None | None |
| qwen/qwen3-coder | 8 | Qe6 | True | d5e6 | -652 cp |
| qwen/qwen3-coder | 9 | Qe3 | False | None | None |
| qwen/qwen3-coder | 10 | Qe6 | True | d5e6 | -659 cp |
| meituan/longcat-flash-chat | 1 | Qxd5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qg8 | True | d5g8 | Mate in 1 |
| meituan/longcat-flash-chat | 3 | Qf7 | True | d5f7 | 14 cp |
| meituan/longcat-flash-chat | 4 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qh5 | True | d5h5 | -630 cp |
| meituan/longcat-flash-chat | 7 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qd8 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qd5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 2 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 5 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qh5 | True | d5h5 | -634 cp |
| mistralai/mistral-medium-3.1 | 7 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 10 |  | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd4 | True | d5d4 | 450 cp |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd4 | True | d5d4 | 451 cp |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd3 | True | d5d3 | 47 cp |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd4 | True | d5d4 | 454 cp |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd4 | True | d5d4 | 472 cp |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd3 | True | d5d3 | 54 cp |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd4 | True | d5d4 | 480 cp |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd3 | True | d5d3 | 47 cp |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd4 | True | d5d4 | 441 cp |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Nf7 | True | h6f7 | 604 cp |