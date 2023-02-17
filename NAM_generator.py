import os

# Define the path to your original NAM file
nam_file = "S:\\02_Projects\\gs261_Otter_NBS\\08_MF\\in\\otrmf405\\otrmf405.nam"

# Define the path to your batch file
batch_file = "S:\\02_Projects\\gs261_Otter_NBS\\08_MF\\in\\otrmf_runs.bat"

# Define the strings to be replaced in NAM
nam_string_1 = 'LIST 6 ..\..\out\otrmf405\otrmf405.out'
nam_string_2 = 'BAS  1 ..\_BAS\otrmf299.bas'
nam_string_3 = 'WEL 12 ..\_WEL\OTRMF400.WEL'
nam_string_4 = 'OTRWR019\OTRWR019.rch'
nam_string_5 = 'OC  22 ..\_OC\otrmf297.oc'
nam_string_6 = 'OTRWR019\OTRWR019g.str'
nam_string_7 = 'DATA(BINARY) 50 ..\..\out\otrmf405\otrmf405.bud Direct 4'
nam_string_8 = 'DATA(BINARY) 57 ..\..\out\otrmf405\otrmf405.cs1 Direct 4'
nam_string_9 = 'DATA(BINARY) 30 ..\..\out\otrmf405\otrmf405.hds Direct 4'
nam_string_10 = 'DATA 61 ..\..\out\otrmf405\otr405b_rl.csv'

# Define the strings to be replaced in BATCH
batch_string_1 = 'in\otrmf406'
batch_string_2 = 'otrmf406.nam'

# Output batch directory
output_batch = "S:\\02_Projects\\gs261_Otter_NBS\\08_MF\\in"

#Input folders directory
prefix_in = "S:\\02_Projects\\gs261_Otter_NBS\\08_MF\\in\\otrmf"

#Output folders directory
prefix_out = "S:\\02_Projects\\gs261_Otter_NBS\\08_MF\\out\\otrmf"

# Loop over the number of copies to create new nam files
for i in range(21, 49):
    # Create input and output folders
    #folder_name_in = prefix_in + str(i+385)
    #folder_name_out = prefix_out + str(i+385)
    #os.makedirs(folder_name_in)
    #os.makedirs(folder_name_out)
    # Open the original file and load the contents into a Python object. Make sure there are the correct number of entries in batch file compared to for loop range.          
    with open(nam_file, 'r') as file:
        data = file.read()
        data = data.replace(nam_string_1, 'LIST 6 ..\..\out\otrmf{}\otrmf{}.out'.format(i+385, i+385))      
        data = data.replace(nam_string_2, 'BAS  1 ..\_BAS\otrmf406.bas')
        data = data.replace(nam_string_3, 'WEL 12 ..\_WEL\OTRMF406.WEL')
        data = data.replace(nam_string_4, 'OTRWR0{}\OTRWR0{}.rch'.format(i, i))
        data = data.replace(nam_string_5, 'OC  22 ..\_OC\otrmf406.oc')        
        data = data.replace(nam_string_6, 'OTRWR0{}\OTRWR0{}.str'.format(i, i))
        data = data.replace(nam_string_7, 'DATA(BINARY) 50 ..\..\out\otrmf{}\otrmf{}.bud Direct 4'.format(i+385, i+385))
        data = data.replace(nam_string_8, 'DATA(BINARY) 57 ..\..\out\otrmf{}\otrmf{}.cs1 Direct 4'.format(i+385, i+385)) 
        data = data.replace(nam_string_9, 'DATA(BINARY) 30 ..\..\out\otrmf{}\otrmf{}.hds Direct 4'.format(i+385, i+385))         
        data = data.replace(nam_string_10, 'DATA 61 ..\..\out\otrmf{}\otrmf{}_rl.csv'.format(i+385, i+385))        

    # Define directory and name of new YAML file
    new_file_name_template = "S:\\02_Projects\\gs261_Otter_NBS\\08_MF\\in\\otrmf{}\\otrmf{}.nam".format(i+385, i+385)

    # Write the modified contents to a new file
    new_file = new_file_name_template
    with open(new_file, "w") as f:
        f.write(data)