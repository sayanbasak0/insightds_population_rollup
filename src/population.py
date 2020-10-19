#---------------------#
# Using bitbucket     #
# Author: Sayan Basak #
# Main file           #
#---------------------#

import csv
import sys
import os

def usage_help():
     
    input_file = './input/censustract-00-10.csv'
    output_file = './output/report.csv'
    col_sep = ','
    empty_cell = ''

    print("Usage:")
    print('python[3] src/population.py'+' -h                      : Usage help')
    print('                           '+' -i <input_file[.csv]>   : file name with relative path. No input defaults to '+str(repr(input_file)))
    print('                           '+' -o <output_file[.csv]>  : file name with relative path. No output defaults to '+str(repr(output_file)))
    
def main(argv, verbose=False):
    input_file = './input/censustract-00-10.csv'
    output_file = './output/report.csv'
    
    arguments = len(sys.argv) - 1
    if (verbose):
        arguments -= 1
    if (arguments%2):
        usage_help()
    else:
        for i in range(int((arguments)/2)):
            if (sys.argv[i*2+1] == '-i'):
                input_file = (sys.argv[i*2+2])
            elif (sys.argv[i*2+1] == '-o'):
                output_file = (sys.argv[i*2+2])
            else:
                usage_help()
                sys.exit()
    # create output folder if it does not exist
    os.makedirs(os.path.split(output_file)[0],exist_ok=True)
    
    
    # read lines extract required columns
    print('Input File: '+str(repr(input_file)))
    entries = {}
    columns = ['TRACT10','CBSA09','CBSA_T','POP00','POP10']
    
    with open(input_file, 'r') as file_i:
        row_stream = csv.reader(file_i, delimiter=',')
        header = True
        for row in row_stream:
            # print(row)
            if header:
                header = False
                column_i = [i for i,h in enumerate(row) if h in columns]
            else:
                entry_group = [row[i] for i in column_i[1:3]]
                entry_tract = row[column_i[0]]
                entry_sum = [int(row[i]) for i in column_i[3:5]]
                # group by CBSA
                group_name = ','.join(entry_group)
                if (group_name in entries.keys()):
                    # group by TRACT
                    if (entry_tract in entries[group_name][0].keys()):
                        for ei in range(len(entry_sum)):
                            entries[group_name][0][entry_tract][ei] += entry_sum[ei]
                    else:
                        entries[group_name][0][entry_tract] = []
                        for ei in range(len(entry_sum)):
                            entries[group_name][0][entry_tract].append(entry_sum[ei])
                else:
                    entries[group_name] = [{},[]]
                    for eg in entry_group:
                        entries[group_name][1].append(eg)
                    entries[group_name][0][entry_tract] = []
                    for ei in range(len(entry_sum)):
                        entries[group_name][0][entry_tract].append(entry_sum[ei])
    # process data
    processed_out = []
    for group_name in entries.keys():
        tracts = len(entries[group_name][0].keys())
        tmp_list = []
        tmp_list.extend(entries[group_name][1])
        tmp_list.append(tracts)
        tmp_list.extend([0,0,0])
        for tr in entries[group_name][0].keys():
            try:
                tmp_list[-1] += 100.0*(entries[group_name][0][tr][1]-entries[group_name][0][tr][0])/entries[group_name][0][tr][0]
            except:
                # division by zero remove data point
                tmp_list[-4] -= 1
                continue
            tmp_list[-3] += entries[group_name][0][tr][0]
            tmp_list[-2] += entries[group_name][0][tr][1]
        try:
            tmp_list[-1] = tmp_list[-1]/tmp_list[-4]
        except:
            # division by zero remove tract
            continue
        processed_out.append(tmp_list)
    # write lines
    with open(output_file, 'w', newline='') as file_o:
        out_stream = csv.writer(file_o, delimiter=',')
        for line in processed_out:
            out_stream.writerow(line[:-1]+["%.2f"%line[-1]])
    print('Output File: '+str(repr(output_file)))

if __name__ == "__main__":
    if (sys.argv[-1] == '-v'):
        main(sys.argv[1:], verbose=True)
    else:
        main(sys.argv[1:])