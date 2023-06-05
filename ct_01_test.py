'''
문제: 브라우저의 앞/뒤 이동 기능 구현

웹 브라우저에서 페이지를 방문할 때마다 이력이 기록됩니다. 또한, 브라우저에는 이전 페이지('뒤로 가기')와 다음 페이지('앞으로 가기')로 이동하는 기능이 있습니다. 
이를 스택 자료구조와 이진 검색 알고리즘을 이용해 구현해보세요.

[요구 사항]

1. Browser라는 이름의 클래스를 만드세요.
2.이 클래스는 다음 메소드들을 포함해야 합니다:
    - visit(url):  새로운 웹페이지 url을 방문하고 이를 이력에 기록합니다.
    - back():      이전 웹페이지로 이동합니다.
    - forward():   다음 웹페이지로 이동합니다.
    - search(url): 방문한 이력 중 url이 존재하는지 이진 검색 알고리즘을 이용해 찾습니다. 만약 존재한다면, 그 url이 몇 번째 방문한 페이지인지 반환합니다. 만약 존재하지 않는다면, -1을 반환합니다.

3.방문한 웹페이지는 모두 다른 url을 가진다고 가정합니다.

'''

#test case 1  정답 : 2
#test case 2  정답 : 3
#test case 3  정답 : 1
import argparse


parser = argparse.ArgumentParser(description='테스트 케이스')
parser.add_argument('--target', required=True, help='어느 것을 요구하냐')

class Browser:
    def __init__(self):
        self.history = []  # 방문 이력을 저장할 스택
        self.forward_stack = []  # 앞으로 가기 기능을 위한 스택

    def visit(self, url):
        self.history.append(url)
        self.forward_stack = []  # 새로운 페이지를 방문하면 앞으로 가기 스택을 비웁니다.

    def back(self):
        if len(self.history) > 1:  # 첫 페이지가 아니라면
            self.forward_stack.append(self.history.pop())  # 이전 페이지로 이동

    def forward(self):
        if self.forward_stack:  # 앞으로 갈 페이지가 있다면
            self.history.append(self.forward_stack.pop())  # 다음 페이지로 이동

    def search(self, url):
        start, end = 0, len(self.history) - 1
        while start <= end:  # 이진 검색 시작
            mid = (start + end) // 2
            if self.history[mid] == url:
                return mid + 1  # 1-based index
            elif self.history[mid] < url:
                start = mid + 1
            else:
                end = mid - 1
        return -1  # url이 이력에 없음


def main(testcase):
    browser = Browser()

    browser.visit('https://www.google.com')
    browser.visit('https://www.openai.com')
    browser.visit('https://www.github.com')

    if testcase == '1':
        #openai
        print(f"Searching for 'https://www.openai.com'. Index found: {browser.search('https://www.openai.com')}")
    elif testcase == '2':
        #github
        print(f"Searching for 'https://www.github.com'. Index found: {browser.search('https://www.github.com')}")
    elif testcase == '3':
        #google
        print(f"Searching for 'https://www.google.com'. Index found: {browser.search('https://www.google.com')}")
    else:
        print(f"Invalid target: {testcase}. Please input either 'openai', 'github', or 'google'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='테스트 케이스')
    parser.add_argument('--testcase', required=True)

    args = parser.parse_args()

    main(args.testcase)