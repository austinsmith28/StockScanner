import main
import csv
from datetime import date

# set date
today = date.today()
today = today.strftime("%Y%m%d")

# get new price from api
def setPrices(row):
    try:
        arr = main.get_prices([row[0]])
        newPrice = arr[0]
    except:
        newPrice = "*ERROR*"

    return newPrice

# check csv for prices and return price list
def getPrices(list):

    # read file
    with open('stockPrices.csv', mode='r+', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)

        plist = []      # list of prices to return
        lines = []      # list of lines to write

        # itterate through stock list
        for row in csv_reader:

            # used for checking change in list
            x = len(list)

            # itterate through input list
            for i in list:

                # check if stock and input are the same
                if row[0] == i:

                    # check if entry is up to date
                    if int(today) > int(row[2]):

                        # get price
                        newPrice = setPrices(row)
                        plist.append(newPrice)
                        if newPrice == "*ERROR*":
                            continue

                        newRow = [i, newPrice, today]
                        lines.append(newRow)

                    # entry is up to date, return price from file and write line
                    else:
                        plist.append(row[1])
                        lines.append(row)

                    list.remove(i)

                # check if list is empty
                if x == 0:
                    break

            # write line if skipped earlier
            if x == len(list):
                lines.append(row)


        # check if any stocks need to be added to list
        if len(list) > 0:
            for i in range(len(list)):
                # create new row
                row = [list[0], "0", "0"]
                row[1] = setPrices(row)
                row[2] = today

                # write new row and add price to output list
                plist.append(row[1])
                if row[1] == "*ERROR*":
                    continue
                print(row[1])
                lines.append(row)
                list.remove(list[0])

    # write to file
    with open('stockPrices.csv', mode='w+', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(lines)

    print(plist)
    return plist