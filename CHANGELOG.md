<!---
#######################################
## Server-Monitor Changelog
##
## Format: markdown (md)
## Latest versions should be placed as first
##
## Notation: 0.1.2
##      - 0: stable released version
##      - 1: new features
##      - 2: bug fixes and small changes
##
## Updating schema (mandatory):
##      <empty_line>
##      <version> (dd/mm/rrrr)
##      ----------------------
##      * <item>
##      * <item>
##      <empty_line>
##
## Useful tutorial: https://en.support.wordpress.com/markdown-quick-reference/
##
#######################################
-->
0.0.2 (11/04/2019)
------------------
* Changed: added stripping the lines from file
* Added: src.system_data.meminfo module for obtaining a memory data

0.0.1 (11/04/2019)
------------------
* Added: CHANGELOG.md, requirements.txt files
* Added: basic .hound.yml configuration
* Added: configured .pylintrc file
* Added: basic Dockerfile for development purpose
* Added: src.system_data package for backend - gathering a system data
* Added: src.common.py for various helpers and constant variables
* Added: src.exceptions  module with SystemFileReadError custom exception
* Added: src.system_data.base_systeminfo with BaseSystemInfo abstract class
