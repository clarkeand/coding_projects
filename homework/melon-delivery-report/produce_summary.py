
#Create a genaral function that takes a file and iterates through deliveries
#For each line in the file ready each part of the token. 
def generateReport(day_file):
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    
#Day 1
print("Day 1")
the_file = open("um-deliveries-day-1.txt")
generateReport(the_file)
the_file.close()

#Day 2
print("Day 2")
the_file = open("um-deliveries-day-2.txt")
generateReport(the_file)
the_file.close()

#Day 3
print("Day 3")
the_file = open("um-deliveries-day-3.txt")
generateReport(the_file)
the_file.close()
