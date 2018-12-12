def play():

    leadtime  = 0

    for i in range(0,5):
    
        leadtime += 5
        
        myfile = open('test.txt', 'a')
        myfile.write(" %f %f \n" % (leadtime, float(2*i) )) 