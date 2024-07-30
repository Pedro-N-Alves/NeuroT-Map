# Import the necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import subprocess
import os

# Parse the command-line arguments (in this case, the name of the lesions, as explained in the README file)
parser = argparse.ArgumentParser()
parser.add_argument('lesions', metavar='lesions', nargs="+", help='list of lesions.')
args = parser.parse_args()
lesions_args = ' '.join(args.lesions)

# Run the command 'NeuroTmap_lesion_int_nt_datad.sh'
cmd_lesion_int_nt ='./NeuroTmap_lesion_int_nt_datad.sh '+str(lesions_args)

# Function to calculate the pre and postsynaptic ratios
def individual_profile():
    for lesion in args.lesions:
    	# Import the .csv file generated in the 'NeuroTmap_lesion_int_nt.sh' command
        # 'recep_inj' refers to the receptor location density map voxels intersected by the lesion
        # 'trans_inj' refers to the transporter location density map voxels intersected by the lesion
        # 'recep_tract_inj' refers to the receptor white matter projection map voxels intersected by the lesion
        # 'trans_tract_inj' refers to the transporter white matter projection map voxels intersected by the lesion
        tab=pd.read_csv('output_datad_'+str(lesion)+'.csv', sep=" ", index_col=0)

        all_inj = tab.loc['injuries', ['GABAa_loc', 'mGluR5_loc', 'MU_loc', 'H3_loc', 'CB1_loc']]
        all_tot = tab.loc['totals', ['GABAa_loc', 'mGluR5_loc', 'MU_loc', 'H3_loc', 'CB1_loc']]
        all_perc = all_inj/all_tot*100

        all_tract_inj = tab.loc['injuries', ['GABAa_con', 'mGluR5_con', 'MU_con', 'H3_con', 'CB1_con']]
        all_tract_tot = tab.loc['totals', ['GABAa_con', 'mGluR5_con', 'MU_con', 'H3_con', 'CB1_con']]
        all_tract_perc = all_tract_inj/all_tract_tot*100


		# Create the plot with: 
		# the percentage of each neurotransmitter system disrupted by the lesion, according to the receptor and transporter location density (location maps injury; upper plot) and white matter projections (tract maps injury; bottom plot)
		# the synaptic ratios presented in a natural logarithmic scale (right plot)
        fig = plt.figure(figsize=(16, 12))
        ax1 = fig.add_subplot(221, projection='polar')
        ax2 = fig.add_subplot(223, projection='polar')

        # Percentage of each neurotransmitter system disrupted by the lesion, according to the receptor and transporter location density (location maps injury)
        width1 = 2 * np.pi/5 - 2 * np.pi/5 * 0.1
        theta1 = np.arange(0, 2 * np.pi, 2 * np.pi/5)
        colors1 = ["#6184B1", "#ECC1FF", "#B5C695", "#FCC477", "#ED967C"]
        radii1 = all_perc
        ax1.bar(theta1, radii1, width=width1, bottom=0.0, color=colors1, alpha=1, edgecolor='dimgray')
        ax1.yaxis.set_major_formatter('{x:1.3f}%')
        ax1.set_yticks(np.arange(0, radii1.max(), radii1.max()/5))
        ax1.set_rlabel_position(0)
        ax1.set_xticks(theta1)
        ax1.set_xticklabels(['GABAa', 'mGluR5', 'MOR', 'H3R', 'CB1R'])
        ax1.set_title('receptor/transporter lesion')
        ax1.set_theta_offset(np.pi/2)
        ax1.set_theta_direction(-1)

        # Percentage of each neurotransmitter system disrupted by the lesion, according to the white matter projections (tract maps injury)
        width2 = 2 * np.pi/5 - 2 * np.pi/5 * 0.1
        theta2 = np.arange(0, 2 * np.pi, 2 * np.pi/5)
        colors2 = ["#6184B1", "#ECC1FF", "#B5C695", "#FCC477", "#ED967C"]
        radii2 = all_tract_perc
        ax2.bar(theta2, radii2, width=width2, bottom=0.0, color=colors2, alpha=1, edgecolor='dimgray')
        ax2.yaxis.set_major_formatter('{x:1.3f}%')
        ax2.set_yticks(np.arange(0, radii1.max(), radii1.max()/5))
        ax2.set_rlabel_position(0)
        ax2.set_xticks(theta2)
        ax2.set_xticklabels(['GABAa', 'mGluR5', 'MOR', 'H3R', 'CB1R'])
        ax2.set_title('receptor/transporter disconnection')
        ax2.set_theta_offset(np.pi/2)
        ax2.set_theta_direction(-1)

		# Create output_les_dis_datad_'lesion_name'.csv (please see README file for more details)
        output_les_dis = np.vstack([all_inj, all_perc, all_tract_inj, all_tract_perc])
        output_les_dis = pd.DataFrame(output_les_dis, columns=['GABAa', 'mGluR5', 'MU', 'H3', 'CB1'], index=['loc_inj_'+str(lesion), 'loc_inj_perc_'+str(lesion), 'tract_inj_'+str(lesion), 'tract_inj_perc_'+str(lesion)])
        output_les_dis.to_csv('output_les_dis_datad_'+str(lesion)+'.csv', sep=" ", header=True, index=True)

		# Create output_datad_'lesion_name'.png (please see README file for more details)
        plt.savefig('output_datad_'+str(lesion)+'.png', bbox_inches='tight')
        plt.clf()
        
        # Remove .csv file generated in the 'NeuroTmap_lesion_int_nt_datad.sh' command
        os.remove('output_datad_'+str(lesion)+'.csv')

subprocess.run(cmd_lesion_int_nt, shell=True)
individual_profile()

