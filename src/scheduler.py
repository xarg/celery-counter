from tasks import count

# schedules 10k count tasks
for i in range(10000):
    count.delay()
