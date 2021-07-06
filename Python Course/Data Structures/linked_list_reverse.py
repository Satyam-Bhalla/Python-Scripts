def ReversePrint(head):
    if head:
        ReversePrint(head.next)
        print(head.data)
