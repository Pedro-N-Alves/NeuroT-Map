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

# Run the command 'NeuroTmap_lesion_int_nt.sh'
cmd_lesion_int_nt ='./NeuroTmap_lesion_int_nt_subcircuits.sh '+str(lesions_args)

# Function to calculate the pre and postsynaptic ratios
def individual_profile():
    for lesion in args.lesions:
        # Import the .csv file generated in the 'NeuroTmap_lesion_int_nt.sh' command
        # 'recep_inj' refers to the receptor location density map voxels intersected by the lesion
        # 'trans_inj' refers to the transporter location density map voxels intersected by the lesion
        # 'recep_tract_inj' refers to the receptor white matter projection map voxels intersected by the lesion
        # 'trans_tract_inj' refers to the transporter white matter projection map voxels intersected by the lesion
        tab=pd.read_csv('output_subcircuits_'+str(lesion)+'.csv', sep=" ", index_col=0)

        all_inj = tab.loc['injuries', ['A4B2_basalforebrain_loc', 'M1_basalforebrain_loc', 'VAChT_basalforebrain_loc', 'A4B2_pontomesencephalic_loc', 'M1_pontomesencephalic_loc', 'VAChT_pontomesencephalic_loc', 'D1_mesocorticolimbic_loc', 'D2_mesocorticolimbic_loc', 'DAT_mesocorticolimbic_loc', 'D1_nigrostriatal_loc', 'D2_nigrostriatal_loc', 'DAT_nigrostriatal_loc']]
        all_tot = tab.loc['totals', ['A4B2_basalforebrain_loc', 'M1_basalforebrain_loc', 'VAChT_basalforebrain_loc', 'A4B2_pontomesencephalic_loc', 'M1_pontomesencephalic_loc', 'VAChT_pontomesencephalic_loc', 'D1_mesocorticolimbic_loc', 'D2_mesocorticolimbic_loc', 'DAT_mesocorticolimbic_loc', 'D1_nigrostriatal_loc', 'D2_nigrostriatal_loc', 'DAT_nigrostriatal_loc']]
        all_perc = all_inj/all_tot*100

        all_tract_inj = tab.loc['injuries', ['A4B2_basalforebrain_con', 'M1_basalforebrain_con', 'VAChT_basalforebrain_con', 'A4B2_pontomesencephalic_con', 'M1_pontomesencephalic_con', 'VAChT_pontomesencephalic_con', 'D1_mesocorticolimbic_con', 'D2_mesocorticolimbic_con', 'DAT_mesocorticolimbic_con', 'D1_nigrostriatal_con', 'D2_nigrostriatal_con', 'DAT_nigrostriatal_con']]
        all_tract_tot = tab.loc['totals', ['A4B2_basalforebrain_con', 'M1_basalforebrain_con', 'VAChT_basalforebrain_con', 'A4B2_pontomesencephalic_con', 'M1_pontomesencephalic_con', 'VAChT_pontomesencephalic_con', 'D1_mesocorticolimbic_con', 'D2_mesocorticolimbic_con', 'DAT_mesocorticolimbic_con', 'D1_nigrostriatal_con', 'D2_nigrostriatal_con', 'DAT_nigrostriatal_con']]
        all_tract_perc = all_tract_inj/all_tract_tot*100
        
        all_max_inj = tab.loc['injuries', ['A4B2_basalforebrain_max', 'M1_basalforebrain_max', 'VAChT_basalforebrain_max', 'A4B2_pontomesencephalic_max', 'M1_pontomesencephalic_max', 'VAChT_pontomesencephalic_max', 'D1_mesocorticolimbic_max', 'D2_mesocorticolimbic_max', 'DAT_mesocorticolimbic_max', 'D1_nigrostriatal_max', 'D2_nigrostriatal_max', 'DAT_nigrostriatal_max']]
        all_max_tot = tab.loc['totals', ['A4B2_basalforebrain_max', 'M1_basalforebrain_max', 'VAChT_basalforebrain_max', 'A4B2_pontomesencephalic_max', 'M1_pontomesencephalic_max', 'VAChT_pontomesencephalic_max', 'D1_mesocorticolimbic_max', 'D2_mesocorticolimbic_max', 'DAT_mesocorticolimbic_max', 'D1_nigrostriatal_max', 'D2_nigrostriatal_max', 'DAT_nigrostriatal_max']]
        all_max_perc = all_tract_inj/all_tract_tot*100

        recep_inj = tab.loc['injuries', ['A4B2_basalforebrain_loc', 'M1_basalforebrain_loc', 'A4B2_pontomesencephalic_loc', 'M1_pontomesencephalic_loc', 'D1_mesocorticolimbic_loc', 'D2_mesocorticolimbic_loc', 'D1_nigrostriatal_loc', 'D2_nigrostriatal_loc']]
        recep_tot = tab.loc['totals', ['A4B2_basalforebrain_loc', 'M1_basalforebrain_loc', 'A4B2_pontomesencephalic_loc', 'M1_pontomesencephalic_loc', 'D1_mesocorticolimbic_loc', 'D2_mesocorticolimbic_loc', 'D1_nigrostriatal_loc', 'D2_nigrostriatal_loc']]
        recep_perc = recep_inj/recep_tot*100

        trans_inj = tab.loc['injuries', ['VAChT_basalforebrain_loc', 'VAChT_basalforebrain_loc', 'VAChT_pontomesencephalic_loc', 'VAChT_pontomesencephalic_loc', 'DAT_mesocorticolimbic_loc', 'DAT_mesocorticolimbic_loc', 'DAT_nigrostriatal_loc', 'DAT_nigrostriatal_loc']]
        trans_tot = tab.loc['totals', ['VAChT_basalforebrain_loc', 'VAChT_basalforebrain_loc', 'VAChT_pontomesencephalic_loc', 'VAChT_pontomesencephalic_loc', 'DAT_mesocorticolimbic_loc', 'DAT_mesocorticolimbic_loc', 'DAT_nigrostriatal_loc', 'DAT_nigrostriatal_loc']]
        trans_perc = trans_inj/trans_tot*100

        recep_tract_inj = tab.loc['injuries', ['A4B2_basalforebrain_con', 'M1_basalforebrain_con', 'A4B2_pontomesencephalic_con', 'M1_pontomesencephalic_con', 'D1_mesocorticolimbic_con', 'D2_mesocorticolimbic_con', 'D1_nigrostriatal_con', 'D2_nigrostriatal_con']]
        recep_tract_tot = tab.loc['totals', ['A4B2_basalforebrain_con', 'M1_basalforebrain_con', 'A4B2_pontomesencephalic_con', 'M1_pontomesencephalic_con', 'D1_mesocorticolimbic_con', 'D2_mesocorticolimbic_con', 'D1_nigrostriatal_con', 'D2_nigrostriatal_con']]
        recep_tract_perc = recep_tract_inj/recep_tract_tot*100

        trans_tract_inj = tab.loc['injuries', ['VAChT_basalforebrain_con', 'VAChT_basalforebrain_con', 'VAChT_pontomesencephalic_con', 'VAChT_pontomesencephalic_con', 'DAT_mesocorticolimbic_con', 'DAT_mesocorticolimbic_con', 'DAT_nigrostriatal_con', 'DAT_nigrostriatal_con']]
        trans_tract_tot = tab.loc['totals', ['VAChT_basalforebrain_con', 'VAChT_basalforebrain_con', 'VAChT_pontomesencephalic_con', 'VAChT_pontomesencephalic_con', 'DAT_mesocorticolimbic_con', 'DAT_mesocorticolimbic_con', 'DAT_nigrostriatal_con', 'DAT_nigrostriatal_con']]
        trans_tract_perc = trans_tract_inj/trans_tract_tot*100
        
        recep_max_inj = tab.loc['injuries', ['A4B2_basalforebrain_max', 'M1_basalforebrain_max', 'A4B2_pontomesencephalic_max', 'M1_pontomesencephalic_max', 'D1_mesocorticolimbic_max', 'D2_mesocorticolimbic_max', 'D1_nigrostriatal_max', 'D2_nigrostriatal_max']]
        recep_max_tot = tab.loc['totals', ['A4B2_basalforebrain_max', 'M1_basalforebrain_max', 'A4B2_pontomesencephalic_max', 'M1_pontomesencephalic_max', 'D1_mesocorticolimbic_max', 'D2_mesocorticolimbic_max', 'D1_nigrostriatal_max', 'D2_nigrostriatal_max']]
        recep_max_perc = recep_tract_inj/recep_tract_tot*100

        trans_max_inj = tab.loc['injuries', ['VAChT_basalforebrain_max', 'VAChT_basalforebrain_max', 'VAChT_pontomesencephalic_max', 'VAChT_pontomesencephalic_max', 'DAT_mesocorticolimbic_max', 'DAT_mesocorticolimbic_max', 'DAT_nigrostriatal_max', 'DAT_nigrostriatal_max']]
        trans_max_tot = tab.loc['totals', ['VAChT_basalforebrain_max', 'VAChT_basalforebrain_max', 'VAChT_pontomesencephalic_max', 'VAChT_pontomesencephalic_max', 'DAT_mesocorticolimbic_max', 'DAT_mesocorticolimbic_max', 'DAT_nigrostriatal_max', 'DAT_nigrostriatal_max']]
        trans_max_perc = trans_tract_inj/trans_tract_tot*100

		# Create the plot with: 
		# the percentage of each neurotransmitter system disrupted by the lesion, according to the receptor and transporter location density (location maps injury; left upper plot) and white matter projections (tract maps injury; left bottom plot)
		# the synaptic ratios presented in a natural logarithmic scale (right plot)
        fig = plt.figure(figsize=(16, 12))
        ax1 = fig.add_subplot(221, projection='polar')
        ax2 = fig.add_subplot(223, projection='polar')
        ax3 = fig.add_subplot(122, projection='polar')

        # Percentage of each neurotransmitter system disrupted by the lesion, according to the receptor and transporter location density (location maps injury)
        width1 = 2 * np.pi/12 - 2 * np.pi/12 * 0.1
        theta1 = np.arange(0, 2 * np.pi, 2 * np.pi/12)
        colors1 = ["#B7DEDA", "#92CEC8", "#6BBDB5"]
        radii1 = all_perc
        ax1.bar(theta1, radii1, width=width1, bottom=0.0, color=colors1, alpha=1, edgecolor='dimgray')
        ax1.yaxis.set_major_formatter('{x:1.3f}%')
        if radii1.max() != 0:
        	ax1.set_yticks(np.arange(0, radii1.max(), radii1.max()/5))
        ax1.set_rlabel_position(0)
        ax1.set_xticks(theta1)
        ax1.set_xticklabels(['A4B2_basalforebrain', 'M1_basalforebrain', 'VAChT_basalforebrain', 'A4B2_pontomesencephalic', 'M1_pontomesencephalic', 'VAChT_pontomesencephalic', 'D1R_mesocorticolimbic', 'D2R_mesocorticolimbic', 'DAT_mesocorticolimbic', 'D1R_nigrostriatal', 'D2R_nigrostriatal', 'DAT_nigrostriatal'])
        ax1.set_title('receptor/transporter lesion')
        ax1.set_theta_offset(np.pi/2)
        ax1.set_theta_direction(-1)

        # Percentage of each neurotransmitter system disrupted by the lesion, according to the white matter projections (tract maps injury)
        width2 = 2 * np.pi/12 - 2 * np.pi/12 * 0.1
        theta2 = np.arange(0, 2 * np.pi, 2 * np.pi/12)
        colors2 = ["#B7DEDA", "#92CEC8", "#6BBDB5"]
        radii2 = all_tract_perc
        ax2.bar(theta2, radii2, width=width2, bottom=0.0, color=colors2, alpha=1, edgecolor='dimgray')
        ax2.yaxis.set_major_formatter('{x:1.3f}%')
        if radii2.max() != 0:
        	ax2.set_yticks(np.arange(0, radii2.max(), radii2.max()/5))
        ax2.set_rlabel_position(0)
        ax2.set_xticks(theta2)
        ax2.set_xticklabels(['A4B2_basalforebrain', 'M1_basalforebrain', 'VAChT_basalforebrain', 'A4B2_pontomesencephalic', 'M1_pontomesencephalic', 'VAChT_pontomesencephalic', 'D1R_mesocorticolimbic', 'D2R_mesocorticolimbic', 'DAT_mesocorticolimbic', 'D1R_nigrostriatal', 'D2R_nigrostriatal', 'DAT_nigrostriatal'])
        ax2.set_title('receptor/transporter disconnection')
        ax2.set_theta_offset(np.pi/2)
        ax2.set_theta_direction(-1)

        # Synaptic ratios presented in a natural logarithmic scale (right plot), according to the formulas presented in the manuscript
        width3 = 2 * np.pi/12 - 2 * np.pi/12 * 0.1
        theta3 = np.arange(0, 2 * np.pi, 2 * np.pi/12)
        radii3a = []
        for i in range(len(recep_tract_perc)):
            if recep_max_perc[i] == 0:
                radii3a.append(float('inf'))
            else:
                radii3a.append(trans_max_perc[i]/recep_max_perc[i])
        radii3b = []
        for i in range(len(recep_tract_perc)):
            if trans_max_perc[i] == 0:
                radii3b.append(float('inf'))
            else:
                radii3b.append(recep_max_perc[i]/trans_max_perc[i])
        radii3b = [(radii3b[0]+radii3b[1])/2, (radii3b[2]+radii3b[3])/2, (radii3b[4]+radii3b[5])/2, (radii3b[6]+radii3b[7])/2]
        radii3 = np.append(radii3a, radii3b)
        colors3 = []
        for i in range(len(radii3)):
            if radii3[i] > 1:
                colors3.append((0.42,0.74,0.71,1))
            else:
                colors3.append((0.96,0.95,0.70,1))
        radii3=np.log(radii3)
        radii3_inf_changed = np.where(radii3==-np.inf, -10, radii3)
        radii3_inf_changed = np.where(radii3_inf_changed==np.inf, 10,  radii3_inf_changed)
        ax3.bar(theta3, radii3_inf_changed, width=width3, bottom=0.0, color=colors3, edgecolor='dimgray')
        ax3.set_ylim([-1, 1])
        ax3.set_yticks([np.floor(radii3_inf_changed.min()), np.floor(radii3_inf_changed.min())/2, 0, np.ceil(radii3_inf_changed.max())/2, np.ceil(radii3_inf_changed.max())])
        ax3.set_rlabel_position(0)
        ax3.set_xticks(theta3)
        ax3.set_xticklabels(['A4B2_basalforebrain presynaptic', 'M1_basalforebrain presynpatic', 'VAChT_basalforebrain postsynaptic', 'A4B2_pontomesencephalic presynaptic', 'M1_pontomesencephalic presynaptic', 'VAChT_pontomesencephalic postsynaptic', 'D1_mesocorticolimbic presynaptic', 'D2_mesocorticolimbic presynaptic', 'DAT_mesocorticolimbic postsynaptic', 'D1_nigrostriatal presynaptic', 'D2_nigrostriatal presynaptic', 'DAT_nigrostriatal postsynaptic'])
        ax3.set_title('Pre/pos synaptic ratios')
        ax3.set_theta_offset(np.pi/2)
        ax3.set_theta_direction(-1)

		# Create output_les_dis_'lesion_name'.csv (please see README file for more details)
        output_les_dis = np.vstack([all_inj, all_perc, all_tract_inj, all_tract_perc])
        output_les_dis = pd.DataFrame(output_les_dis, columns=['A4B2_basalforebrain', 'M1_basalforebrain', 'VAChT_basalforebrain', 'A4B2_pontomesencephalic', 'M1_pontomesencephalic', 'VAChT_pontomesencephalic', 'D1_mesocorticolimbic', 'D2_mesocorticolimbic', 'DAT_mesocorticolimbic', 'D1R_nigrostriatal', 'D2R_nigrostriatal', 'DAT_nigrostriatal'], index=['loc_inj_'+str(lesion), 'loc_inj_perc_'+str(lesion), 'tract_inj_'+str(lesion), 'tract_inj_perc_'+str(lesion)])
        output_les_dis.to_csv('output_les_dis_subcircuits_'+str(lesion)+'_v3.0.csv', sep=" ", header=True, index=True)
	
		# Create output_pre_post_synaptic_ratio_'lesion_name'.csv (please see README file for more details)
        pre_pos_ratio = pd.DataFrame(radii3, index=['A4B2_basalforebrain presynaptic', 'M1_basalforebrain presynpatic', 'VAChT_basalforebrain postsynaptic', 'A4B2_pontomesencephalic presynaptic', 'M1_pontomesencephalic presynaptic', 'VAChT_pontomesencephalic postsynaptic', 'D1_mesocorticolimbic presynaptic', 'D2_mesocorticolimbic presynaptic', 'DAT_mesocorticolimbic postsynaptic', 'D1_nigrostriatal presynaptic', 'D2_nigrostriatal presynaptic', 'DAT_nigrostriatal postsynaptic'], columns=['pre_pos_ratio_'+str(lesion)])
        pre_pos_ratio = pre_pos_ratio.transpose()
        pre_pos_ratio.to_csv('output_pre_post_synaptic_ratio_subcircuits_'+str(lesion)+'_v3.0.csv', sep=" ", header=True, index=True)
        pre_pos_ratio = pd.DataFrame(radii3_inf_changed, index=['A4B2_basalforebrain presynaptic', 'M1_basalforebrain presynpatic', 'VAChT_basalforebrain postsynaptic', 'A4B2_pontomesencephalic presynaptic', 'M1_pontomesencephalic presynaptic', 'VAChT_pontomesencephalic postsynaptic', 'D1_mesocorticolimbic presynaptic', 'D2_mesocorticolimbic presynaptic', 'DAT_mesocorticolimbic postsynaptic', 'D1_nigrostriatal presynaptic', 'D2_nigrostriatal presynaptic', 'DAT_nigrostriatal postsynaptic'], columns=['pre_pos_ratio_'+str(lesion)])
        pre_pos_ratio = pre_pos_ratio.transpose()
        pre_pos_ratio.to_csv('output_pre_post_synaptic_ratio_inf_changed_subcircuits_'+str(lesion)+'_v3.0.csv', sep=" ", header=True, index=True)

		# Create output_'lesion_name'.png (please see README file for more details)
        plt.savefig('output_subcircuits_'+str(lesion)+'_v3.0.png', bbox_inches='tight')
        plt.clf()
        
        # Remove .csv file generated in the 'NeuroTmap_lesion_int_nt.sh' command
        os.remove('output_subcircuits_'+str(lesion)+'.csv')

subprocess.run(cmd_lesion_int_nt, shell=True)
individual_profile()

