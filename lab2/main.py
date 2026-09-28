import random
import time


# Количество проверенных узлов
minimax_nodes = 0
alphabeta_nodes = 0


# Глубина и ширина дерева
DEPTH = 6
WIDTH = 2


# -------------------------------------------------
# Создание дерева
# -------------------------------------------------

def create_tree(depth):
    """
    Создаёт игровое дерево.
    В листьях находятся случайные значения от -100 до 100.
    """

    # Если достигли листа
    if depth == 0:
        return random.randint(-100, 100)

    # Создаём WIDTH дочерних узлов
    children = []

    for _ in range(WIDTH):
        children.append(create_tree(depth - 1))

    return children


# -------------------------------------------------
# Обычный мини-макс
# -------------------------------------------------

def minimax(node, depth, maximizing_player):
    global minimax_nodes

    # Проверяем узел
    minimax_nodes += 1

    # Если дошли до листа
    if depth == 0:
        return node

    # Ход MAX
    if maximizing_player:
        best_value = float('-inf')

        for child in node:
            value = minimax(child, depth - 1, False)
            best_value = max(best_value, value)

        return best_value

    # Ход MIN
    else:
        best_value = float('inf')

        for child in node:
            value = minimax(child, depth - 1, True)
            best_value = min(best_value, value)

        return best_value


# -------------------------------------------------
# Мини-макс с альфа-бета отсечением
# -------------------------------------------------

def alphabeta(node, depth, maximizing_player, alpha, beta):
    global alphabeta_nodes

    # Проверяем узел
    alphabeta_nodes += 1

    # Если дошли до листа
    if depth == 0:
        return node

    # Ход MAX
    if maximizing_player:
        best_value = float('-inf')

        for child in node:
            value = alphabeta(
                child,
                depth - 1,
                False,
                alpha,
                beta
            )

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            # Альфа-бета отсечение
            if beta <= alpha:
                break

        return best_value

    # Ход MIN
    else:
        best_value = float('inf')

        for child in node:
            value = alphabeta(
                child,
                depth - 1,
                True,
                alpha,
                beta
            )

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            # Альфа-бета отсечение
            if beta <= alpha:
                break

        return best_value


# -------------------------------------------------
# Основная программа
# -------------------------------------------------

# Генерируем одно дерево
random.seed(42)
tree = create_tree(DEPTH)


# Обычный мини-макс
minimax_nodes = 0

start_time = time.perf_counter()

minimax_result = minimax(
    tree,
    DEPTH,
    True
)

minimax_time = time.perf_counter() - start_time


# Мини-макс с альфа-бета отсечением
alphabeta_nodes = 0

start_time = time.perf_counter()

alphabeta_result = alphabeta(
    tree,
    DEPTH,
    True,
    float('-inf'),
    float('inf')
)

alphabeta_time = time.perf_counter() - start_time


# -------------------------------------------------
# Результаты
# -------------------------------------------------

print("=== Результаты ===")

print(f"Глубина дерева: {DEPTH}")
print(f"Ширина дерева: {WIDTH}")

print()

print("Обычный мини-макс:")
print(f"Результат: {minimax_result}")
print(f"Проверено узлов: {minimax_nodes}")
print(f"Время: {minimax_time:.8f} секунд")

print()

print("Мини-макс с альфа-бета:")
print(f"Результат: {alphabeta_result}")
print(f"Проверено узлов: {alphabeta_nodes}")
print(f"Время: {alphabeta_time:.8f} секунд")

print()

print("Проверка результатов:")

if minimax_result == alphabeta_result:
    print("Результаты совпадают")
else:
    print("Результаты НЕ совпадают")