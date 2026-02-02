"""
Calculator tool for performing basic mathematical operations.
"""

from agents import function_tool
import operator
import re


@function_tool
def calculator(expression: str) -> str:
    """
    Perform basic mathematical calculations on a given expression.
    
    Args:
        expression: A mathematical expression as a string (e.g., "5 + 5", "10 * 3", "100 / 4")
        
    Returns:
        The result of the calculation as a string, or an error message if the expression is invalid.
    """
    try:
        # Clean the expression and validate it contains only safe characters
        expression = expression.strip()
        
        # Basic validation - only allow numbers, operators, parentheses, and spaces
        if not re.match(r'^[0-9+\-*/().\s]+$', expression):
            return "Error: Invalid characters in expression. Only numbers and basic operators (+, -, *, /) are allowed."
        
        # Replace common text operators with symbols
        expression = expression.replace('plus', '+')
        expression = expression.replace('minus', '-')
        expression = expression.replace('times', '*')
        expression = expression.replace('multiplied by', '*')
        expression = expression.replace('divided by', '/')
        expression = expression.replace('to the power of', '**')
        expression = expression.replace('squared', '**2')
        expression = expression.replace('cubed', '**3')
        expression = expression.replace('square root of', 'sqrt(')
        expression = expression.replace('sqrt(', 'math.sqrt(')
        
        # Import math for advanced functions
        import math
        
        # Evaluate the expression safely
        result = eval(expression)
        
        # Format the result
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        return f"Result: {result}"
        
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: Invalid mathematical expression. {str(e)}"
