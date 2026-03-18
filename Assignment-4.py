L1 = []

def addevent():
    L = input("Enter the event to be add")
    L1.append(L)

def processevent():
    if L1:
        X = L1.pop(0)
        print(f"Event {X} is process ")
    else:
        print("No event is in process")

def pendingevent():
    if L1:
        for X in L1:
            print(X)
    else:
        print("Event is not pending")

def cancel_event(event_name):
    if event_name in L1:
        L1.remove(event_name)
        print(f"Event is cancelled : (event_name)")
    else:
        print(f"Event name is not present in the queue")

while True:
    print("1.\n---MENU---")
    print("2.Add Event")
    print("3.Process Event")
    print("4.Pending Event")
    print("4.Cancel Event")
    print("5.Exit")
    choice = input("Enter the choice:")

    if choice == '1':
        addevent()
    elif choice == '2':
        processevent()
    elif choice == '3':
        pendingevent()
    elif choice == '4':
        event_name = input("Enter the event to be cancel:")
        cancel_event(event_name)
    elif choice == '5':
        print("exit")

    else:
        print("try again")          

            

