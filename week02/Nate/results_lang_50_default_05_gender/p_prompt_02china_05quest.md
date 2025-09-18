# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qg8 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qxh7 | True | h5h7 | -464 cp |
| google/gemini-2.5-flash-lite | 3 | Qg6 | True | h5g6 | -634 cp |
| google/gemini-2.5-flash-lite | 4 | Qh6 | True | h5h6 | 206 cp |
| google/gemini-2.5-flash-lite | 5 | Qxh7 | True | h5h7 | -505 cp |
| google/gemini-2.5-flash-lite | 6 | Qh6 | True | h5h6 | 204 cp |
| google/gemini-2.5-flash-lite | 7 | Qh6 | True | h5h6 | 184 cp |
| google/gemini-2.5-flash-lite | 8 | Qh6 | True | h5h6 | 165 cp |
| google/gemini-2.5-flash-lite | 9 | Qh6 | True | h5h6 | 182 cp |
| google/gemini-2.5-flash-lite | 10 | Qh6 | True | h5h6 | 207 cp |
| openai/gpt-4.1-mini | 1 | Qh6 | True | h5h6 | 191 cp |
| openai/gpt-4.1-mini | 2 | Bxf7 | True | c4f7 | 0 cp |
| openai/gpt-4.1-mini | 3 | Qh6 | True | h5h6 | 204 cp |
| openai/gpt-4.1-mini | 4 | Qh6 | True | h5h6 | 193 cp |
| openai/gpt-4.1-mini | 5 | Qh6 | True | h5h6 | 191 cp |
| openai/gpt-4.1-mini | 6 | Qxf7 | True | h5f7 | Mate in 1 |
| openai/gpt-4.1-mini | 7 | Qxf7 | True | h5f7 | Mate in 1 |
| openai/gpt-4.1-mini | 8 | Bxf7 | True | c4f7 | 0 cp |
| openai/gpt-4.1-mini | 9 | Qh6 | True | h5h6 | 193 cp |
| openai/gpt-4.1-mini | 10 | Bxf7 | True | c4f7 | 0 cp |
| openai/gpt-3.5-turbo-instruct | 1 | 白方应着：Qe3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | 我的答案是Qa6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | 白方最佳应着：Qe3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | 白方应着：Qe3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Re8 | True | e1e8 | -369 cp |
| deepseek/deepseek-chat-v3.1 | 3 | Qg6 | True | h5g6 | -646 cp |
| deepseek/deepseek-chat-v3.1 | 4 | Qg6 | True | h5g6 | -652 cp |
| deepseek/deepseek-chat-v3.1 | 5 | Rd1 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Qxh7 | True | h5h7 | -540 cp |
| deepseek/deepseek-chat-v3.1 | 7 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Qxf7 | True | h5f7 | Mate in 1 |
| deepseek/deepseek-chat-v3.1 | 10 | Rxe7 | True | e1e7 | -520 cp |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Qxf7 | True | h5f7 | Mate in 1 |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Qg3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Qg4 | True | h5g4 | -514 cp |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nxd5 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Qg4 | True | h5g4 | -497 cp |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Qg4 | True | h5g4 | -511 cp |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Qg5 | True | h5g5 | -123 cp |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| qwen/qwen3-coder | 1 | Qh6 | True | h5h6 | 193 cp |
| qwen/qwen3-coder | 2 | Qxh7 | True | h5h7 | -524 cp |
| qwen/qwen3-coder | 3 | Qh7 | True | h5h7 | -534 cp |
| qwen/qwen3-coder | 4 | Qh8 | False | None | None |
| qwen/qwen3-coder | 5 | Qe3 | False | None | None |
| qwen/qwen3-coder | 6 | Qxh7 | True | h5h7 | -545 cp |
| qwen/qwen3-coder | 7 | Qe8 | False | None | None |
| qwen/qwen3-coder | 8 | Qxh7 | True | h5h7 | -546 cp |
| qwen/qwen3-coder | 9 | Qxh7 | True | h5h7 | -556 cp |
| qwen/qwen3-coder | 10 | Qxh7 | True | h5h7 | -558 cp |
| meituan/longcat-flash-chat | 1 | Bg5 | True | f6g5 | -223 cp |
| meituan/longcat-flash-chat | 2 | Qh6 | True | h5h6 | 176 cp |
| meituan/longcat-flash-chat | 3 | Qh7 | True | h5h7 | -559 cp |
| meituan/longcat-flash-chat | 4 | Qh7 | True | h5h7 | -567 cp |
| meituan/longcat-flash-chat | 5 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Bg5 | True | f6g5 | -206 cp |
| meituan/longcat-flash-chat | 9 | Qh7 | True | h5h7 | -567 cp |
| meituan/longcat-flash-chat | 10 | Qh6 | True | h5h6 | 191 cp |
| mistralai/mistral-medium-3.1 | 1 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 2 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 3 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qh8 | False | None | None |
| mistralai/mistral-medium-3.1 | 9 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 10 | Qh8 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qh5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qh5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Qh5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Qh5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Qh5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Qh5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qh5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Qh5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qh5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Qh5 | False | None | None |