def readQuote():
    with open('quotes.txt','r') as file:
        quotes = file.read()
        print('\nyour saved quotes\n')
        print(quotes)


def writeQUote():
    userInput = input('Enter the quote: ')
    with open('quotes.txt','a') as file:
        file.write(f"{userInput}\n\n")


while True:
    print('--------- Read and write quote -------------')
    print("\n1. Write a quote")
    print("2. Read quotes")
    print("3. Exit\n")
    choice = input("Choose an option (1/2/3):\n")

    if choice == "1":
        writeQUote()

    elif choice == "2":
        readQuote()

    elif choice == "3":
        print("Return back soon, Goodbye!\n\n")
        break
# choice validation
    else:
        print("Invalid choice. Please enter 1, 2, or 3.\n")

