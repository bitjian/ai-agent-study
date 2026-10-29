"""一元二次方程 ax² + bx + c = 0 的求根公式

求根公式：x = (-b ± √(b² - 4ac)) / (2a)

运行：uv run python python/quadratic.py
"""

import math


def quadratic(a, b, c):
    """返回方程 ax² + bx + c = 0 的两个实数解。

    无实数解时返回 None。
    """
    if a == 0:
        raise ValueError("a 不能为 0，这就不是一元二次方程了")

    delta = b**2 - 4 * a * c          # 判别式 Δ = b² - 4ac
    if delta < 0:
        return None                   # Δ < 0，无实数解

    sqrt_delta = math.sqrt(delta)     # √Δ
    return (-b + sqrt_delta) / (2 * a), (-b - sqrt_delta) / (2 * a)


print("quadratic(2, 3, 1) =", quadratic(2, 3, 1))    # 两个解
print("quadratic(1, -2, 1) =", quadratic(1, -2, 1))  # Δ=0，重根
print("quadratic(1, 0, 1) =", quadratic(1, 0, 1))    # Δ<0，无实根

x1, x2 = quadratic(1, 2, -4)
print("quadratic(1, 2, -4) =", x1, x2)

# 验算：把解代回方程 x² + 2x - 4，结果应该 ≈ 0
for x in (x1, x2):
    print(f"验算 x={x:+.4f} -> x²+2x-4 = {x**2 + 2 * x - 4:.10f}")
