# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh7 | True | h6h7 | -482 cp |
| google/gemini-2.5-flash-lite | 2 | Qxh7 | True | h6h7 | -494 cp |
| google/gemini-2.5-flash-lite | 3 | Qxh7 | True | h6h7 | -524 cp |
| google/gemini-2.5-flash-lite | 4 | Qh7 | True | h6h7 | -467 cp |
| google/gemini-2.5-flash-lite | 5 | Qxh7 | True | h6h7 | -509 cp |
| google/gemini-2.5-flash-lite | 6 | Qh7 | True | h6h7 | -507 cp |
| google/gemini-2.5-flash-lite | 7 | Qh7 | True | h6h7 | -506 cp |
| google/gemini-2.5-flash-lite | 8 | Qg7 | True | h6g7 | -615 cp |
| google/gemini-2.5-flash-lite | 9 | Qh7 | True | h6h7 | -506 cp |
| google/gemini-2.5-flash-lite | 10 | Qf6 | False | None | None |
| openai/gpt-4.1-mini | 1 | Qh7 | True | h6h7 | -511 cp |
| openai/gpt-4.1-mini | 2 | Qg7 | True | h6g7 | -590 cp |
| openai/gpt-4.1-mini | 3 | Nxf7 | False | None | None |
| openai/gpt-4.1-mini | 4 | Qg7 | True | h6g7 | -621 cp |
| openai/gpt-4.1-mini | 5 | Qxh7 | True | h6h7 | -527 cp |
| openai/gpt-4.1-mini | 6 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-4.1-mini | 7 | Qh7 | True | h6h7 | -528 cp |
| openai/gpt-4.1-mini | 8 | Qg7 | True | h6g7 | -641 cp |
| openai/gpt-4.1-mini | 9 | Nxh7 | False | None | None |
| openai/gpt-4.1-mini | 10 | Qh7 | True | h6h7 | -519 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | Qh6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | Qd8 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Nxe5 | True | g6e5 | 328 cp |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Nxe5 | True | g6e5 | 344 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Nf4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qg7 | True | h6g7 | -633 cp |
| deepseek/deepseek-chat-v3.1 | 4 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Ndf6 | True | d5f6 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 7 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Rxf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qxh7 | True | h6h7 | -514 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Nf7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qd2 | True | h6d2 | -172 cp |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qh4 | True | h6h4 | -97 cp |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qxf7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nh7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| qwen/qwen3-coder | 1 | Qh7 | True | h6h7 | -542 cp |
| qwen/qwen3-coder | 2 | Qh7 | True | h6h7 | -533 cp |
| qwen/qwen3-coder | 3 | Qh7 | True | h6h7 | -532 cp |
| qwen/qwen3-coder | 4 | Qh7 | True | h6h7 | -547 cp |
| qwen/qwen3-coder | 5 | Qg7 | True | h6g7 | -617 cp |
| qwen/qwen3-coder | 6 | Qe3 | True | h6e3 | -487 cp |
| qwen/qwen3-coder | 7 | Qe3 | True | h6e3 | -521 cp |
| qwen/qwen3-coder | 8 | Qxf6 | False | None | None |
| qwen/qwen3-coder | 9 | Qh7 | True | h6h7 | -538 cp |
| qwen/qwen3-coder | 10 | Qg7 | True | h6g7 | -635 cp |
| meituan/longcat-flash-chat | 1 | Qh7 | True | h6h7 | -535 cp |
| meituan/longcat-flash-chat | 2 | Ngxf7 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qh7 | True | h6h7 | -543 cp |
| meituan/longcat-flash-chat | 4 | Ng8 | False | None | None |
| meituan/longcat-flash-chat | 5 | Ng8 | False | None | None |
| meituan/longcat-flash-chat | 6 | Ng8 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 9 | Ng8 | False | None | None |
| meituan/longcat-flash-chat | 10 | Ng8-e7 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qxh7 | True | h6h7 | -537 cp |
| mistralai/mistral-medium-3.1 | 2 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 3 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 4 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 5 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 6 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qxh7 | True | h6h7 | -543 cp |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | True | h6h7 | -523 cp |
| mistralai/mistral-medium-3.1 | 9 | Qxh7 | True | h6h7 | -548 cp |
| mistralai/mistral-medium-3.1 | 10 |  | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd3 | False | None | None |