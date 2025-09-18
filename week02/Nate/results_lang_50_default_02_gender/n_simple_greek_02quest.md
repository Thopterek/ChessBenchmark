# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qf7 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Nxe7 | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Nxf7 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Nf6 | True | d5f6 | Mate in 1 |
| google/gemini-2.5-flash-lite | 5 | Nf6 | True | d5f6 | Mate in 1 |
| google/gemini-2.5-flash-lite | 6 | Nxf6 | True | d5f6 | Mate in 1 |
| google/gemini-2.5-flash-lite | 7 | Nxf6 | True | d5f6 | Mate in 1 |
| google/gemini-2.5-flash-lite | 8 | Qxh7 | True | h6h7 | -496 cp |
| google/gemini-2.5-flash-lite | 9 | Nxf6 | True | d5f6 | Mate in 1 |
| google/gemini-2.5-flash-lite | 10 | Qg7 | True | h6g7 | -653 cp |
| openai/gpt-4.1-mini | 1 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-4.1-mini | 2 | Qh7 | True | h6h7 | -486 cp |
| openai/gpt-4.1-mini | 3 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-4.1-mini | 4 | Qh7 | True | h6h7 | -507 cp |
| openai/gpt-4.1-mini | 5 | Qxh7 | True | h6h7 | -498 cp |
| openai/gpt-4.1-mini | 6 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-4.1-mini | 7 | Nxf6 | True | d5f6 | Mate in 1 |
| openai/gpt-4.1-mini | 8 | Qxh7 | True | h6h7 | -529 cp |
| openai/gpt-4.1-mini | 9 | Qg7 | True | h6g7 | -597 cp |
| openai/gpt-4.1-mini | 10 | Qh7 | True | h6h7 | -527 cp |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | H5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qxh7 | True | h6h7 | -543 cp |
| deepseek/deepseek-chat-v3.1 | 4 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Rhg1 | True | h1g1 | 130 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| qwen/qwen3-coder | 1 | Qh7 | True | h6h7 | -524 cp |
| qwen/qwen3-coder | 2 | Qh7 | True | h6h7 | -531 cp |
| qwen/qwen3-coder | 3 | Qh7 | True | h6h7 | -529 cp |
| qwen/qwen3-coder | 4 | Qh7 | True | h6h7 | -528 cp |
| qwen/qwen3-coder | 5 | Qg7 | True | h6g7 | -636 cp |
| qwen/qwen3-coder | 6 | Qh7 | True | h6h7 | -532 cp |
| qwen/qwen3-coder | 7 | Qxf6 | False | None | None |
| qwen/qwen3-coder | 8 | Qe3 | True | h6e3 | -508 cp |
| qwen/qwen3-coder | 9 | Qh7 | True | h6h7 | -541 cp |
| qwen/qwen3-coder | 10 | Qh7 | True | h6h7 | -507 cp |
| meituan/longcat-flash-chat | 1 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qh7 | True | h6h7 | -524 cp |
| meituan/longcat-flash-chat | 3 | Ng8 | False | None | None |
| meituan/longcat-flash-chat | 4 | Nf7 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qh7 | True | h6h7 | -533 cp |
| meituan/longcat-flash-chat | 6 | Ng8-e7 | False | None | None |
| meituan/longcat-flash-chat | 7 | Ng5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 10 | Nxf7 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qxh7 | True | h6h7 | -527 cp |
| mistralai/mistral-medium-3.1 | 2 | Qxh7 | True | h6h7 | -534 cp |
| mistralai/mistral-medium-3.1 | 3 | Qxh7 | True | h6h7 | -534 cp |
| mistralai/mistral-medium-3.1 | 4 | Qxh7 | True | h6h7 | -495 cp |
| mistralai/mistral-medium-3.1 | 5 | Qxh7 | True | h6h7 | -534 cp |
| mistralai/mistral-medium-3.1 | 6 | Qxh7 | True | h6h7 | -539 cp |
| mistralai/mistral-medium-3.1 | 7 | Qxh7 | True | h6h7 | -548 cp |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | True | h6h7 | -501 cp |
| mistralai/mistral-medium-3.1 | 9 | Qxg7 | True | h6g7 | -640 cp |
| mistralai/mistral-medium-3.1 | 10 | Qxh7 | True | h6h7 | -538 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qd3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qe2 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qe3 | True | h6e3 | -509 cp |