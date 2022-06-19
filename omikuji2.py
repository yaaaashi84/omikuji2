"""
①「今日の運勢は… 大吉」と出力
"""
import random

omikuji = ["大吉", "吉", "凶", "中吉", "末吉"]

# index = random.randint(0, len(omikuji) - 1) # おみくじのリストの中の乱数を取得する(これは読みにくいらしい)
# result = omikuji[index]
# 一行にしたいときは、randintではなくchoiceを使用する

result = random.choice(omikuji)

print(f"今日の運勢は… {result}")


