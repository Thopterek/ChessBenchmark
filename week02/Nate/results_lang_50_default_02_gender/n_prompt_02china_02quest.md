# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qxf7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qf6 | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Qf6 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qxh7 | True | h6h7 | -482 cp |
| google/gemini-2.5-flash-lite | 5 | Qg7 | True | h6g7 | -625 cp |
| google/gemini-2.5-flash-lite | 6 | Qxh7 | True | h6h7 | -528 cp |
| google/gemini-2.5-flash-lite | 7 | Qxh7 | True | h6h7 | -526 cp |
| google/gemini-2.5-flash-lite | 8 | Qxh7 | True | h6h7 | -500 cp |
| google/gemini-2.5-flash-lite | 9 | Qh7 | True | h6h7 | -518 cp |
| google/gemini-2.5-flash-lite | 10 | Qxf7 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qxh7 | True | h6h7 | -510 cp |
| openai/gpt-4.1-mini | 2 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-4.1-mini | 3 | Nh6 | False | None | None |
| openai/gpt-4.1-mini | 4 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-4.1-mini | 5 | Qh7 | True | h6h7 | -521 cp |
| openai/gpt-4.1-mini | 6 | Qxh7 | True | h6h7 | -505 cp |
| openai/gpt-4.1-mini | 7 | Qg7 | True | h6g7 | -645 cp |
| openai/gpt-4.1-mini | 8 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-4.1-mini | 9 | Qg7 | True | h6g7 | -637 cp |
| openai/gpt-4.1-mini | 10 | Qh7 | True | h6h7 | -532 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | Qe3 | True | h6e3 | -472 cp |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | 选择走法：Qe3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Rg1 | True | h1g1 | 171 cp |
| deepseek/deepseek-chat-v3.1 | 2 | f4 | True | f2f4 | 137 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qxh7 | True | h6h7 | -523 cp |
| deepseek/deepseek-chat-v3.1 | 4 | Rhg1 | True | h1g1 | 177 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Rd1 | True | a1d1 | 178 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Rg1 | True | h1g1 | 161 cp |
| deepseek/deepseek-chat-v3.1 | 8 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Rg1 | True | h1g1 | 221 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Qh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qg4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nh3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nh4 | True | g6h4 | 333 cp |
| qwen/qwen3-coder | 1 | Qg7 | True | h6g7 | -642 cp |
| qwen/qwen3-coder | 2 | Qe3 | True | h6e3 | -491 cp |
| qwen/qwen3-coder | 3 | Qh7 | True | h6h7 | -529 cp |
| qwen/qwen3-coder | 4 | Qxh7 | True | h6h7 | -519 cp |
| qwen/qwen3-coder | 5 |  | False | None | None |
| qwen/qwen3-coder | 6 | Qh7 | True | h6h7 | -534 cp |
| qwen/qwen3-coder | 7 | Qh7 | True | h6h7 | -521 cp |
| qwen/qwen3-coder | 8 | Qh7 | True | h6h7 | -530 cp |
| qwen/qwen3-coder | 9 | Qh8 | False | None | None |
| qwen/qwen3-coder | 10 | Qxh7 | True | h6h7 | -519 cp |
| meituan/longcat-flash-chat | 1 | Nf6 | True | d5f6 | Mate in 1 |
| meituan/longcat-flash-chat | 2 | Nxf7 | False | None | None |
| meituan/longcat-flash-chat | 3 | Nh5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qh7 | True | h6h7 | -545 cp |
| meituan/longcat-flash-chat | 5 | Nf7 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qh7 | True | h6h7 | -536 cp |
| meituan/longcat-flash-chat | 8 | Ng5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qh7 | True | h6h7 | -515 cp |
| meituan/longcat-flash-chat | 10 | Qh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 2 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 3 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qxh7 | True | h6h7 | -536 cp |
| mistralai/mistral-medium-3.1 | 5 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 6 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 7 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxg7 | True | h6g7 | -641 cp |
| mistralai/mistral-medium-3.1 | 9 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 10 |  | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qh6 | False | None | None |