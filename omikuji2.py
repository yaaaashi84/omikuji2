"""
①「今日の運勢は… 大吉」と出力
"""
import random

omikuji = ["大吉", "吉", "凶", "中吉"]

index = random.randint(0, 3)
result = omikuji[index]

print(f"今日の運勢は… {result}")


