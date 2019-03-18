class ValidationChainException(Exception):
    """ execao custom para a cadeia de validacao """
    
    def __init__(self,*args, **kwargs):
        """
        sobreescreve o metodo do init 
        """
        return super().__init__(*args,**kwargs)