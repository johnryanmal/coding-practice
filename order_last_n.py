# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.


class OrderLast:
    none = object()

    def __init__(self, n):
        self.array = [self.none] * n
        self.size = n
        self.index = 0

    def record(self, order_id):
        self.array[self.index] = order_id
        self.index = (self.index + 1) % self.size
    
    def get_last(self, i):
        order_id = self.array[(self.index - i) % self.size]
        if order_id is not self.none:
            return order_id


buffer = OrderLast(3) #buffer last 3 orders
for id in range(10): #record orders 0-9
    buffer.record(id)
for i in range(1,1+3): #print out last 3 orders in order of most recent (9-7)
    print(buffer.get_last(i))