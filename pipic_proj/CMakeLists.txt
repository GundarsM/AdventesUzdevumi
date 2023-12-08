cmake_minimum_required(VERSION 3.13)

# initialize the SDK based on PICO_SDK_PATH
# note: this must happen before project()
include(/home/gundars/Downloads/vs_code_projects/AdventesUzdevumi/pipico/pico-sdk/external/pico_sdk_import.cmake)

project(my_project C CXX ASM)

set(CMAK_C_STANDARD 11)
set(CMAKE_CXX_SATNDARD 17)

# initialize the Raspberry Pi Pico SDK
pico_sdk_init()

# rest of your project


add_executable(hello_world
    hello_world.c
)

# Add pico_stdlib library which aggregates commonly used features
target_link_libraries(hello_world pico_stdlib)

# create map/bin/hex/uf2 file in addition to ELF.
pico_add_extra_outputs(hello_world)
