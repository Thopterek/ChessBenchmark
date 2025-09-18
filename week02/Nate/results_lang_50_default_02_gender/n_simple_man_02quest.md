# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Nxf7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qh7 | True | h6h7 | -482 cp |
| google/gemini-2.5-flash-lite | 3 | Qh7 | True | h6h7 | -494 cp |
| google/gemini-2.5-flash-lite | 4 | Qh7 | True | h6h7 | -524 cp |
| google/gemini-2.5-flash-lite | 5 | Qg7 | True | h6g7 | -651 cp |
| google/gemini-2.5-flash-lite | 6 | Qxh7 | True | h6h7 | -463 cp |
| google/gemini-2.5-flash-lite | 7 | Nxe7 | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Qh7 | True | h6h7 | -505 cp |
| google/gemini-2.5-flash-lite | 9 | Bh7 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Qh7 | True | h6h7 | -515 cp |
| openai/gpt-4.1-mini | 1 | Qh7 | True | h6h7 | -519 cp |
| openai/gpt-4.1-mini | 2 | Qh7 | True | h6h7 | -523 cp |
| openai/gpt-4.1-mini | 3 | Qg7 | True | h6g7 | -654 cp |
| openai/gpt-4.1-mini | 4 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-4.1-mini | 5 |  | False | None | None |
| openai/gpt-4.1-mini | 6 | Qh7 | True | h6h7 | -532 cp |
| openai/gpt-4.1-mini | 7 |  | False | None | None |
| openai/gpt-4.1-mini | 8 | Qh7 | True | h6h7 | -539 cp |
| openai/gpt-4.1-mini | 9 | Qh7 | True | h6h7 | -524 cp |
| openai/gpt-4.1-mini | 10 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Nxe6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qxf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qxf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Qh7 | True | h6h7 | -529 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Nf6 | True | d5f6 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 9 | Rh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qh7 | True | h6h7 | -506 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qxf7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nh3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qg4 | False | None | None |
| qwen/qwen3-coder | 1 | Qh7 | True | h6h7 | -519 cp |
| qwen/qwen3-coder | 2 | Qh7 | True | h6h7 | -537 cp |
| qwen/qwen3-coder | 3 | Qh7 | True | h6h7 | -536 cp |
| qwen/qwen3-coder | 4 | Qh7 | True | h6h7 | -528 cp |
| qwen/qwen3-coder | 5 | Qh8 | False | None | None |
| qwen/qwen3-coder | 6 | Qh7 | True | h6h7 | -526 cp |
| qwen/qwen3-coder | 7 | Qh7 | True | h6h7 | -490 cp |
| qwen/qwen3-coder | 8 | Qh7 | True | h6h7 | -517 cp |
| qwen/qwen3-coder | 9 | Qh7 | True | h6h7 | -502 cp |
| qwen/qwen3-coder | 10 | Qh7 | True | h6h7 | -533 cp |
| meituan/longcat-flash-chat | 1 | Ng8 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qh7 | True | h6h7 | -531 cp |
| meituan/longcat-flash-chat | 3 | Ng8 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qh7 | True | h6h7 | -542 cp |
| meituan/longcat-flash-chat | 5 | Qxh7 | True | h6h7 | -540 cp |
| meituan/longcat-flash-chat | 6 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qh7 | True | h6h7 | -542 cp |
| meituan/longcat-flash-chat | 9 | Nf7 | False | None | None |
| meituan/longcat-flash-chat | 10 | Nxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qxh7 | True | h6h7 | -549 cp |
| mistralai/mistral-medium-3.1 | 2 | Qxh7 | True | h6h7 | -515 cp |
| mistralai/mistral-medium-3.1 | 3 | Qxh7 | True | h6h7 | -520 cp |
| mistralai/mistral-medium-3.1 | 4 | Qxh7 | True | h6h7 | -529 cp |
| mistralai/mistral-medium-3.1 | 5 | Qxh7 | True | h6h7 | -519 cp |
| mistralai/mistral-medium-3.1 | 6 | Qxh7 | True | h6h7 | -526 cp |
| mistralai/mistral-medium-3.1 | 7 | Qxg7 | True | h6g7 | -602 cp |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | True | h6h7 | -555 cp |
| mistralai/mistral-medium-3.1 | 9 | Qxh7 | True | h6h7 | -542 cp |
| mistralai/mistral-medium-3.1 | 10 | Qxh7 | True | h6h7 | -526 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd3 | False | None | None |