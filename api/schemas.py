from pydantic import BaseModel


class AddInput(BaseModel):
    """
    Pydantic data model for addition input.

    Attributes:
        x (int): The first integer to add.
        y (int): The second integer to add.
    """
    x: int
    y: int


class MultiplyInput(BaseModel):
    """
    Pydantic data model for multiplication input.

    Attributes:
        x (int): The first integer to multiply.
        y (int): The second integer to multiply.
    """
    x: int
    y: int


class UpperCaseInput(BaseModel):
    """
    Pydantic data model for text input to be converted to uppercase.

    Attributes:
        text (str): The string to be converted to uppercase.
    """
    text: str
