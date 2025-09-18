# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qh6 | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Qh6 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Nf7 | True | h6f7 | 616 cp |
| google/gemini-2.5-flash-lite | 5 | Qh6 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Qh6 | False | None | None |
| google/gemini-2.5-flash-lite | 7 | Qh6 | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Qf7 | True | d5f7 | 0 cp |
| google/gemini-2.5-flash-lite | 9 | Qh5 | True | d5h5 | -625 cp |
| google/gemini-2.5-flash-lite | 10 | json | False | None | None |
| openai/gpt-4.1-mini | 1 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 2 | Qxd8 | False | None | None |
| openai/gpt-4.1-mini | 3 | Qh5 | True | d5h5 | -642 cp |
| openai/gpt-4.1-mini | 4 | Qd8 | False | None | None |
| openai/gpt-4.1-mini | 5 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 6 | Qh5 | True | d5h5 | -639 cp |
| openai/gpt-4.1-mini | 7 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 8 | Qh5 | True | d5h5 | -647 cp |
| openai/gpt-4.1-mini | 9 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 10 | Qd8 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Qf7 | True | d5f7 | 0 cp |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | Qf4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qe8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qd4 | True | d5d4 | 460 cp |
| deepseek/deepseek-chat-v3.1 | 4 | Qf7 | True | d5f7 | 20 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Qg8 | True | d5g8 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 6 | Qe5 | True | d5e5 | 263 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Rf8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Rd7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qxg8 | True | d5g8 | Mate in 1 |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qf4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qg5 | True | d5g5 | 410 cp |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Qxd5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qxf7 | True | d5f7 | 0 cp |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qg4 | False | None | None |
| qwen/qwen3-coder | 1 | Qe3 | False | None | None |
| qwen/qwen3-coder | 2 | Qe3 | False | None | None |
| qwen/qwen3-coder | 3 | Qe6 | True | d5e6 | -671 cp |
| qwen/qwen3-coder | 4 | Qe3 | False | None | None |
| qwen/qwen3-coder | 5 | Qe6 | True | d5e6 | -665 cp |
| qwen/qwen3-coder | 6 | Qe6 | True | d5e6 | -643 cp |
| qwen/qwen3-coder | 7 | Qe6 | True | d5e6 | -657 cp |
| qwen/qwen3-coder | 8 | Qe6 | True | d5e6 | -672 cp |
| qwen/qwen3-coder | 9 | Qe5 | True | d5e5 | 272 cp |
| qwen/qwen3-coder | 10 | Qe3 | False | None | None |
| meituan/longcat-flash-chat | 1 | Qxd5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Ngxf7 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Ng8 | True | h6g8 | -565 cp |
| meituan/longcat-flash-chat | 5 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qd8 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qd5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qg8 | True | d5g8 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 2 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qh5 | True | d5h5 | -617 cp |
| mistralai/mistral-medium-3.1 | 5 | Qh5 | True | d5h5 | -627 cp |
| mistralai/mistral-medium-3.1 | 6 | Qh5 | True | d5h5 | -633 cp |
| mistralai/mistral-medium-3.1 | 7 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qd8 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qh5 | True | d5h5 | -643 cp |
| mistralai/mistral-medium-3.1 | 10 | Qxh7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd4 | True | d5d4 | 437 cp |
| baidu/ernie-4.5-vl-28b-a3b | 2 | NdB5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd4 | True | d5d4 | 437 cp |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd4 | True | d5d4 | 472 cp |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd3 | True | d5d3 | 48 cp |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd4 | True | d5d4 | 467 cp |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd4 | True | d5d4 | 471 cp |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd4 | True | d5d4 | 474 cp |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd4 | True | d5d4 | 433 cp |