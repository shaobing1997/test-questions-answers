class Design:
    def __init__(self, name, lower_left_x, lower_left_y, upper_right_x, upper_right_y, polygon_count, md5sum):  #初始化类属性
        self.name = name
        self.lower_left_x = int(lower_left_x)
        self.lower_left_y = int(lower_left_y)
        self.upper_right_x = int(upper_right_x)
        self.upper_right_y = int(upper_right_y)
        self.polygon_count = int(polygon_count)
        self.md5sum = md5sum
        
        self.area = self.area_calculate(self.lower_left_x, self.lower_left_y, self.upper_right_x, self.upper_right_y)
        self.density = self.density_calculate(self.area, self.polygon_count)  #单位(polygons per mm^2)
        
    def get_name(self):
        return self.name
         
    #计算多边形面积
    def area_calculate(self, x_1, y_1, x_2, y_2): 
        l = x_2-x_1
        w = y_2-y_1
        area = l*w
        return area
    
    #计算多边形密度   
    def density_calculate(self, area, num):
        delta = 1e-06 
        temp = area*delta   #单位换算(um^2转换成mm^2)
        density = num/temp  
        return density

class Library:
    def __init__(self, file_name):
        self.design_list = list()
        
        #读取txt文件数据，并存储在列表data中
        data = list()
        with open(file_name,'r') as f:
            for line in f:
                data.append(line.strip().split("\t"))
        
        #遍历列表data，创建design实例并存储在列表design_list中
        for i in range(len(data)):
            if i == 0:
                continue
            design = Design(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6])
            self.design_list.append(design)
    
    #将design实例按照密度从大到小进行排序，并输出   
    def display(self):
        self.design_list.sort(key=lambda design: design.density,reverse = True) 
        for i in range(len(self.design_list)):
            print (self.design_list[i].name)
              
if __name__ == '__main__':
    library = Library('./testdata.txt')
    library.display()    