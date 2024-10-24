def teilbar(x,y,):
    if y == 0:
        print("es ist nicht möglich durch 0 zu teilen!")
    else:
        
          if x == y:
              print ("x und y sind gleich")
          elif x%y == 0:
              print("x ist durch y teilbar")
          else:
              print("x ist nicht durch y teilbar")
              
    
teilbar(5,5,)
teilbar(2,0)
teilbar(5,6)

