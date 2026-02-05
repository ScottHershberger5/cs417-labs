# Scott Hershberger
# CS417
# Parser/pytest/API's

def parse_product_basic(response):
    """
    Extract basic product information from API response.
    
    Args:
        response (dict): Full API response containing product data
        
    Returns:
        dict: Dictionary with only 'id' and 'name' keys
        
    Example:
        >>> response = {"id": "prod_123", "name": "Headphones", "in_stock": True}
        >>> parse_product_basic(response)
        {"id": "prod_123", "name": "Headphones"}
    """
    basic_info = dict()
    basic_info["id"] = response["id"]
    basic_info["name"] = response["name"]
    return basic_info



def parse_availability(response):
    """
    Determine if product is available for purchase.
    
    Args:
        response (dict): API response that may contain 'in_stock' field
        
    Returns:
        bool: True if in_stock is True, False otherwise (including when field is missing)
        
    Example:
        >>> parse_availability({"in_stock": True})
        True
        >>> parse_availability({"in_stock": False})
        False
        >>> parse_availability({})  # Missing field
        False
    """
    pass  # Your implementation here