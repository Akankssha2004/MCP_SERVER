
from fastmcp import FastMCP

mcp = FastMCP("Amazon E-commerce")


@mcp.tool
def search_products():
    """Returns the available products on Amazon."""
    products = [
        "Mobiles",
        "Laptops",
        "Headphones",
        "SmartWatches",
        "SmartBands"
    ]
    return products


@mcp.tool
def get_offers():
    """Returns the offer details of products."""
    offers = {
        "Mobiles": "10%",
        "Laptops": "35%",
        "Headphones": "12%"
    }
    return offers


@mcp.tool
def order_status():
    """Returns the order delivery status."""
    return "The product is delivered."


@mcp.tool
def payment():
    """Checks whether the payment is completed."""
    return "Payment completed."


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=5001
    )
