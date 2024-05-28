from django.db import models

class AutoMetaModelBase(models.base.ModelBase):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        meta = new_class._meta
        if not meta.abstract:
            class_name = name.lower().replace('_', ' ')
            meta.verbose_name = class_name
            meta.verbose_name_plural = class_name
        return new_class

class BaseLookupsModel(models.Model, metaclass=AutoMetaModelBase):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
        ordering = ["name"]

    def __str__(self):
        return self.name

class Province(BaseLookupsModel):
    pass

class Country(BaseLookupsModel):
    pass

class Client_Status(BaseLookupsModel):
    pass

class Project_Status(BaseLookupsModel):
    pass

class Task_Status(BaseLookupsModel):
    pass
