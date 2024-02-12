from datetime import datetime
import random
class Token():


    """
        Devuelve token.
    """
    def getToken(self):
        

        token  = random.randint(100000, 999999)
        return str(token)


        



