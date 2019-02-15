import random

class Triangles:

    # creating a global class variable
    amount_of_triangles = 0

    # init function controls all other class functions
    def __init__(self, amount_to_generate):
        self.generate_amount = int(amount_to_generate)
        for amount in range(amount_to_generate):
            Triangles.create_side(self)
            Triangles.create_angle(self)
            Triangles.successful_triangles(self)
        print(f"After {amount_to_generate} attempts, {Triangles.amount_of_triangles} "
              f"were generated successfully.")



    def create_side(self):
        self.side_test = False
        side_one = random.randint(1, 100)
        side_two = random.randint(1, 100)
        side_three = random.randint(1, 100)
        if side_one + side_two >= side_three:
            if side_three + side_two >= side_one:
                if side_one + side_three >= side_two:
                    # only returns true if Triangle Inequality Theorem is true
                    self.side_test = True
        else:
            pass
        if self.side_test == True:
            return "Side created successfully"


    def create_angle(self):
        self.angle_test = False
        angle_one = random.randint(1, 120)
        angle_two = random.randint(1, 120)
        angle_three = random.randint(1, 120)
        if angle_one + angle_two + angle_three == 180: # to get very specific
            if angle_one + angle_two >= angle_three:
                if angle_three + angle_two >= angle_one:
                    if angle_one + angle_three >= angle_two:
                        self.angle_test = True
        else:
            pass
        if self.angle_test == True:
            return "Angle created successfully"

    def successful_triangles(self):
        self.angle = self.angle_test
        self.side = self.side_test
        if self.angle and self.side == True:
            Triangles.amount_of_triangles += 1

generate_triangles = Triangles(int(input("Enter amount to generate: ")))
