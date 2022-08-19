


def rotator(cap_dict_1 , cap_dict_2):
    pass

class CapData():
    def __init__(self , cap_list):
        self.cap_dict = {"R":[cap_list[0], cap_list[1]] ,\
        "Y":[cap_list[2], cap_list[3]],\
            "B":[cap_list[4], cap_list[5]]}
        
        self.R = self.cap_dict["R"]
        self.Y = self.cap_dict["Y"]
        self.B = self.cap_dict["B"]

    
    def __repr__(self) -> dict:
        return str(self.cap_dict)
    
    def calculate_total(self):
        # cap_dict = {"R":[cap_list[0], cap_list[1]] ,\
        #     "Y":[cap_list[2], cap_list[3]],\
        #         "B":[cap_list[4], cap_list[5]]}
        branch_total = 0
        for k in self.cap_dict.keys():
            if float(self.cap_dict[str(k)][0]) !=0 and float(self.cap_dict[str(k)][1]) !=0:
                branch_total += 1/float(self.cap_dict[str(k)][0]) + 1/float(self.cap_dict[str(k)][1])

        return branch_total
    
    def swap_R(self , X):
        temp = {
            (0,0): [CapData([X.R[0], ])]
        }

        self.R[0] 


    def get_diff(self , X):
        return abs(self.calculate_total() - X.calculate_total())


if __name__ == '__main__':
    x = CapData([12,12.5,12.3 , 12.4,12.5,12.1 ])
    print(x.calculate_total())

