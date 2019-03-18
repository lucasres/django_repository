from dpatterns.repository import RepositoryBase
from dpatterns.exception import ValidationChainException

class NumberRepository(RepositoryBase):
    """ Exemplo de cadeia de responsabilidade """
    @classmethod
    def handle_great_20(cls,number:int) -> str:
        """
        Cadeia de responsabilidade
        number: Int
        """
        #tenta passar pela cadeia de responsabilidade
        try:
            cls.validate_1(number)
            cls.validate_2(number)
            cls.validate_3(number)
            return 'passou'
        except ValidationChainException as e:
            return str(e)


    @classmethod
    def validate_1(cls,number:int) -> bool:
        """
        Valida se eh maior que 10
        number: Int
        return: Bool
        """
        if number > 10:
            return True
        else:
            raise ValidationChainException('O numero deve ser maior que 10')
    
    @classmethod
    def validate_2(cls,number:int) -> bool:
        """
        Valida se eh maior que 20
        number: Int
        return: Bool
        """
        if number > 20:
            return True
        else:
            raise ValidationChainException('O numero deve ser maior que 20')
    
    @classmethod
    def validate_3(cls,number:int) -> bool:
        """
        Valida se eh menor que 30
        number: Int
        return: Bool
        """
        if number < 30:
            return True
        else:
            raise ValidationChainException('O numero deve ser menor que 30')