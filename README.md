# Gaussian_input_file_generate_kit

Some small tools help to generate gaussian calculation input files

1. DFT_energy_script.py

A script to automatically write Gaussian single point energy calculcation input file .gjf for given .sdf or other type mol files.


2. DFT_energy_script_read.py

A script to read a lots of gaussian single point energy calculation output files.


3. Maetsro_autorun.py

A script to generate all tyoes of running files to run MacroMOdel using command line in universtiy' module system.


Including:

(1)different types of files converter, from mol to sdf/mol2 etc. using openbabel. mol2/mol etc. to mae(maestro input structure file).

(2)minimation/conformational searching running command files(.com) generating function.

(3)generate running files command.

(4)output files converter, from -out.maegz to readable mol files like .sdf etc.



4. comfile.py

A script to generate Maestro running file .com file for cyclohexyl, which require more complicated structure read and write.



5. logfile.py

A script to read Maestro conformational searching output .log file. 




