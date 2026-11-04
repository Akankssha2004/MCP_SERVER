from anyio.itertools import product
from fastmcp import FastMCP

mcp=FastMCP('Amazon E-commerce')

@mcp.tool
def search_products():
    '''The Available products in amazon'''
    products=['Mobiles','Laptops','Headphones','SmartWatches','SmartBands']
    return products

@mcp.tool
def get_offers():
    '''This tool gives  the offer details of product '''
    offers={'Mobiles':'10%','Laptop':'35%','Headphone':'12%'}
    return offers

@mcp.tool
def order_status():
    ''' The order status of delivery'''
    return 'The Product is delivered'

@mcp.tool
def payment():
    '''This tool tells whether payment is done or not '''
    status='yes'
    return status
    
if __name__=='__main___':
    mcp.run(transport='streamable-http',port=5001,host='0.0.0.0')