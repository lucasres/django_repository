class RepositoryMixin():
    """ This class will served for base for all repository of project """
    class Meta:
        model = None

    @classmethod
    def all(cls) -> 'QuerySet<Meta.Model>':
        """
        Shortcut for get all entity from model
        return: QuerySet<Model>
        """
        return cls.Meta.model.objects.all()
    
    @classmethod
    def get(cls, **kwargs:dict) -> 'Meta.Model':
        """
        Shortcut for get method of model
        return: Model
        """
        return cls.Meta.model.objects.get(**kwargs)

    @classmethod
    def filter(cls, **kwargs:dict) -> 'QuerySet<Meta.Model>':
        """
        Shortcut for filter method of model
        return: QuerySet<Model>
        """
        return cls.Meta.model.objects.filter(**kwargs)
    
    @classmethod
    def create(cls, **kwargs:dict) -> 'Meta.Model':
        """
        Shortcut for create method of model
        return: Model
        """
        return cls.Meta.model.objects.create(**kwargs)