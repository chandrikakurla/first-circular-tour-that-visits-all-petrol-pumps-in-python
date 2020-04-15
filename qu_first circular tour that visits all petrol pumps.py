#class petrolpump
class petrolpump:
    def __init__(self,petrol,distance):
        #initialising first parameter to petrol
        self.petrol=petrol
        #initialising second parameter to distance
        self.distance=distance
#finding start position of circular tour
def Circular_Tour(arr):
    start=0
    end=1
    n=len(arr)
    current_petrol=arr[start].petrol-arr[start].distance
    while(start!=end or current_petrol<0):
        #If curremt amount of petrol in truck becomes less than 0, then  
        #remove the starting petrol pump from tour  
        while(start!=end and current_petrol<0):
            #Remove starting petrol pump. 
            current_petrol-=arr[start].petrol-arr[start].distance
            #Change start
            start=(start+1)%n
            if start==0:
                print("circular tour is not possible")
                return
        current_petrol+=arr[end].petrol-arr[end].distance
        end=(end+1)%n
    return start
if __name__=="__main__":
    array=[petrolpump(4,6),petrolpump(6,5),petrolpump(7,3),petrolpump(4,5)]
    print(Circular_Tour(array))

