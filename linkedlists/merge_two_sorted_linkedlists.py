def sortedMerge(head1, head2):
    # code here
    head = None
    if (head1.data < head2.data):
        head = head1
        curr1 = head1.next
        curr2 = head2
    else:
        head = head2
        curr2 = head2.next
        curr1 = head1

    curr = head
    while (curr1 != None and curr2 != None):
        if (curr1.data < curr2.data):
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        curr = curr.next
    while (curr1 != None):
        curr.next = curr1
        curr1 = curr1.next
        curr = curr.next
    while (curr2 != None):
        curr.next = curr2
        curr2 = curr2.next
        curr = curr.next
    curr.next = None
    return head