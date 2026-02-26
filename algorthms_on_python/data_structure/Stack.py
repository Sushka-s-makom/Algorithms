

from typing import Any, List


def stack_create() -> List[Any]:
    return []


def stack_push(stack: List[Any], value: Any) -> None:
    stack.append(value)


def stack_pop(stack: List[Any]) -> Any:
    if not stack:
        raise IndexError("Pop from empty stack")
    return stack.pop()


def stack_peek(stack: List[Any]) -> Any:
    if not stack:
        raise IndexError("Peek from empty stack")
    return stack[-1]


def stack_is_empty(stack: List[Any]) -> bool:
    return len(stack) == 0


def stack_size(stack: List[Any]) -> int:
    return len(stack)
if __name__ == "__main__":
    # list stack
    s = stack_create()
    stack_push(s, 10)
    stack_push(s, 20)
    print(stack_peek(s))  # 20
    print(stack_pop(s))   # 20
    print(stack_size(s))  # 1