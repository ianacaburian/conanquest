cmake_minimum_required(VERSION 3.25)
project(conanquest VERSION 0.0.1)
find_package(JUCE CONFIG REQUIRED)
juce_add_console_app(${PROJECT_NAME}
    PRODUCT_NAME ${PROJECT_NAME})
target_sources(${PROJECT_NAME}
    PRIVATE
        src/Main.cpp)
target_compile_definitions(${PROJECT_NAME}
    PRIVATE
        JUCE_WEB_BROWSER=0
        JUCE_USE_CURL=0)  
target_link_libraries(${PROJECT_NAME}
    PRIVATE
        juce::juce_core
    PUBLIC
        juce::juce_recommended_config_flags
        juce::juce_recommended_warning_flags)

install(TARGETS ${PROJECT_NAME} DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
