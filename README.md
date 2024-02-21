# shared library reusable in python

## compile the library
```
mkdir build
cd build

cmake ..
cmake --build .
```

## test the library in cpp
run `./prog` in `build` directory

## test the library in python
run `python3 test_python.py`