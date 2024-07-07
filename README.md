Welcome to NeuroT-Map!

With this tool you can chart how stroke damages neurotransmitter systems.

Manuscript: Alves PN, Nozais V, Hansen J, Corbetta M, Nachev P, Martins IP, Thiebaut de Schotten M (2024). Neurotransmitters’ white matter mapping unveils the neurochemical fingerprints of stroke. Research Square. https://doi.org/10.21203/rs.3.rs-3937453/v1

Hereby, we present the steps to use this tool:
1. Download the NeuroT-map zip file from git-hub and unzip it
2. Inside the generated folder ('NeuroT-Map-main'), create a folder named 'lesions'
3. Paste the stroke lesions you want to study inside the folder 'lesions'
- the lesions should be binary maps, normalized to the MNI152 152 2mm
- they should be in the NIFTI format
4. Run the python command NeuroTmap.py
- The required packages are: numpy, pandas, matplotlib, argparse, subprocess and os.
- The command line arguments should be the name of the lesions, separated by spaces, without the file extensions (i.e. .nii or .nii.gz)
- Example of a command line: 'python3 NeuroT-Map.py patient01 patient02 patient03'
5. Find the command outputs inside the main folder. The command will produce 3 outputs for each lesion:
- CSV file called output_les_dis_'lesion_name'. This file contains:
		 - the sum of the receptor or transporter location density map voxels intersected by the lesion (loc_inj_'lesion_name') 
		 - the percentage of the location density map intersected by the lesion, calculated by dividing the loc_inj_'lesion_name' value by the sum of all voxels of the receptor or transporter location density map * 100 (perc_loc_inj_'lesion_name')
		 - the sum of the receptor or transporter white matter projection map voxels intersected by the lesion (tract_inj_'lesion_name')
		 - the percentage of the white matter projection map intersected by the lesion, calculated by dividing the tract_inj_'lesion_name' value by the sum of all voxels of the receptor or transporter white matter projection map * 100 (perc_tract_inj_'lesion_name')
- CSV file called output_pre_post_synaptic_ratio_'lesion_name'. This file contains the pre and postsynaptic ratios of the studied neurotransmitter systems.
- PNG file called output_'lesion_name'. This image contains the graphs of:
		 - the percentage of each neurotransmitter system disrupted by the lesion, according to the receptor and transporter location density (location maps injury) and white matter projections (tract maps injury)
		 - the synaptic ratios presented in a natural logarithmic scale
		 
A supplemental data-driven analysis is also provided (please see the manuscript for more details).
You should follow the same steps but use the NeuroTmap_datad.py command instead.

If you have troubles or doubts, please contact: pedronascimentoalves@gmail.com 
