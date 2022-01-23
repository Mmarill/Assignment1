from account import Account
from customer import Customer
from datasource import Datasource

class Bank:
    
    ds = Datasource()
    

    def _load(self):
        self.customer