class Order:
    _id_count = 0

    def __init__(self, date, name_client, delivery):
        Order._id_count += 1
        self._id = Order._id_count
        self._date = date
        self._name_client = name_client
        self._delivery = delivery

    @property
    def id(self):
        return self._id

    @property
    def name_client(self):
        return self._name_client

    @property
    def date(self):
        return self._date

    @property
    def delivery(self):
        return self._delivery
    
    def __str__(self):
        return f"Order ID: {self._id}, Date: {self._date}, Client: {self._name_client}, Delivery: {self._delivery}"

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return self._id == other._id