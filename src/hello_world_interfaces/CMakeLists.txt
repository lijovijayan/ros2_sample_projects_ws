cmake_minimum_required(VERSION 3.8)
project(hello_world_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

# newly added lines
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
	"msg/HelloWorld.msg"
	"srv/HelloWorld.srv"
)
ament_export_dependencies(rosidl_default_runtime)
# end - newly added lines

ament_package()
