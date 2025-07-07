if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        cmd = input()
        if cmd[:6] == "insert":
            cmd = cmd[7:]
            num1 = 0
            num2 = 0
            for j in range(len(cmd)):
                if cmd[j].isspace():
                    num1 = int(cmd[:j])
                    num2 = int(cmd[j+1:])
            l.insert(num1, num2)
        elif cmd[:5] == "print":
            print(l)
        elif cmd[:6] == "remove":
            num = int(cmd[7:])
            l.remove(num)
        elif cmd[:6] == "append":
            num = int(cmd[7:])
            l.append(num)
        elif cmd[:4] == "sort":
            l.sort()
        elif cmd[:3] == "pop":
            l.pop()
        elif cmd[:7] == "reverse":
            l.reverse()
            
# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

