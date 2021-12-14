# -*- coding: utf-8 -*-
class Pedidos:
    def __init__(self, code = None, register_date = None, assisted = None, need = None, age = None, beginning = None, ending = None, requester = None, email = None, phone = None, address = None, observations = None, info = None):
        self._code = code
        self._register_date = register_date
        self._assisted = assisted
        self._need = need
        self._age = age
        self._beginning = beginning
        self._ending = ending
        self._requester = requester
        self._email = email
        self._phone = phone
        self._address = address
        self._observations = observations
        self._info = info
    
    
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, Code):
        self._code = Code
    
    
    @property
    def register_date(self):
        return self._register_date
    @register_date.setter
    def register_date(self, Register_Date):
        self._register_date = Register_Date


    @property
    def assisted(self):
        return self._assisted
    @assisted.setter
    def assisted(self, Assisted):
        self._assisted = Assisted


    @property
    def need(self):
        return self._need
    @need.setter
    def need(self, Need):
        self._need = Need


    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, Age):
        self._age = Age
    
    
    @property    
    def beginning(self):
        return self._beginning
    @beginning.setter
    def beginning(self, Beginning):
        self._beginning = Beginning


    @property
    def ending(self):
        return self._ending
    @ending.setter
    def ending(self, Ending):
        self._ending = Ending


    @property    
    def requester(self):
        return self._requester
    @requester.setter
    def requester(self, Requester):
        self._requester = Requester


    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, Email):
        self._email = Email


    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, Phone):
        self._phone = Phone


    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, Address):
        self._address = Address
    
    
    @property
    def observations(self):
        return self._observations
    @observations.setter
    def observations(self, Observations):
        self._observations = Observations


    @property
    def info(self):
        return self._info
    @info.setter
    def info(self, Info):
        self._info = Info
