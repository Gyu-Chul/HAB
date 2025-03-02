cmake_minimum_required(VERSION 3.10)
project(MyProject)

# C++ 표준 버전 설정 (필요에 따라 변경)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 디렉토리별로 모든 .cpp 파일을 찾는다.
file(GLOB_RECURSE SOURCE_FILES
    "${CMAKE_SOURCE_DIR}/*.cpp"  # main.cpp 등 루트에 있는 cpp 파일 포함
)

# 파일 이름이 CMakeCXXCompilerId.cpp로 끝나는 항목들을 제거
list(FILTER SOURCE_FILES EXCLUDE REGEX "CMakeCXXCompilerId\\.cpp$")

# 실행 파일 생성
add_executable(MyExecutable ${SOURCE_FILES})
