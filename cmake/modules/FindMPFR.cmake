# Try to find the MPFR libraries
# MPFR_FOUND - system has MPFR lib
# MPFR_INCLUDE_DIR - the MPFR include directory
# MPFR_LIBRARIES_DIR - Directory where the MPFR libraries are located
# MPFR_LIBRARIES - the MPFR libraries

include(FindPackageHandleStandardArgs)

# Is it already configured?
if (MPFR_INCLUDE_DIR AND MPFR_LIBRARIES)
  set(MPFR_FOUND TRUE)
else()
  find_path(MPFR_INCLUDE_DIR 
            NAMES mpfr.h 
            PATHS ${CMAKE_SOURCE_DIR}/builds/gmp/include
                  ENV MPFR_INC_DIR
            DOC "The directory containing the MPFR header files"
            )
  
  find_library(MPFR_LIBRARIES NAMES mpfr 
               PATHS ENV MPFR_LIB_DIR ${CMAKE_SOURCE_DIR}/builds/gmp/lib
               DOC "Path to the MPFR library"
               )
  find_package_handle_standard_args(MPFR "DEFAULT_MSG" MPFR_INCLUDE_DIR MPFR_LIBRARIES_DIR)
endif()

