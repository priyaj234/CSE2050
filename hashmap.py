class Hashmap():
    def __init__(self):
         self._dict = dict()
    def update_balance(self, user = "", amount = 0):
        '''Updates the user's bank balance'''
        self._dict[user] = amount
    def get(self, user = ""):
        '''return the user's bank balance'''
        #user in dict
        #user not in dict
        if user not in self:
            return 0
        else:
            return self._dict[user] 
    def __contains__(self, user = ""):
        if user in self._dict:
            return True
        else:
            return False
    def __len__(self):
        return self._dict