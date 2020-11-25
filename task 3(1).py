def merge(caps1,caps2):
    return(caps1.update(caps2))
caps1=dict(tn="chennai",ap="amaravathi",ka="bangalore")
caps2=dict(ts="hyderabad",mh="mumbai",goa="panaji")
print(merge(caps1,caps2))
print(caps2)