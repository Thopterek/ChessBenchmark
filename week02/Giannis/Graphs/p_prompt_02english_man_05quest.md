# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh7 | True | h5h7 | -464 cp |
| google/gemini-2.5-flash-lite | 2 | Qh6 | True | h5h6 | 195 cp |
| google/gemini-2.5-flash-lite | 3 | Qh6 | True | h5h6 | 161 cp |
| google/gemini-2.5-flash-lite | 4 | Qh6 | True | h5h6 | 164 cp |
| google/gemini-2.5-flash-lite | 5 | Qh6 | True | h5h6 | 191 cp |
| google/gemini-2.5-flash-lite | 6 | Qxh7 | True | h5h7 | -521 cp |
| google/gemini-2.5-flash-lite | 7 | Qh7 | True | h5h7 | -502 cp |
| google/gemini-2.5-flash-lite | 8 | Qh6 | True | h5h6 | 202 cp |
| google/gemini-2.5-flash-lite | 9 | Qh7 | True | h5h7 | -522 cp |
| google/gemini-2.5-flash-lite | 10 | Qh6 | True | h5h6 | 214 cp |
| openai/gpt-4.1-mini | 1 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 2 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 3 | Qh6 | True | h5h6 | 199 cp |
| openai/gpt-4.1-mini | 4 | Qh6 | True | h5h6 | 213 cp |
| openai/gpt-4.1-mini | 5 | Qh6 | True | h5h6 | 193 cp |
| openai/gpt-4.1-mini | 6 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 7 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 8 |  | False | None | None |
| openai/gpt-4.1-mini | 9 | Bxf7 | True | c4f7 | 0 cp |
| openai/gpt-4.1-mini | 10 | Qg7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | Qe3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Qe3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Rg2 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Rxe8 | True | e1e8 | -400 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qh6 | True | h5h6 | 199 cp |
| deepseek/deepseek-chat-v3.1 | 4 | c4 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qg6 | True | h5g6 | -647 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Qh6 | True | h5h6 | 185 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Bh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Rxe8 | True | e1e8 | -411 cp |
| deepseek/deepseek-chat-v3.1 | 10 | Qh8 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qg3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qd2 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Qg3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Qg4 | True | h5g4 | -507 cp |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Qg4 | True | h5g4 | -574 cp |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qf4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Qxd4 | False | None | None |
| qwen/qwen3-coder | 1 | Qxh7 | True | h5h7 | -542 cp |
| qwen/qwen3-coder | 2 | Qh7 | True | h5h7 | -546 cp |
| qwen/qwen3-coder | 3 | Qxh7 | True | h5h7 | -541 cp |
| qwen/qwen3-coder | 4 | Qxh7 | True | h5h7 | -535 cp |
| qwen/qwen3-coder | 5 | Qh7 | True | h5h7 | -555 cp |
| qwen/qwen3-coder | 6 | Qh6 | True | h5h6 | 196 cp |
| qwen/qwen3-coder | 7 | Qh7 | True | h5h7 | -525 cp |
| qwen/qwen3-coder | 8 | Qh7 | True | h5h7 | -531 cp |
| qwen/qwen3-coder | 9 | Qh7 | True | h5h7 | -506 cp |
| qwen/qwen3-coder | 10 | Qh7 | True | h5h7 | -533 cp |
| meituan/longcat-flash-chat | 1 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 2 | Qxh7 | True | h5h7 | -556 cp |
| meituan/longcat-flash-chat | 3 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qh7 | True | h5h7 | -565 cp |
| meituan/longcat-flash-chat | 5 | Qh7 | True | h5h7 | -539 cp |
| meituan/longcat-flash-chat | 6 | Qh7 | True | h5h7 | -554 cp |
| meituan/longcat-flash-chat | 7 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qh5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qxg6 | True | h5g6 | -639 cp |
| mistralai/mistral-medium-3.1 | 3 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qg8 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qf7 | True | h5f7 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 9 | Qxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qxg6 | True | h5g6 | -665 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qb3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qb3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qd4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qd4 | False | None | None |