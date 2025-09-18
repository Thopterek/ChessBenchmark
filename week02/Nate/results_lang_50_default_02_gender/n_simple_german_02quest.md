# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Bh7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qh7 | True | h6h7 | -482 cp |
| google/gemini-2.5-flash-lite | 3 | Qh7 | True | h6h7 | -494 cp |
| google/gemini-2.5-flash-lite | 4 | Qh7 | True | h6h7 | -524 cp |
| google/gemini-2.5-flash-lite | 5 | Qh7 | True | h6h7 | -467 cp |
| google/gemini-2.5-flash-lite | 6 | Qh7 | True | h6h7 | -509 cp |
| google/gemini-2.5-flash-lite | 7 | Qg7 | True | h6g7 | -655 cp |
| google/gemini-2.5-flash-lite | 8 | Qg7 | True | h6g7 | -625 cp |
| google/gemini-2.5-flash-lite | 9 | Qg7 | True | h6g7 | -637 cp |
| google/gemini-2.5-flash-lite | 10 | Qh7 | True | h6h7 | -483 cp |
| openai/gpt-4.1-mini | 1 | Qh7 | True | h6h7 | -521 cp |
| openai/gpt-4.1-mini | 2 | Qh7 | True | h6h7 | -510 cp |
| openai/gpt-4.1-mini | 3 | Qg7 | True | h6g7 | -628 cp |
| openai/gpt-4.1-mini | 4 | Qg7 | True | h6g7 | -626 cp |
| openai/gpt-4.1-mini | 5 | Qxh7 | True | h6h7 | -519 cp |
| openai/gpt-4.1-mini | 6 | Qh7 | True | h6h7 | -528 cp |
| openai/gpt-4.1-mini | 7 | Qg7 | True | h6g7 | -622 cp |
| openai/gpt-4.1-mini | 8 | Qh7 | True | h6h7 | -530 cp |
| openai/gpt-4.1-mini | 9 | Qh7 | True | h6h7 | -536 cp |
| openai/gpt-4.1-mini | 10 | Qh7 | True | h6h7 | -548 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | Bd4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Rg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Rf8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qxh7 | True | h6h7 | -504 cp |
| deepseek/deepseek-chat-v3.1 | 4 | Qd6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qh7 | True | h6h7 | -523 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Qxf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qe3 | True | h6e3 | -453 cp |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nc3 | True | d5c3 | 221 cp |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nc3 | True | d5c3 | 249 cp |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Qe3 | True | h6e3 | -510 cp |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nh7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nc3 | True | d5c3 | 232 cp |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nc3 | True | d5c3 | 245 cp |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nc3 | True | d5c3 | 242 cp |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nc3 | True | d5c3 | 221 cp |
| qwen/qwen3-coder | 1 | Qh7 | True | h6h7 | -518 cp |
| qwen/qwen3-coder | 2 | Qh7 | True | h6h7 | -528 cp |
| qwen/qwen3-coder | 3 | Qh7 | True | h6h7 | -548 cp |
| qwen/qwen3-coder | 4 | Qh7 | True | h6h7 | -538 cp |
| qwen/qwen3-coder | 5 | Qh7 | True | h6h7 | -548 cp |
| qwen/qwen3-coder | 6 |  | False | None | None |
| qwen/qwen3-coder | 7 | Qh7 | True | h6h7 | -548 cp |
| qwen/qwen3-coder | 8 | Qh8 | False | None | None |
| qwen/qwen3-coder | 9 | Qh7 | True | h6h7 | -507 cp |
| qwen/qwen3-coder | 10 | Qh7 | True | h6h7 | -523 cp |
| meituan/longcat-flash-chat | 1 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qh7 | True | h6h7 | -537 cp |
| meituan/longcat-flash-chat | 6 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qh7 | True | h6h7 | -539 cp |
| meituan/longcat-flash-chat | 9 | Qh7 | True | h6h7 | -538 cp |
| meituan/longcat-flash-chat | 10 | Qh7 | True | h6h7 | -557 cp |
| mistralai/mistral-medium-3.1 | 1 | Qxh7 | True | h6h7 | -539 cp |
| mistralai/mistral-medium-3.1 | 2 | Qxh7 | True | h6h7 | -543 cp |
| mistralai/mistral-medium-3.1 | 3 | Qxh7 | True | h6h7 | -551 cp |
| mistralai/mistral-medium-3.1 | 4 | Qh7 | True | h6h7 | -548 cp |
| mistralai/mistral-medium-3.1 | 5 | Qh7 | True | h6h7 | -540 cp |
| mistralai/mistral-medium-3.1 | 6 | Qh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qxg7 | True | h6g7 | -636 cp |
| mistralai/mistral-medium-3.1 | 8 | Qh6 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qh7 | True | h6h7 | -534 cp |
| mistralai/mistral-medium-3.1 | 10 | Qh7 | True | h6h7 | -526 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qe3 | True | h6e3 | -504 cp |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qe3 | True | h6e3 | -506 cp |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qh5 | True | h6h5 | 83 cp |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qf6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qf4 | True | h6f4 | -569 cp |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qh5 | True | h6h5 | 95 cp |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Nf3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qh5 | True | h6h5 | 83 cp |