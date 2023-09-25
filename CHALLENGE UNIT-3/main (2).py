def linear_search_product(productlist,targetproduct):
    indices=[]
    for index,product in enumerate(productlist):
        if product==targetproduct:
            indices.append(index)
    return indices

print("\n\t\tLINEAR SEARCH")
print("\n\t\t*************")
products=["shoes","boots","shoes","saree","coat","sandal","shoes"]
target="shoes"
target2="apple"
result=linear_search_product(products,target)
result1=linear_search_product(products,target2)
print("THE TARGET PRODUCT IS FOUND IN THE POSITION(SHOES):",result)
print("THE TARGET PRODUCT IS NOT FOUND. SO, THE LIST IS EMPTY(APPLE)",result1)
