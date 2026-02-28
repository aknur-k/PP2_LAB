from datetime import datetime, timedelta

today = datetime.now()
new_date = today - timedelta(days=5)

print(new_date)



from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(today, yesterday, tomorrow)




from datetime import datetime

now = datetime.now()
micro = now.replace(microsecond=0)

print(micro)



from datetime import datetime

date1 = datetime(2025, 1, 1, 12, 0, 0)
date2 = datetime(2025, 1, 2, 12, 0, 0)

dif = date2 - date1
print(dif.total_seconds())