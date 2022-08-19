


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
    
    def swap_caps(self , X, phase):
        # temp = {
        #     (0,0): [CapData([X.R[0], ])]
        # }
        # self.R[0] 
        X = X.cap_dict
        copy_0_0 = self.cap_dict; copy_0_0[phase][0] = X[phase][0] 
        copy_0_0_X = X;  copy_0_0_X[phase][0]= self.cap_dict[phase][0]
        diff_0_0 = self.get_diff(copy_0_0_X)

        copy_0_1 = self.cap_dict; copy_0_1[phase][0] = X[phase][1] 
        copy_0_1_X = X;  copy_0_1_X[phase][1]= self.cap_dict[phase][0]
        diff_0_1 = self.get_diff(copy_0_1_X)

        copy_1_0 = self.cap_dict; copy_1_0[phase][1] = X[phase][0] 
        copy_1_0_X = X;  copy_1_0_X[phase][0]= self.cap_dict[phase][1]
        diff_1_0 = self.get_diff(copy_1_0_X)

        copy_1_1 = self.cap_dict; copy_1_1[phase][1] = X[phase][1] 
        copy_1_1_X = X;  copy_1_1_X[phase][1]= self.cap_dict[phase][1]
        diff_1_1 = self.get_diff(copy_1_1_X)
        
        return [diff_0_0 , diff_0_1, diff_1_0, diff_1_1]


    def get_diff(self , X):
        return abs(self.calculate_total() - X.calculate_total())
    
    # def executer(self):
    #     X = CapData([12,12.5,12.3 , 12.4,12.5,12.1 ])


if __name__ == '__main__':
    x = CapData([12,12.5,12.3 , 12.4,12.5,12.1 ])
    X =  CapData([12,12.5,12.3 , 12.4,12.5,12.1 ])
    v = x.swap_caps(X, "R")
    print(v)
    print(x.calculate_total())

