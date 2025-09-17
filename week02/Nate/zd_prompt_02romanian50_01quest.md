# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 |  | False | None | None |
| google/gemini-2.5-flash-lite | 2 |  | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Qh5 | True | d5h5 | -657 cp |
| google/gemini-2.5-flash-lite | 4 | Nf7 | True | h6f7 | 593 cp |
| google/gemini-2.5-flash-lite | 5 |  | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Rf6 | False | None | None |
| google/gemini-2.5-flash-lite | 7 |  | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Nhf5 | True | h6f5 | -498 cp |
| google/gemini-2.5-flash-lite | 9 |  | False | None | None |
| google/gemini-2.5-flash-lite | 10 |  | False | None | None |
| openai/gpt-4.1-mini | 1 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 2 | Dxf7 | False | None | None |
| openai/gpt-4.1-mini | 3 | Qxf7 | True | d5f7 | -15 cp |
| openai/gpt-4.1-mini | 4 | Qxd8 | False | None | None |
| openai/gpt-4.1-mini | 5 | Qh5 | True | d5h5 | -638 cp |
| openai/gpt-4.1-mini | 6 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 7 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 8 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 9 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-4.1-mini | 10 | Qg8 | True | d5g8 | Mate in 1 |
| openai/gpt-3.5-turbo-instruct | 1 | E4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | Rfe8 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | E6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Domnul | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | e5 | True | e4e5 | -522 cp |
| openai/gpt-3.5-turbo-instruct | 10 |  | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qg6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qh5 | True | d5h5 | -611 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Dg8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qxh7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qh5 | True | d5h5 | -619 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Qh5 | True | d5h5 | -626 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Dd7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qh5 | True | d5h5 | -619 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Qh5 | True | d5h5 | -606 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | N1f3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | N1c3 | False | None | None |
| qwen/qwen3-coder | 1 | Qe5 | True | d5e5 | 214 cp |
| qwen/qwen3-coder | 2 |  | False | None | None |
| qwen/qwen3-coder | 3 | Qe3 | False | None | None |
| qwen/qwen3-coder | 4 | Qe3 | False | None | None |
| qwen/qwen3-coder | 5 |  | False | None | None |
| qwen/qwen3-coder | 6 | Df7 | False | None | None |
| qwen/qwen3-coder | 7 |  | False | None | None |
| qwen/qwen3-coder | 8 | Qe6 | True | d5e6 | -646 cp |
| qwen/qwen3-coder | 9 |  | False | None | None |
| qwen/qwen3-coder | 10 | Qe6 | True | d5e6 | -652 cp |
| meituan/longcat-flash-chat | 1 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 5 | Ng4 | True | h6g4 | -2 cp |
| meituan/longcat-flash-chat | 6 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Nf7 | True | h6f7 | 583 cp |
| meituan/longcat-flash-chat | 10 | Qd5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Dh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Dh7 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | D8h8 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 |  | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qe2 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qe2 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qb3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qe2 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Pe3茄 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Pe2-g2 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qe2 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Pe4-f6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qxf7 | True | d5f7 | -6 cp |