import random
from copy import deepcopy


class Agent:
    counter = 0
    ram_movement = 4 # rams can move 4 times quicker than ewes

    def __init__(self, i, environment, agents, ram=False, x=None, y=None, age=5):
        self.i = deepcopy(i)
        self.environment = environment
        self.agents = agents
        self.age = age
        self.ram = ram
        self.old_x = 0  # make sure defined inside init. This is not a default
        self.old_y = 0  # make sure defined inside init

        # print(f'{len( self.agents)=}')
        self.store = 0
        if x:
            self.x = x
        else:
            self.x = random.randint(0, 99)

        if y:
            self.y = y
        else:
            self.y = random.randint(0, 99)
            # self.y = 99 # test for torus movement

        print(f'{self=}')

    def __str__(self):
        """ Just a nice way of printing out the variables associated with each agent class"""
        return "i=" + str(self.i) + ", store=" + str(self.store) \
               + ", x=" + str(self.x) + ", y=" + str(self.y)

    def move(self):
        print(f'move: {len(self.agents)=}')

        self.old_x = deepcopy(self.x)

        self.old_y = deepcopy(self.y)

        movement = 1
        if self.ram:
            movement = Agent.ram_movement

        if random.random() < 0.5:
            self.x = (self.x + movement) % 100
        else:
            self.x = (self.x - movement) % 100

        # change y coordinate
        if random.random() < 0.5:
            self.y = (self.y + movement) % 100
        else:
            self.y = (self.y - movement) % 100

        print(f'({self.old_x}, {self.old_y}) --> ({self.x}, {self.y})')

    def eat(self):
        # agents to eat the environemnt
        print(f'{self.environment[self.y][self.x]=}')

        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0

        if self.store >= 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0

    def share_with_neighbours(self, neighbourhood, breeding_distance):
        print(f'we was ere {len(self.agents)}')
        # sharing with neighbours
        # Loop through the agents in self.agents

        print(f'{len(self.agents)=}')

        for i in range(len(self.agents)):
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(self.agents[i])
            print(f'distance = {distance}')

            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Sum self.store and agent.store .
                # Divide sum by two to calculate average.

                print(f'{self.store=} {self.agents[i].store=}')
                if self.store != self.agents[i].store:
                    ave = (self.store + self.agents[i].store) / 2
                    self.store = ave
                    self.agents[i].store = ave
                    print(f"sharing  {str(distance)} {str(ave)} {i=} {self.i=}")
                else:
                    print(f"we didn't need to share {self.store=} {i=} {self.i=}")

                # if distance is less than breeding distance between ram and ewe
                # and agents are older than 5 = breed function
                if distance <= breeding_distance:
                    if self.age > 5 and self.agents[i].age > 5 and self.i != i and (self.ram or self.agents[i].ram):
                        if self.ram and self.agents[i].ram:  # We don't want two rams
                            print(f'no breeding.. two rams {self.age=} {self.agents[i].age=}')
                        else:
                            print(f'time to breed {self.age=} {self.ram=} {self.agents[i].age=} {self.agents[i].ram=}')
                            self.breed(breed_with=i)
                            Agent.counter += 1 
                            if Agent.counter > 200:
                                pass
                                # exit(5)

                elif self.age <= 5 or self.agents[i].age <= 5: # aged 5 or less = too young
                    print(f'no breeding this time - too young {self.age=} {self.agents[i].age=}')

                elif self.i == i: # can't breed with self
                    print(f"can't breed with yourself {self.age=} {self.agents[i].age}")

    def breed(self, breed_with):
        """
        If we get breedingbetween a ram and a ewe. The lambs will come into existence at the same
        location as the mother.
        :param breed_with: This is the number of the other Agent we are breeding with
        :type breed_with:
        :return:
        :rtype:
        """

        # one of these will definitely be a ram as we can't come into this method otherwise
        if not self.ram:
            breeding_x, breeding_y = (self.x, self.y)
        else:
            breeding_x, breeding_y = (self.agents[breed_with].x, self.agents[breed_with].y)

        # breeding_x, breeding_y = (50, 50)  # for testing
        print(f'{breed_with=} {self.i=}')

        # add new agent to the list of agents, but with specific co-ordinates (mothers location)
        # specify age of zero for lambs so they can't breed until they are 5
        number_of_lambs = random.choice([1, 1, 1, 1, 1, 2, 2, 2, 3, 0, 0])  # random choice for number of lambs born
        breeding_failure = False

        print(f'{number_of_lambs=}')
        if number_of_lambs == 0:  # 0 lambs = breeding failure
            print(f'breeding failure. Too bad!!! {self.age=} {self.agents[breed_with].age=}')
            breeding_failure = True
            # exit(9)

        for i in range(number_of_lambs):
            print(f'getting {number_of_lambs} lambs {self.age=} {self.agents[breed_with].age=}')
            new_lamb_gender = random.choice([True, False])  # random choice for lamb gender
            # add new lamb(s) to list of agents. age = 0, gender is random.
            self.agents.append(Agent(len(self.agents), self.environment, self.agents, x=breeding_x, y=breeding_y,
                                     age=0, ram=new_lamb_gender))

        # if breeding failure mother age returns to 5 so can breed again.
        # if mother bred, age resets to 0 to wait 5 times before breeding again
        if not self.ram and not breeding_failure:
            self.age = 0

        if not self.agents[breed_with].ram and not breeding_failure:
            self.agents[breed_with].age = 0

        print(f'{breed_with=} ')
        # exit(0)

    # distance calculation - due to torus, distance is calculated in both
    # directions to ensure smallest distance
    def distance_between(self, b):
        print(f'{self.x=} {self.y=} {b.x=} {b.y=}')
        x_distance = abs(self.x - b.x)  # default
        y_distance = abs(self.y - b.y)  # default

        if x_distance > 50:
            x_distance = 100 - x_distance

        if y_distance > 50:
            y_distance = 100 - y_distance

        print(f'{x_distance=} {y_distance=}')

        return round((float((x_distance ** 2) + (y_distance) ** 2)) ** 0.5, 2)