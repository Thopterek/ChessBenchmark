# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qh6 | False | None | None |
| google/gemini-2.5-flash-lite | 2 | Qg7 | True | h6g7 | -659 cp |
| google/gemini-2.5-flash-lite | 3 | Qh7 | True | h6h7 | -501 cp |
| google/gemini-2.5-flash-lite | 4 | Qg7 | True | h6g7 | -624 cp |
| google/gemini-2.5-flash-lite | 5 | Qh6 | False | None | None |
| google/gemini-2.5-flash-lite | 6 | Qg7 | True | h6g7 | -657 cp |
| google/gemini-2.5-flash-lite | 7 | Dh7 | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Qf7 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Sg7 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Qg7 | True | h6g7 | -625 cp |
| openai/gpt-4.1-mini | 1 | Qh7 | True | h6h7 | -514 cp |
| openai/gpt-4.1-mini | 2 | Qxh7 | True | h6h7 | -493 cp |
| openai/gpt-4.1-mini | 3 | Qg7 | True | h6g7 | -602 cp |
| openai/gpt-4.1-mini | 4 | Qh7 | True | h6h7 | -497 cp |
| openai/gpt-4.1-mini | 5 | Qg7 | True | h6g7 | -620 cp |
| openai/gpt-4.1-mini | 6 | Qxh7 | True | h6h7 | -517 cp |
| openai/gpt-4.1-mini | 7 | Qh7 | True | h6h7 | -499 cp |
| openai/gpt-4.1-mini | 8 | Qg7 | True | h6g7 | -618 cp |
| openai/gpt-4.1-mini | 9 | Qh7 | True | h6h7 | -486 cp |
| openai/gpt-4.1-mini | 10 | Qg7 | True | h6g7 | -636 cp |
| openai/gpt-3.5-turbo-instruct | 1 | Qg7 | True | h6g7 | -635 cp |
| openai/gpt-3.5-turbo-instruct | 2 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | B3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 |  | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Rxf6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | SE | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | SE | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qg7 | True | h6g7 | -631 cp |
| deepseek/deepseek-chat-v3.1 | 2 | Nf7 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qh6 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 6 | Rh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qxh7 | True | h6h7 | -506 cp |
| deepseek/deepseek-chat-v3.1 | 8 | Qh7 | True | h6h7 | -535 cp |
| deepseek/deepseek-chat-v3.1 | 9 | Qh8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qh6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nc6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nc6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nc6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nc4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nc6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nc6 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nc4 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nc3 | True | d5c3 | 233 cp |
| meta-llama/llama-3.3-8b-instruct:free | 10 | Nf3 | False | None | None |
| qwen/qwen3-coder | 1 | Qe3 | True | h6e3 | -516 cp |
| qwen/qwen3-coder | 2 | Qh7 | True | h6h7 | -509 cp |
| qwen/qwen3-coder | 3 | Qh7 | True | h6h7 | -518 cp |
| qwen/qwen3-coder | 4 | Qh7 | True | h6h7 | -517 cp |
| qwen/qwen3-coder | 5 | Qh7 | True | h6h7 | -511 cp |
| qwen/qwen3-coder | 6 | Qh7 | True | h6h7 | -538 cp |
| qwen/qwen3-coder | 7 |  | False | None | None |
| qwen/qwen3-coder | 8 | Qh7 | True | h6h7 | -505 cp |
| qwen/qwen3-coder | 9 | Qe3 | True | h6e3 | -488 cp |
| qwen/qwen3-coder | 10 | Qh7 | True | h6h7 | -520 cp |
| meituan/longcat-flash-chat | 1 | Qh7 | True | h6h7 | -503 cp |
| meituan/longcat-flash-chat | 2 | Qh7 | True | h6h7 | -528 cp |
| meituan/longcat-flash-chat | 3 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 4 | Qh7 | True | h6h7 | -543 cp |
| meituan/longcat-flash-chat | 5 | Qh6 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qh7 | True | h6h7 | -517 cp |
| meituan/longcat-flash-chat | 7 | Qh7 | True | h6h7 | -534 cp |
| meituan/longcat-flash-chat | 8 | Qh7 | True | h6h7 | -537 cp |
| meituan/longcat-flash-chat | 9 | Qh7 | True | h6h7 | -551 cp |
| meituan/longcat-flash-chat | 10 | Qh7 | True | h6h7 | -521 cp |
| mistralai/mistral-medium-3.1 | 1 | Qh7 | True | h6h7 | -532 cp |
| mistralai/mistral-medium-3.1 | 2 | Qh7 | True | h6h7 | -534 cp |
| mistralai/mistral-medium-3.1 | 3 | Qh7 | True | h6h7 | -545 cp |
| mistralai/mistral-medium-3.1 | 4 | Qh7 | True | h6h7 | -538 cp |
| mistralai/mistral-medium-3.1 | 5 | Qh7 | True | h6h7 | -545 cp |
| mistralai/mistral-medium-3.1 | 6 | Qh7 | True | h6h7 | -524 cp |
| mistralai/mistral-medium-3.1 | 7 | Qh7 | True | h6h7 | -537 cp |
| mistralai/mistral-medium-3.1 | 8 | Qh7 | True | h6h7 | -516 cp |
| mistralai/mistral-medium-3.1 | 9 | Qh7 | True | h6h7 | -515 cp |
| mistralai/mistral-medium-3.1 | 10 | Qh7 | True | h6h7 | -505 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | Nf7 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | Nf3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | Nd5 | False | None | None |