import GiftCode
import datetime

code = GiftCode.GetCode()
fh = open('somewhere.txt', 'w') # Change somewhere to wherever you want to save;
fh.write(code)
fh.write("\n")
today = datetime.date.today()
fh.write(today.strftime("%m%d"))



