class Database:
    def __init__(self, path):
        self.path = path
        self.data = {}

        with open(self.path, 'r') as file_handle:
            

        acct = self.data.get(acct_id)

        if acct:
            balance = float(acct['due']) - float(acct['paid'])
            return f"Balance is: ${balance.2f} USD"
        return None
