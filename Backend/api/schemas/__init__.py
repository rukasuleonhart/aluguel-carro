from .user import (User_Public_Schema, User_Create_Schema, User_Read_Schema, User_Read_With_Cars_Schema, User_Read_With_Rentals_Schema, User_Read_Full_Schema, Users_List,)
from .car import Car_Schema
from .rental import Rental_Schema

# Isso facilita a importação sendo necessário apenas usar from schemas e o nome da classe Ex: from schemas import * || from schemas import User_Read_Schema
__all__ = ["User_Public_Schema", "User_Create_Schema", "User_Read_Schema", "User_Read_With_Cars_Schema", "User_Read_With_Rentals_Schema", "User_Read_Full_Schema", "Car_Schema", "Rental_Schema", "Users_List"]

