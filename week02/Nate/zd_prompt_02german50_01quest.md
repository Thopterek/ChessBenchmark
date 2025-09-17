# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh5 | True | d5h5 | -657 cp |
| google/gemini-2.5-flash-lite | 2 | Qg5 | True | d5g5 | 354 cp |
| google/gemini-2.5-flash-lite | 3 | Qh5 | True | d5h5 | -644 cp |
| google/gemini-2.5-flash-lite | 4 | Qb7 | True | d5b7 | 429 cp |
| google/gemini-2.5-flash-lite | 5 | Qf7 | True | d5f7 | -10 cp |
| google/gemini-2.5-flash-lite | 6 | Qh5 | True | d5h5 | -655 cp |
| google/gemini-2.5-flash-lite | 7 | Qg5 | True | d5g5 | 415 cp |
| google/gemini-2.5-flash-lite | 8 | Qg6 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Qh5 | True | d5h5 | -639 cp |
| google/gemini-2.5-flash-lite | 10 | Qh5 | True | d5h5 | -642 cp |
| openai/gpt-4.1-mini | 1 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 2 | Qxf7 | True | d5f7 | 10 cp |
| openai/gpt-4.1-mini | 3 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 4 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 5 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 6 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 7 | Qf7 | True | d5f7 | 12 cp |
| openai/gpt-4.1-mini | 8 | Qxf7 | True | d5f7 | 1 cp |
| openai/gpt-4.1-mini | 9 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 10 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-3.5-turbo-instruct | 1 | Qg5 | True | d5g5 | 423 cp |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | D4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Qg6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Rxe6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | Qg5 | True | d5g5 | 429 cp |
| deepseek/deepseek-chat-v3.1 | 1 | Qh5 | True | d5h5 | -625 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 |  | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Qe8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Rg3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qh5 | True | d5h5 | -627 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qd2 | True | d5d2 | 78 cp |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qd3 | True | d5d3 | 36 cp |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Qd3 | True | d5d3 | 28 cp |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qe3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qd3 | True | d5d3 | 50 cp |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qe3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qc4 | False | None | None |
| qwen/qwen3-coder | 1 | Qe5 | True | d5e5 | 269 cp |
| qwen/qwen3-coder | 2 | Qe6 | True | d5e6 | -643 cp |
| qwen/qwen3-coder | 3 | Qe3 | False | None | None |
| qwen/qwen3-coder | 4 | Qxg7 | False | None | None |
| qwen/qwen3-coder | 5 | Qe3 | False | None | None |
| qwen/qwen3-coder | 6 | Qe6 | True | d5e6 | -657 cp |
| qwen/qwen3-coder | 7 | Qe6 | True | d5e6 | -652 cp |
| qwen/qwen3-coder | 8 | Qxg7 | False | None | None |
| qwen/qwen3-coder | 9 | Qe6 | True | d5e6 | -659 cp |
| qwen/qwen3-coder | 10 | Qe6 | True | d5e6 | -629 cp |
| meituan/longcat-flash-chat | 1 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qh5 | True | d5h5 | -616 cp |
| meituan/longcat-flash-chat | 7 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qd5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qh5 | True | d5h5 | -628 cp |
| mistralai/mistral-medium-3.1 | 2 | Qh5 | True | d5h5 | -636 cp |
| mistralai/mistral-medium-3.1 | 3 | Qh5 | True | d5h5 | -633 cp |
| mistralai/mistral-medium-3.1 | 4 | Qh5 | True | d5h5 | -618 cp |
| mistralai/mistral-medium-3.1 | 5 | Qh5 | True | d5h5 | -633 cp |
| mistralai/mistral-medium-3.1 | 6 | Qh5 | True | d5h5 | -627 cp |
| mistralai/mistral-medium-3.1 | 7 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qh5 | True | d5h5 | -628 cp |
| mistralai/mistral-medium-3.1 | 9 | Qh5 | True | d5h5 | -628 cp |
| mistralai/mistral-medium-3.1 | 10 | Qh5 | True | d5h5 | -618 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd4 | True | d5d4 | 443 cp |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd4 | True | d5d4 | 464 cp |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd4 | True | d5d4 | 464 cp |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd4 | True | d5d4 | 446 cp |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd4 | True | d5d4 | 479 cp |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qb3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Nf3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd4 | True | d5d4 | 454 cp |