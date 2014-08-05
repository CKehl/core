# Try to find the GMP libraries
# GMP_FOUND - system has GMP lib
# GMP_INCLUDE_DIR - the GMP include directory
# GMP_LIBRARIES_DIR - Directory where the GMP libraries are located
# GMP_LIBRARIES - the GMP libraries

include(FindPackageHandleStandardArgs)

# Is it already configured?
if (GMP_INCLUDE_DIR AND GMP_LIBRARIES)
  set(GMP_FOUND TRUE)
else()
  find_path(GMP_INCLUDE_DIR 
            NAMES gmp.h
            PATHS ${CMAKE_SOURCE_DIR}/builds/gmp/include
                  ENV GMP_INC_DIR
            DOC "The directory containing the GMP header files"
           )
  find_library(GMP_LIBRARIES NAMES gmp 
               PATHS ENV GMP_LIB_DIR ${CMAKE_SOURCE_DIR}/builds/gmp/lib
               DOC "Path to the GMP library"
               )
  find_package_handle_standard_args(GMP "DEFAULT_MSG" GMP_INCLUDE_DIR GMP_LIBRARIES_DIR)
endif()
