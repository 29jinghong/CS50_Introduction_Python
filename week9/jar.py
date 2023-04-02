def main():
    jinghong_jar = jar(23)
    print("1:")
    print("0 cookie")
    print(jinghong_jar)

    jinghong_jar.deposit(23)
    print("2:")
    print("23 cookie")
    print(jinghong_jar)
    
    jinghong_jar.withdraw(20)
    print("3:")
    print("3 cookie")
    print(jinghong_jar)

    jinghong_jar.capacity = 30
    jinghong_jar.cookie = 30
    print("4:")
    print("30 cookie")
    print(jinghong_jar)

    #testing deposit
    #ValueError
    #jinghong_jar.deposit(2000)
    
class jar:
    #init defalt capacity is 12
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.cookie = 0

    #when printing the function you get whats under __str__
    def __str__(self):
        return "🍪" * self.cookie

    #making depositing(adding cookie to the jar)
    def deposit(self, num):
        self.cookie += num
    
    #making withdraw(taking cookie away from the jar)
    def withdraw(self, num):
        self.cookie -= num

    #adding a property
    @property
    def capacity(self):
    #getting the max capacity
        return self._capacity

    #setting the max capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity

    #adding a property
    @property
    #getting cookie total
    def cookie(self):
        return self._cookie

    #setting cookie
    @cookie.setter
    def cookie(self, cookie):
        if cookie < 0:
            raise ValueError("There is not enough cookies.")
        if cookie > self.capacity:
            raise ValueError("There is not enough space.")
        self._cookie = cookie

if __name__ == "__main__":
    raise SystemExit(main())

