import copy
import random

class Hat:
    def __init__(self,**ball_with_number):
        # The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. 
        self.hat_info = {}
        self.contents = []
        for ball,number in ball_with_number.items():
            self.hat_info[ball] = number
            # add a number of ball to contents Ex. contents = ["red","red","green","blue","blue"]
            self.contents += [ ball for i in range(number) ]
            
    def draw(self,number):
        # This method should remove balls at random from contents and return those balls as a list of strings. 
        # The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. 
        # If the number of balls to draw exceeds the available quantity, return all the balls.
        drawed_list =[]
        contents = copy.deepcopy(self.contents)
        print("Draw methods : contents =>",contents)
        if(number < len(contents)):
            for i in range(number):
                random_index = random.randint(0,len(contents)-1)
                drawed_list.append(contents.pop(random_index))
        else:
            drawed_list.append(contents)
        return drawed_list

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    # hat: A hat object containing balls that should be copied inside the function.
    # expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment.
    # For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
    # num_balls_drawn: The number of balls to draw out of the hat in each experiment.
    # num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
    #* The experiment function should return a probability.
    hat = copy.deepcopy(hat)
    # M is the number of times that meet the expected balls condition
    M = 0
    ball_list = [ball for ball,number in expected_balls.items()]
    for i in range(num_experiments):
        count = { ball : 0 for ball in ball_list}
        meet_expected = 0
        drawed_list = hat.draw(num_balls_drawn)
        # Count number of drawed ball from the experiment
        for ball in drawed_list:
            if (ball in ball_list):
                count[ball] += 1
        # checking number of ball from the experiment
        for ball in count : 
            if count[ball] >= expected_balls[ball]:
                meet_expected += 1
        if(meet_expected == len(expected_balls)):
            M += 1
    return M/num_experiments

    

# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat = Hat(black=6, red=4, green=3)
print(hat.contents)
print(hat.hat_info)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)