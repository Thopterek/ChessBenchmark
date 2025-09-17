# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Sg6 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qh5 | True | d5h5 | -657 cp |
| google/gemini-2.5-flash-lite | 3 | Qf5 | True | d5f5 | 374 cp |
| google/gemini-2.5-flash-lite | 4 | Qf7 | True | d5f7 | -3 cp |
| google/gemini-2.5-flash-lite | 5 | Qh5 | True | d5h5 | -641 cp |
| google/gemini-2.5-flash-lite | 6 | Qh5 | True | d5h5 | -636 cp |
| google/gemini-2.5-flash-lite | 7 | Qh5 | True | d5h5 | -633 cp |
| google/gemini-2.5-flash-lite | 8 | Qh5 | True | d5h5 | -632 cp |
| google/gemini-2.5-flash-lite | 9 | Qf7 | True | d5f7 | 34 cp |
| google/gemini-2.5-flash-lite | 10 | Qh5 | True | d5h5 | -626 cp |
| openai/gpt-4.1-mini | 1 | Ngf7 | False | None | None |
| openai/gpt-4.1-mini | 2 | Qh5 | True | d5h5 | -633 cp |
| openai/gpt-4.1-mini | 3 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 4 | Qf6 | False | None | None |
| openai/gpt-4.1-mini | 5 | Nhf7 | True | h6f7 | Mate in 3 |
| openai/gpt-4.1-mini | 6 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 7 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 8 | Qxf7 | True | d5f7 | 17 cp |
| openai/gpt-4.1-mini | 9 | Qxd8 | False | None | None |
| openai/gpt-4.1-mini | 10 | Qxf7 | True | d5f7 | 39 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | F4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | D4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | D4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Qe6 | True | d5e6 | -646 cp |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qf7 | True | d5f7 | 45 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qh5 | True | d5h5 | -621 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Qh5 | True | d5h5 | -621 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Qh5 | True | d5h5 | -628 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Qe8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qh5 | True | d5h5 | -627 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Qf7 | True | d5f7 | 37 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qg5 | True | d5g5 | 420 cp |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qc3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qd2 | True | d5d2 | 89 cp |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nc4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qc4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nh3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nc4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qd3 | True | d5d3 | 67 cp |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qc4 | False | None | None |
| qwen/qwen3-coder | 1 | Qxg7 | False | None | None |
| qwen/qwen3-coder | 2 | Qe6 | True | d5e6 | -639 cp |
| qwen/qwen3-coder | 3 | Qe6 | True | d5e6 | -647 cp |
| qwen/qwen3-coder | 4 | Qe3 | False | None | None |
| qwen/qwen3-coder | 5 | Qe6 | True | d5e6 | -659 cp |
| qwen/qwen3-coder | 6 | Qe6 | True | d5e6 | -639 cp |
| qwen/qwen3-coder | 7 | Qe6 | True | d5e6 | -642 cp |
| qwen/qwen3-coder | 8 | Qxg7 | False | None | None |
| qwen/qwen3-coder | 9 | Qe6 | True | d5e6 | -644 cp |
| qwen/qwen3-coder | 10 | Qe6 | True | d5e6 | -640 cp |
| meituan/longcat-flash-chat | 1 | Qg5 | True | d5g5 | 420 cp |
| meituan/longcat-flash-chat | 2 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qd8 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qd8 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qd5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qh5 | True | d5h5 | -609 cp |
| mistralai/mistral-medium-3.1 | 3 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qh5 | True | d5h5 | -620 cp |
| mistralai/mistral-medium-3.1 | 7 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qh5 | True | d5h5 | -635 cp |
| mistralai/mistral-medium-3.1 | 9 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qh5 | True | d5h5 | -632 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qe3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd4 | True | d5d4 | 434 cp |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd4 | True | d5d4 | 447 cp |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd4 | True | d5d4 | 447 cp |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd4 | True | d5d4 | 426 cp |