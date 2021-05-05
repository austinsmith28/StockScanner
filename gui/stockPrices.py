import main
import csv
from datetime import date

today = date.today()
today = today.strftime("%Y%m%d")


def setPrices(row):
    newPrice = main.get_prices([row[0]])
    return newPrice

def getPrices(list):

    with open('stockPrices.csv', mode='r+') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(csv_file)

        plist = []

        #itterate through stock list
        for row in csv_reader:
            print(row)
            for i in list:
                if row[0] == i:
                    if int(today) > int(row[2]):
                        newPrice = setPrices(row)
                        plist.append(newPrice)
                    else:
                        plist.append(row[1])

                    list.remove(i)

                if len(list) == 0:
                    break

        if len(list) > 0:
            for i in range(len(list)):
                row = [list[0], "0", "0"]
                row[1] = setPrices(row)
                row[2] = today
                csv_writer.writerow(row)
                plist.append(row[1])
                list.remove(list[0])

    print(plist)
    return plist