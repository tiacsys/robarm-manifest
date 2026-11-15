# Docs build of the full linked set (D26). Run `curatrix docs full` from the workspace root;
# it calls cmake with the right build folder (build/full/docs) and strict options (D64c).
cmake_minimum_required(VERSION 3.20.0)
project(robarm-manifest-docs LANGUAGES)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE} COMPONENTS doc)
execute_process(COMMAND west topdir OUTPUT_VARIABLE WEST_TOPDIR
                OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ERROR_IS_FATAL ANY)
include(${WEST_TOPDIR}/xdmod/cmake/xdmod-docs.cmake)
xdmod_docs(REGISTRY ${CMAKE_CURRENT_LIST_DIR}/documents.yaml PROJECT_BASE ${CMAKE_CURRENT_LIST_DIR}/..)
