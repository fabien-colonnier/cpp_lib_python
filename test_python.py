
import ctypes

# get the library
lib = ctypes.cdll.LoadLibrary('./build/libfunction_lib.so')

# set the argument of the c function to ensure compatibility with python
lib.create.restype = ctypes.c_void_p
lib.set_a.argtypes = [ ctypes.c_void_p, ctypes.c_int ]
lib.process.argtypes = [ ctypes.c_void_p ]
lib.get_a.argtypes = [ ctypes.c_void_p ]

class simple_p(object):
    def __init__(self):
        self.obj = lib.create()

    def set_(self, val):
        lib.set_a(self.obj, val)
    
    def process_(self):
        lib.process(self.obj)

    def get_(self):
        return lib.get_a(self.obj)

if __name__ == "__main__":
    # Load the shared library into ctypes
    # libname = pathlib.Path().absolute() / "libcmult.so"
    # c_lib = ctypes.CDLL(libname)

    
    t = simple_p()
    string_tp = input("read a val = ")
    a = int(string_tp)

    t.set_(a)
    t.process_()
    out = t.get_()

    print ("out = " + str(out))
