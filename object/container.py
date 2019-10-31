import csv


class container(object):

    """

Cargo ship contain a large amount of the Cargo containers, each ship has
different kinds of amount for containing cargo containing with 1500~6500.
In my simulation, I ignore the cargo ship arriving part because it has
been planned, it was an essential prelude so there are only fix size with
1 cargo ship every day or 1 cargo twice a day in this case.
In simulation, I try to follow the real cargo ship in real life but not
for random generating.
About which ship problem, I will use uniform distribution to simulate.
variable


    @ID : Use to specify which cargo container are

    @size : Cargo container has different kinds of standard, in our
            simulation, we only definite with three standards to simplify
            the case in real world. Size must follow that and use enum
            Len:0,7.6m 1, 13.7m 2, 16.1m
            Height:2.6m

    @ton :  Ton is random with different kinds of embedded commodity.
            I try to use normal distribution to simulate with that.
            //Without to thinking about the 20 tons and 40 tons cargo
            //container case

    @flag : Flag states the position for cargo container, I use enum to
            represent it
            ->0: at marine (coming soon)
            ->1: Gantry crane
            ->2: Stack
            ->3: internal cargo truck
            ->4: external cargo truck
            ->5: done

    @source ship :  which ship are they come from

    @source truck : which truck are they come from

    @target ship : which ship are they go out

    @target truck : which truck are they go out

"""

    def __init__(self, ID, size, ton, flag, source_ship, source_truck, target_ship, target_truck):
        self.ID = ID
        self.size = size
        self.ton = ton
        self.flag = flag
        self.source_ship = source_ship
        self.source_truck = source_truck
        self.target_ship = target_ship
        self.target_truck = target_truck
    # tracking if it has source_ship and source_truck in this case

    # to string
    def tracing(self):
        print("ID = %10d, size = %1d ton = %0.2f flag = %1d source_ship = %d source_truck = %d target_ship = %d target_truck = %d" %
              (self.ID, self.size, self.ton, self.flag, self.source_ship, self.
                  source_truck, self.target_ship, self.target_truck))

    # for insert data
    def insert_data(self):
        with open('container.csv', 'w') as csvfile:
            csvfile_write = csv.writer(
                csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvfile_write.writerow([self.ID, self.size, self.ton, self.flag,
                                    self.source_ship, self.source_truck,
                                    self.target_ship, self.target_truck])
            csvfile.close()


if __name__ == '__main__':
    i = container(ID=11145141919, size=1, ton=20, flag=0, source_ship=114514,
                  source_truck=1919, target_ship=819, target_truck=114514)
    y = container(ID=114154114514, size=2, ton=3, flag=0,
                  source_ship=11, source_truck=2, target_ship=10, target_truck=8)
    i.tracing()
    i.insert_data()
    y.insert_data()
