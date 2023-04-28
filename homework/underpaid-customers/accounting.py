

def customer_accounting(file):
    customer_list = []
    for line in file:
        line = line.rstrip()
        words = line.split('|')

        customer_name = words[1]
        customer_melons = float(words[2])
        customer_payment = float(words[3])

        customer_list.append([customer_name, customer_melons,customer_payment])

    melon_cost = 1.00

    for item in customer_list: 
        expected_payment = item[1] * melon_cost
        if expected_payment != item[2]:
            print(f"{item[0]} paid ${item[2]},",
            f"expected ${expected_payment}")
        else:
            continue

the_file = open("customer-orders.txt")
customer_accounting(the_file)
the_file.close()