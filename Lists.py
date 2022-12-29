if __name__ == '__main__':
    N = int(input())
    list_ = []
    for i in range(N):
        inst = list(map(str, input().split()))
        command = inst[0]
        if command == "print":
            print(list_)
        elif command == "insert":
                list_.insert(int(inst[1]),int(inst[2]))
        elif command == "remove":
                list_.remove(int(inst[1]))
        elif command == "append":
                list_.append(int(inst[1]))
        elif command == "sort":
                list_.sort()
        elif command == "pop":
                list_.pop()
        elif command == "reverse":
                list_.reverse()
