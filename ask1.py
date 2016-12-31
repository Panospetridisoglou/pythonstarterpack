x=raw_input()
y=x.split("!")
i=0
while (y[-(i+1)]==""):
    i+=1

print ''.join(y)+(i*"!")
