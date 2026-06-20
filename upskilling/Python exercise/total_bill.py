def split_bill(total_bill, people):

    if people <= 0:
        return "Invalid"

    share = total_bill // people

    print("Each person pays:", share)

total_bill = 1250
people = 4

split_bill(total_bill, people)