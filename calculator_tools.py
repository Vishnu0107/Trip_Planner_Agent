from langchain.tools import tool
from pydantic import BaseModel, Field
import warnings
warnings.filterwarnings("ignore")


class CalculatorTools():
    @tool("Make a calculation") # Here we use a decorator to define the tool name and description
    def calculate(operation): # The crewai will recognize this tool and automatically calls it 
        """
        Usefull to perform any mathematical calculations like addition, subtraction, multiplication, division, etc...
        The input to this tool should be a mathematical expression, a couple examples are `200 * 7`
        or `5000 / 2 * 10`

        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"


# We can use the below approach 
# # Define a pydantic model for the tool's input parameters
# class CalculatorInput(BaseModel):
#     operation: str = Field(..., description="The mathematical expression to evaluate")
#     factor: float = Field(..., description="The factor to multiply the result by", default=1)

# # Use the local decorator with the arg_schema parameter pointing to the Pydantic model
# @tool("perform_calculation", args_schema=CalculatorInput, return_direct = True)
# def perform_calculation(operation: str, factor: float) -> str:
#     """
#     Performs a specified mathematical operation and multiplies the result by a given factor.

#     Parameters:
#     - operation (str): A string representing a mathematical operation (e.g., "2 + 3").
#     - factor (float): A float representing the factor to multiply the result by (e.g., 2.5).

#     Returns:
#     - str: The result of the specified mathematical operation, multiplied by the given factor.
#     """

#     # Perform the calculation
#     result = eval(operation) * factor

#     # Return the result as a string
#     return f"The result of '{operation}' multiplied by {factor} is {result:.2f}"