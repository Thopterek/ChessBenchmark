# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 |  | False | None | None |
| google/gemini-2.5-flash-lite | 2 |  | False | None | None |
| google/gemini-2.5-flash-lite | 3 |  | False | None | None |
| google/gemini-2.5-flash-lite | 4 |  | False | None | None |
| google/gemini-2.5-flash-lite | 5 |  | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Qh6 | True | h5h6 | 175 cp |
| google/gemini-2.5-flash-lite | 7 |  | False | None | None |
| google/gemini-2.5-flash-lite | 8 |  | False | None | None |
| google/gemini-2.5-flash-lite | 9 |  | False | None | None |
| google/gemini-2.5-flash-lite | 10 |  | False | None | None |
| openai/gpt-4.1-mini | 1 | Qh6 | True | h5h6 | 389 cp |
| openai/gpt-4.1-mini | 2 | Qh6 | True | h5h6 | 374 cp |
| openai/gpt-4.1-mini | 3 | Qh6 | True | h5h6 | 385 cp |
| openai/gpt-4.1-mini | 4 | Qg7 | False | None | None |
| openai/gpt-4.1-mini | 5 | Qh6 | True | h5h6 | 381 cp |
| openai/gpt-4.1-mini | 6 | Qg7 | False | None | None |
| openai/gpt-4.1-mini | 7 | Qh6 | True | h5h6 | 385 cp |
| openai/gpt-4.1-mini | 8 | Qh6 | True | h5h6 | 381 cp |
| openai/gpt-4.1-mini | 9 | Dh6 | False | None | None |
| openai/gpt-4.1-mini | 10 | Qg7 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | E7-E3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | Dxe6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | E2-E4 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | D5-H5 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qg6 | True | h5g6 | -606 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Rxf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Dh3 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Rh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Rxf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Rxf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qxf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 8 | Dg6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Rf8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Dg5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | B2-B7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | N2-O-O | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Ne1 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | N1f3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | B2-B7 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | N1c3 | False | None | None |
| qwen/qwen3-coder | 1 | Qh7 | True | h5h7 | -478 cp |
| qwen/qwen3-coder | 2 | Qh7 | True | h5h7 | -529 cp |
| qwen/qwen3-coder | 3 | Dh5-g6 | False | None | None |
| qwen/qwen3-coder | 4 | Qg6 | True | h5g6 | -665 cp |
| qwen/qwen3-coder | 5 | Qh7 | True | h5h7 | -505 cp |
| qwen/qwen3-coder | 6 |  | False | None | None |
| qwen/qwen3-coder | 7 |  | False | None | None |
| qwen/qwen3-coder | 8 | Qh6 | True | h5h6 | 386 cp |
| qwen/qwen3-coder | 9 | Qxh7 | True | h5h7 | -502 cp |
| qwen/qwen3-coder | 10 | Qg6 | True | h5g6 | -623 cp |
| meituan/longcat-flash-chat | 1 | Qh7 | True | h5h7 | -548 cp |
| meituan/longcat-flash-chat | 2 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 3 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qxh7 | True | h5h7 | -533 cp |
| meituan/longcat-flash-chat | 5 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qh7 | True | h5h7 | -520 cp |
| meituan/longcat-flash-chat | 7 | Qh7 | True | h5h7 | -537 cp |
| meituan/longcat-flash-chat | 8 | SE | False | None | None |
| meituan/longcat-flash-chat | 9 | Qh7 | True | h5h7 | -546 cp |
| meituan/longcat-flash-chat | 10 | Qh5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | D8h8 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qh6 | True | h5h6 | 381 cp |
| mistralai/mistral-medium-3.1 | 8 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qh8 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qe6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qh5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Re2 | True | e1e2 | -345 cp |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qi5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qf5 | True | h5f5 | 32 cp |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qe6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Re2 | True | e1e2 | -375 cp |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qxf7 | True | h5f7 | Mate in 1 |
| baidu/ernie-4.5-vl-28b-a3b | 9 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Re2-e4 | False | None | None |