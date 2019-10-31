import container
#import stack


class ship(object):
    """
    Cargo ship contain a large amount of the Cargo containers, each ship 
    has different kinds of amount for containing cargo containing with 
    1500~2500, in my simulation, I ignore the cargo ship arriving part 
    because it has been planned, it was an essential prelude so there are 
    only fix size with 1 cargo ship every day or 1 cargo twice a day 
    in this case. 

    In simulation, I try to follow the real cargo ship in real life but 
    not for random generating. About which ship problem, I will use 
    uniform distribution to simulate with that 


        @ID :Use to specify which cargo container are, it is an unique 
            number 

        @The kinds of cargo ship :Because ships can also deliver with 
            oil or gas, so I prepare to follow this case in the project. 

        @Ton :Use for real word data

        @container_num: The amount of a Cargo container

        @arrival time: It indicates that which time it came from, this 
                    case will be used by normal distribution. 

            @depart time :It is the time that departing out for the port. 

            @stack :Stack is simulating the position of cargo containers. 
                        It will be stored like that.  
"""

    def __init__(self, ID, kinds, ton, container_num, arrival_time, departing_time, stack):
        self.arg = arg
        self.ID = ID
        self.kinds = kinds
        self.ton = ton
        self.container_num = container_num
        self.arrival_time = arrival_time
        self.departing_time = departing_time
        self.stack = stack


if __name__ == '__main__':
    main()
