# evolution
Population genetics 

Implements simulation of drift and selection 

Usage 
Change the parameters in parameter.py, minding the python syntax 

run the script 
./experiment <destination folder> 

the resultant report, consiting of three files: 

- heatmap.html : heatmap view of the smulation 
- report.frequency : generation vs frequency report 
- report.frequency.transposed : transposition of report.frequency, used by the heatmap ggenerator 

will end up under 
<experiment_result>/<destination folder> 

If no <destination folder> is given the name will be generated out of 
experiment_<milliseconds> where <milliseconds> is generated by the script 

The behavior of the mutation can be changed at mutation.py, adding flavors and registering them in the function 
mutate(pop, size = 1, on = True, type = 'flat') 

where 
pop is the population, 
size is the number of members in the population subject to mutation 
on is a flag specifying if mutation will be introduced 
type is the flavor
