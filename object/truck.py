import container


class truck(object):

    """
    Cargo truck is the land part of the delivering, it can transport to 
    storage using internal cargo truck 


        @ID : For specify truck  

        @position : I will make the position to indicate the cargo truck 
                    are in which place, it is 2D array
        @flag:  0-> have a truck 
                1-> not have the cargo truck 
        @flag2: 0-> out 
                1-> in 
        @flag3: 0-> internal
                1-> external 
    """

    def __init__(self, ID, position, flag, flag2, flag3):
        self.ID = ID
        self.position = position
        self.flag = flag
        self.flag2 = flag2
        self.flag3


if __name__ == '__main__':
    main()
