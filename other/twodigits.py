#workers and payrolls

payrolls = {'charlie' : 3.1415926, 'tom' : 19.994, 'jenny' : 5, 'clark' : 7.1, 'elya' : 6.55555}


print("charlie:" + "$" + "{:.2f}".format(payrolls['charlie']))
print("tom:" + "$" + "{:.2f}".format(payrolls['tom']))
print("jenny:" + "$" + "{:.2f}".format(payrolls['jenny']))
print("clark:" + "$" + "{:.2f}".format(payrolls['clark']))
print("elya:" + "$" + "{:.2f}".format(payrolls['elya']))


payrolls1 = [3.1415926, 19.994, 5, 7.1, 6.5555]
n = 0
for i in payrolls1:
    print("$" + "%.02f" % (payrolls1[n]))
    n = n+1

