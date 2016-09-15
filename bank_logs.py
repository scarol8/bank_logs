import re

def find_suspicious_ips(log):

    with open (log, "r") as myfile:
        data=myfile.readlines()

    regex = '([(\d\.)]+) - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'

    ipArr = []
    dateArr = []
    for section in data:
        ip = re.search('([(\d\.)]+)', section).group()
        ipArr.append(ip)
        date = re.search('\[(.*?)\]', section).group()
        splitDate = date.split(":")
        splitDateAgain = splitDate[3].split("-")
        dateInt = splitDate[1] + splitDate[2] + splitDateAgain[0]
        dateArr.append(dateInt)
    index = 0
    badList = []
    kindaBadList = []
    count = 0;
    for item in ipArr:
        if index != len(ipArr) - 1:
            if int(dateArr[index]) - int(dateArr[index+1]) <= 1 and item == ipArr[index+1]:
                if item not in badList:
                    badList.append(item)
        index = index+1
    #print kindaBadList
    return badList
