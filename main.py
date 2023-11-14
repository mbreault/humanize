import humanize
import datetime as dt

print(humanize.intcomma(12345))
print(humanize.intword(123455913))
print(humanize.intword(12345591313))
print(humanize.apnumber(4))
print(humanize.apnumber(41))
print(humanize.clamp(1.5 ,"{:}", 2, 3))
print(humanize.metric(1000))

print(humanize.naturalday(dt.datetime.now()))
print(humanize.naturaldelta(dt.timedelta(seconds=1001)))
print(humanize.naturalday(dt.datetime.now() - dt.timedelta(days=1)))
print(humanize.naturalday(dt.date(2007, 6, 5)))
print(humanize.naturaldate(dt.date(2007, 6, 5)))
print(humanize.naturaltime(dt.datetime.now() - dt.timedelta(seconds=1)))
print(humanize.naturaltime(dt.datetime.now() - dt.timedelta(seconds=3600)))


delta = dt.timedelta(seconds=3633, days=2, microseconds=123000)
print(humanize.precisedelta(delta))
print(humanize.precisedelta(delta, minimum_unit="milliseconds"))
print(humanize.precisedelta(delta, suppress=["days"], format="%0.4f"))
print(humanize.naturaldelta(dt.timedelta(seconds=2)))

print(humanize.naturalsize(1_000_000))
print(humanize.naturalsize(1_000_000, binary=True))
print(humanize.naturalsize(1_000_000, gnu=True))


print(humanize.fractional(1.5))
print(humanize.fractional(0.3))
print(humanize.fractional(0.333))

print(humanize.scientific(0.3))
print(humanize.scientific(500))
print(humanize.scientific("20000"))
print(humanize.scientific(1**10))
print(humanize.scientific(1**10, precision=1))
print(humanize.scientific(1**10, precision=0))
