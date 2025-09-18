# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 |  | False | None | None |
| google/gemini-2.5-flash-lite | 2 |  | False | None | None |
| google/gemini-2.5-flash-lite | 3 |  | False | None | None |
| google/gemini-2.5-flash-lite | 4 |  | False | None | None |
| google/gemini-2.5-flash-lite | 5 |  | False | None | None |
| google/gemini-2.5-flash-lite | 6 |  | False | None | None |
| google/gemini-2.5-flash-lite | 7 |  | False | None | None |
| google/gemini-2.5-flash-lite | 8 |  | False | None | None |
| google/gemini-2.5-flash-lite | 9 |  | False | None | None |
| google/gemini-2.5-flash-lite | 10 |  | False | None | None |
| openai/gpt-4.1-mini | 1 | Qh7 | True | h6h7 | -482 cp |
| openai/gpt-4.1-mini | 2 | Qg7 | True | h6g7 | -625 cp |
| openai/gpt-4.1-mini | 3 | Qxh7 | True | h6h7 | -528 cp |
| openai/gpt-4.1-mini | 4 | Qg7 | True | h6g7 | -636 cp |
| openai/gpt-4.1-mini | 5 | Qh7 | True | h6h7 | -498 cp |
| openai/gpt-4.1-mini | 6 | Qxh7 | True | h6h7 | -523 cp |
| openai/gpt-4.1-mini | 7 | Qxh7 | True | h6h7 | -533 cp |
| openai/gpt-4.1-mini | 8 | Qxh7 | True | h6h7 | -532 cp |
| openai/gpt-4.1-mini | 9 | Qxh7 | True | h6h7 | -501 cp |
| openai/gpt-4.1-mini | 10 | Qh7 | True | h6h7 | -519 cp |
| openai/gpt-3.5-turbo-instruct | 1 | Re1 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | Rhe1 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | Nf6xg5 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | G2g7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Rg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Nxf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Dg6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Rxe5 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Dh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 8 | Rxf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Dg7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | N1e4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | SE | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | N2-O-O | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | N1c3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | N1f3 | False | None | None |
| qwen/qwen3-coder | 1 |  | False | None | None |
| qwen/qwen3-coder | 2 | Qg7 | True | h6g7 | -628 cp |
| qwen/qwen3-coder | 3 | Qg7 | True | h6g7 | -578 cp |
| qwen/qwen3-coder | 4 | h8 | False | None | None |
| qwen/qwen3-coder | 5 | Qg7 | True | h6g7 | -620 cp |
| qwen/qwen3-coder | 6 | Qg7 | True | h6g7 | -621 cp |
| qwen/qwen3-coder | 7 | Qg7 | True | h6g7 | -642 cp |
| qwen/qwen3-coder | 8 | Qg7 | True | h6g7 | -617 cp |
| qwen/qwen3-coder | 9 | Qg7 | True | h6g7 | -619 cp |
| qwen/qwen3-coder | 10 | Qg7 | True | h6g7 | -634 cp |
| meituan/longcat-flash-chat | 1 | Qxh7 | True | h6h7 | -522 cp |
| meituan/longcat-flash-chat | 2 | Rdf8 | False | None | None |
| meituan/longcat-flash-chat | 3 | Nxf5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Nf7 | False | None | None |
| meituan/longcat-flash-chat | 5 | Qg6 | False | None | None |
| meituan/longcat-flash-chat | 6 | O5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Nf7 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qxh7 | True | h6h7 | -517 cp |
| meituan/longcat-flash-chat | 9 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qh7 | True | h6h7 | -513 cp |
| mistralai/mistral-medium-3.1 | 1 | Nf6 | True | d5f6 | Mate in 1 |
| mistralai/mistral-medium-3.1 | 2 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 3 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 4 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 5 | Dxg7 | False | None | None |
| mistralai/mistral-medium-3.1 | 6 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 7 |  | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qxh7 | True | h6h7 | -522 cp |
| mistralai/mistral-medium-3.1 | 9 | Qxh7 | True | h6h7 | -544 cp |
| mistralai/mistral-medium-3.1 | 10 |  | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Re4-e5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | SE | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Re4-e5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Qh6 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | SE | False | None | None |