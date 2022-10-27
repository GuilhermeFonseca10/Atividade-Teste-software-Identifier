from src import identifier
class TesteIdentifier:

    def teste1(self):
        assert identifier.identifier("") == False
    
    def teste2(self):
        assert identifier.identifier("a") == True
    
    def teste3(self):
        assert identifier.identifier("a12345") == True

    def teste4(self):
        assert identifier.identifier("1") == False

    def teste5(self):
        assert identifier.identifier("a123546") == False

    def teste6(self):
        assert identifier.identifier("a1&34") == False
