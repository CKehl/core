project(core++)

cmake_minimum_required(VERSION 2.4.5 FATAL_ERROR)

if(COMMAND cmake_policy)
  cmake_policy(SET CMP0003 NEW)
endif()

set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/modules)

find_package(GMP REQUIRED)
find_package(MPFR REQUIRED)

file(GLOB sources src/*.cpp src/gmpxx/*.cc)
file(GLOB sources_ext ext/*.cpp)
file(GLOB_RECURSE includes inc/*.h)

option(BUILD_SHARED_LIBS "Build as a shared library (vs. static library)." ON)

include_directories(${CMAKE_SOURCE_DIR}/inc ${GMP_INCLUDE_DIR} ${MPFR_INCLUDE_DIR})

add_library(core++_level1 ${sources} ${includes})
target_link_libraries(core++_level1 ${GMP_LIBRARIES} ${MPFR_LIBRARIES})
set_target_properties(core++_level1 PROPERTIES COMPILE_DEFINITIONS "CORE_LEVEL=1")

add_library(core++_level3 ${sources} ${includes})
target_link_libraries(core++_level3 ${GMP_LIBRARIES} ${MPFR_LIBRARIES})
set_target_properties(core++_level3 PROPERTIES COMPILE_DEFINITIONS "CORE_LEVEL=3")

macro(add_core_test target exsources)
  add_executable(${target}_level1 ${exsources} ${sources} ${sources_ext})
  target_link_libraries(${target}_level1 ${GMP_LIBRARIES} ${MPFR_LIBRARIES})
  set_target_properties(${target}_level1 PROPERTIES COMPILE_DEFINITIONS "CORE_LEVEL=1")
  
  add_executable(${target}_level3 ${exsources} ${sources} ${sources_ext})
  target_link_libraries(${target}_level3 ${GMP_LIBRARIES} ${MPFR_LIBRARIES})
  set_target_properties(${target}_level3 PROPERTIES COMPILE_DEFINITIONS "CORE_LEVEL=3")
endmacro()

include_directories(${CMAKE_SOURCE_DIR}/inc/CORE)

add_core_test(test_geom2d ${CMAKE_SOURCE_DIR}/ext/geom2d/test/tGeom2d.cpp)
add_core_test(test_geom2d_pentagon ${CMAKE_SOURCE_DIR}/ext/geom2d/test/pentagon.cpp)

add_core_test(test_geom3d ${CMAKE_SOURCE_DIR}/ext/geom3d/test/test.cpp)
add_core_test(test_geom3d2 ${CMAKE_SOURCE_DIR}/ext/geom3d/test/test2.cpp)