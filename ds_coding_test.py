# 배열을 이용한 스택 구현
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None


# 테스트 함수
def main():
    # 스택 객체 생성
    stack = Stack()

    # push 연산 테스트
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # 스택 상태 출력
    print("Stack: ", stack.stack)

    # pop 연산 테스트
    popped_element = stack.pop()
    print("Popped Element: ", popped_element)

    # top 연산 테스트
    top_element = stack.top()
    print("Top Element: ", top_element)

    # 스택이 비어 있는지 확인
    is_empty = stack.is_empty()
    print("Is Empty: ", is_empty)

    # 스택의 크기 확인
    stack_size = stack.size()
    print("Stack Size: ", stack_size)


# 테스트 실행
if __name__ == "__main__":
    main()
