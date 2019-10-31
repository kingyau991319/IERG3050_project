
class Crane(object):
    """
    It is the moving part of the cargo container, so that cargo container can
    from one part for two part. For the case of different tons and size of 
    cargo container, Gantry crane also have different size with that. 

    @speed: states the time that moving the cargo container, because it is 
                    not increasing linearly by tons, so need to make a directory to 
                    specify with that. 

    @ID: Unique case 

    @flag: working, no working,  ? 0:1 

    @position: I will make the position to indicate the Gantry crane are in 
                            which place 

    @using year: Maybe it will have some error or accident with Gantry crane,
                             so I will set a random number for probability that may crash 
                             in this case. It just depends on the deficit. 

    @use case: 	It has different position so it has a different case for Gantry 
                            Crane, it may move from storage to ship or ship to storage, 
                            it is a pair, the other pair is stack with stack and reach 
                            stacker to stack 

    """

    def __init__(self, ID, speed, flag, position, using_year, use_case):
        self.ID = ID
        self.speed = speed
        self.flag = flag
        self.position = position
        self.using_year = using_year
        self.use_case = use_case
