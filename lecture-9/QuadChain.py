chain = map(int, raw_input().split(','));
p = sum(chain);
side = p / 4;
# print 'side=',side;
index = 0;
sum=0;
for i in range(4):
    sum = 0;
    for j in chain[index:len(chain)]:
        # print 'index=',index;
        # print 'sum=',sum;
        if sum != side:
            sum += j;
            index += 1;
        else:
            break;
if sum != side:
    print 'NO';
else:
    print 'YES';