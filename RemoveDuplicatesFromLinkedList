# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	temp = linkedList
	while 1:
		if temp and temp.next != None:
			if temp.next.value != temp.value:
				temp = temp.next
			else:
				temp.next = temp.next.next
		else:
			return linkedList
