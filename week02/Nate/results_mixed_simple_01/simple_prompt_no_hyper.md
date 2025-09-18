# Chess Move Prediction Results with Legality & Stockfish Eval

| Model | Call # | Move | Legal | UCI | Eval |
|-------|--------|------|-------|-----|------|
| google/gemini-2.5-flash-lite | 1 | Qxd4 | True | d5d4 | -237 cp |
| google/gemini-2.5-flash-lite | 2 | Qe3 | False | None | None |
| google/gemini-2.5-flash-lite | 3 | Qh5 | False | None | None |
| google/gemini-2.5-flash-lite | 4 | Qd3 | True | d5d3 | -215 cp |
| google/gemini-2.5-flash-lite | 5 | Qxd4 | True | d5d4 | -237 cp |
| google/gemini-2.5-flash-lite | 6 | Qxe5 | True | d5e5 | -263 cp |
| google/gemini-2.5-flash-lite | 7 | Qd4xd4 | False | None | None |
| google/gemini-2.5-flash-lite | 8 | Bh4 | False | None | None |
| google/gemini-2.5-flash-lite | 9 | Rg1 | False | None | None |
| google/gemini-2.5-flash-lite | 10 | Qxd4 | True | d5d4 | -242 cp |
| openai/gpt-4.1-mini | 1 | Qxd8 | False | None | None |
| openai/gpt-4.1-mini | 2 | Qxf6 | False | None | None |
| openai/gpt-4.1-mini | 3 | Qxf6 | False | None | None |
| openai/gpt-4.1-mini | 4 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 5 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 6 | Qxg7 | False | None | None |
| openai/gpt-4.1-mini | 7 | Qxf7 | True | d5f7 | -247 cp |
| openai/gpt-4.1-mini | 8 | Qd4xf6 | False | None | None |
| openai/gpt-4.1-mini | 9 | Qxf6 | False | None | None |
| openai/gpt-4.1-mini | 10 | Qxf6 | False | None | None |
| anthropic/claude-sonnet-4 | 1 | Qd8 | False | None | None |
| anthropic/claude-sonnet-4 | 2 | Qd8 | False | None | None |
| anthropic/claude-sonnet-4 | 3 | Qd8 | False | None | None |
| anthropic/claude-sonnet-4 | 4 | Qd8 | False | None | None |
| anthropic/claude-sonnet-4 | 5 | Nf7 | True | h6f7 | 569 cp |
| anthropic/claude-sonnet-4 | 6 | Qd8 | False | None | None |
| anthropic/claude-sonnet-4 | 7 | Qd8 | False | None | None |
| anthropic/claude-sonnet-4 | 8 | Qd8 | False | None | None |
| anthropic/claude-sonnet-4 | 9 | Qd8 | False | None | None |
| anthropic/claude-sonnet-4 | 10 | Qd8 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 1 | Your move should be "Qd5" to capture the black bishop. | False | None | None |
| openai/gpt-3.5-turbo-instruct | 2 | Based on your current board state, I would suggest the following move: "Qd4". This move benefits white by putting pressure on the black queen and potentially winning a piece. | False | None | None |
| openai/gpt-3.5-turbo-instruct | 3 | The best move would be Qd2. | False | None | None |
| openai/gpt-3.5-turbo-instruct | 4 | Based on the board state, the best move for White would be "Qd8", as it would allow the queen to attack the black king and force Black to respond. | False | None | None |
| openai/gpt-3.5-turbo-instruct | 5 | The best move for white is to move the queen to d3, capturing the black bishop at g6. This move would increase white's control of the center and open up the rook on e1 to attack the black king. It would also prevent black from castling short and create threats of the queen and rook working together on the d-file. | False | None | None |
| openai/gpt-3.5-turbo-instruct | 6 | Possible next move: Qf6 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 7 | Possible move: Qd3 | False | None | None |
| openai/gpt-3.5-turbo-instruct | 8 | Based on the board state and FEN notation given, the best move for white is to move the queen to the square d6. This move will put pressure on the black king and potentially lead to a checkmate. In algebraic notation, the move would be "Qd6". | False | None | None |
| openai/gpt-3.5-turbo-instruct | 9 | The best move would be Qd4. This would put pressure on the black queen and protect the white queen. | False | None | None |
| openai/gpt-3.5-turbo-instruct | 10 | The best move for white in this position would be to move the queen from d1 to d5, attacking the black knight on d4 and potentially gaining control over the d-file. This move could lead to a strong position for white, as the queen is now threatening to capture the knight or even the pawn on c6. | False | None | None |
| deepseek/deepseek-chat-v3.1 | 1 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 2 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 3 | Rd1 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 4 | d5 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 5 | Qxb7 | True | d5b7 | 493 cp |
| deepseek/deepseek-chat-v3.1 | 6 | Qd8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 7 | Qd6 | True | d5d6 | -267 cp |
| deepseek/deepseek-chat-v3.1 | 8 | Qxe8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 9 | Rxe8 | False | None | None |
| deepseek/deepseek-chat-v3.1 | 10 | Qd8 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 1 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 2 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 3 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 4 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 5 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 6 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 7 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 8 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 9 | Nf3 | False | None | None |
| meta-llama/llama-3.3-8b-instruct:free | 10 | e4 | False | None | None |
| openai/gpt-5-chat | 1 | Nf7 | True | h6f7 | Mate in 3 |
| openai/gpt-5-chat | 2 | Nf7 | True | h6f7 | Mate in 3 |
| openai/gpt-5-chat | 3 | Nf7 | True | h6f7 | Mate in 3 |
| openai/gpt-5-chat | 4 | Nf7 | True | h6f7 | Mate in 3 |
| openai/gpt-5-chat | 5 | Nf7 | True | h6f7 | Mate in 3 |
| openai/gpt-5-chat | 6 | Nf7 | True | h6f7 | Mate in 3 |
| openai/gpt-5-chat | 7 | Nf7 | True | h6f7 | Mate in 3 |
| openai/gpt-5-chat | 8 | Nf7 | True | h6f7 | Mate in 3 |
| openai/gpt-5-chat | 9 | Nf7 | True | h6f7 | Mate in 3 |
| openai/gpt-5-chat | 10 | Nf7 | True | h6f7 | Mate in 3 |
| qwen/qwen3-coder | 1 | Qxg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 2 | Qxg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 3 | Qxg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 4 | Qxg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 5 | Qxg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 6 | Qxg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 7 | Qxg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 8 | Qxg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 9 | Qxg8 | True | d5g8 | Mate in 1 |
| qwen/qwen3-coder | 10 | Qxg8 | True | d5g8 | Mate in 1 |
| meituan/longcat-flash-chat | 1 | Nxf7 | True | h6f7 | Mate in 3 |
| meituan/longcat-flash-chat | 2 | Qg5 | True | d5g5 | 539 cp |
| meituan/longcat-flash-chat | 3 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 4 | Nf5 | True | h6f5 | -455 cp |
| meituan/longcat-flash-chat | 5 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 6 | Qh5 | False | None | None |
| meituan/longcat-flash-chat | 7 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 8 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 9 | Qd5 | False | None | None |
| meituan/longcat-flash-chat | 10 | Qd5 | False | None | None |
| mistralai/mistral-medium-3.1 | 1 | Qd6 | True | d5d6 | -283 cp |
| mistralai/mistral-medium-3.1 | 2 | Qd7 | True | d5d7 | -565 cp |
| mistralai/mistral-medium-3.1 | 3 | Qc4 | False | None | None |
| mistralai/mistral-medium-3.1 | 4 | Qd7 | True | d5d7 | -603 cp |
| mistralai/mistral-medium-3.1 | 5 | Qd7 | True | d5d7 | -624 cp |
| mistralai/mistral-medium-3.1 | 6 | Rxe8 | False | None | None |
| mistralai/mistral-medium-3.1 | 7 | Qd8 | False | None | None |
| mistralai/mistral-medium-3.1 | 8 | Qd7 | True | d5d7 | -623 cp |
| mistralai/mistral-medium-3.1 | 9 | Qf5 | True | d5f5 | -185 cp |
| mistralai/mistral-medium-3.1 | 10 | Qd6 | True | d5d6 | -262 cp |
| baidu/ernie-4.5-vl-28b-a3b | 1 | e4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 2 | e4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 3 | e4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 4 | d3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 5 | e4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 6 | Nd5 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 7 | Qb3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 8 | d3 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 9 | e4 | False | None | None |
| baidu/ernie-4.5-vl-28b-a3b | 10 | d3 | False | None | None |