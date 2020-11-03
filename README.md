# Population Census Tract (Insights Data-Science Challenge question)

## Table of Contents
1. [Problem Statement](README.md#problem_statement)
1. [Usage Instructions](README.md#usage_instructions)
1. [Test](README.md#test)
1. [Complaints](README.md#complaints)

## Problem Statement
[Here](https://github.com/InsightDataScience/population-rollup/blob/master/README.md) is the full description of the problem.

Constructing the required report after processing the input file column names:
 
TRACT10 | CBSA09 | CBSA_T | POP00 | POP10 | PPCHG


CBSA09 | CBSA_T | No. of different TRACTs | Total(Population in 2000) | Total(Population in 2010) | Average Population Change %

*Output does not contain these column headers.*

## Usage Instructions

`python3 src/population.py [ (optional) -i '<input_file_name_with_path>' -o '<output_file_name_with_path>' ]`

* `<input_file_name_with_path>` - file name with relative path in linux style. No input filename defaults to `./input/censustract-00-10.csv`.
* `<output_file_name_with_path>` - file name with relative path in linux style. No output filename defaults to `./output/report.csv`.
## Test
`bash run.sh`
* Input filename should be `./input/censustract-00-10.csv`
* Output file goes in `./output/report.csv`

## Complaints
Email: [basak@purdue.edu](mailto:basak@purdue.edu)

### Disclaimer
Use at your own risk!