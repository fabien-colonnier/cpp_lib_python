project(Test)

add_library(function_lib SHARED src/function_simple.cpp)

add_executable(prog src/Struct_test.cpp)

target_include_directories(function_lib PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

target_include_directories(prog PUBLIC 
    ${CMAKE_CURRENT_SOURCE_DIR}/include/
)
target_link_libraries(prog function_lib)

target_compile_features(function_lib PUBLIC cxx_std_11)

install(TARGETS function_lib DESTINATION lib)
install(TARGETS prog DESTINATION bin)