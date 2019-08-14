import warnings

warnings.simplefilter('always',UserWarning)

class my_vec:
    def __init__(self,arg=None):
        self.vector=list()
        if '__iter__' in dir(arg):
            self.vector=list(arg)
            #for i in arg:
            #    self.vector.append(i)
        elif(arg is not None):
            self.vector.append(arg)
    def print_vec(self):
        print('VECTOR with length {0}'.format(len(self.vector)))
        print(self.vector)
    def mean_vec(self):
        if self.vector:
            return my_vec(sum(self.vector)/len(self.vector))
        else:
            return my_vec()
    def add_vec(self,vec=None):
        if vec is None:
            vector=list()
        elif type(vec) is my_vec:
            vector=vec.vector.copy()
        elif '__iter__' in dir(vec):
            vector=list(vec)
        else:
            vector=list()
            vector.append(vec)
        if len(self.vector)==len(vector):
            for i in range(len(vector)):
                vector[i]+=self.vector[i]
            return my_vec(vector)
        else:
            warnings.warn('The lengths of two vectors are different',UserWarning)
            #raise UserWarning('The lengths of two vectors are different')
    def inner_prod(self,vec=None):
        if vec is None:
            vector=list()
        elif type(vec) is my_vec:
            vector=vec.vector.copy()
        elif '__iter__' in dir(vec):
            vector=list(vec)
        else:
            vector=list()
            vector.append(vec)
        if len(self.vector)==len(vector):
            for i in range(len(vector)):
                vector[i]*=self.vector[i]
            return my_vec(sum(vector))
        else:
            warnings.warn('The lengths of two vectors are different',UserWarning)
            #raise UserWarning('The lengths of two vectors are different')
    def cross_prod(self,vec=None):
        if vec is None:
            vector=list()
        elif type(vec) is my_vec:
            vector=vec.vector.copy()
        elif '__iter__' in dir(vec):
            vector=list(vec)
        else:
            vector=list()
            vector.append(vec)
        if len(self.vector)==len(vector)==3:
            pass
        else:
            pass


vec1=my_vec()
vec1.print_vec()

vec2=my_vec(.8)
vec2.print_vec()

vec3=my_vec([1,2,3])
vec3.print_vec()

my_vec().mean_vec().print_vec()
vec1.mean_vec().print_vec()
vec2.mean_vec().print_vec()
vec3.mean_vec().print_vec()



vec2.add_vec()
vec2.add_vec(vec1)
vec2.add_vec(0.2).print_vec()
vec2.add_vec([0.2]).print_vec()
tmp=vec2.add_vec(my_vec(0.3))
tmp.print_vec()
vec4=my_vec([2,3,1])
a=vec3.add_vec(vec4)
a.print_vec()
vec3.print_vec();vec4.print_vec()
vec2.inner_prod()
vec3.inner_prod(vec4).print_vec()
vec4.inner_prod([1,2,3]).print_vec()
vec3.print_vec();vec4.print_vec()
