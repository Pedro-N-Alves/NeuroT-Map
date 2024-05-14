import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import subprocess
import csv

parser = argparse.ArgumentParser()
parser.add_argument('lesions', metavar='lesions', nargs="+", help='list of lesions.')
args = parser.parse_args()

lesions_args = ' '.join(args.lesions)
cmd_lesion_int_nt ='./NeuroTmap_lesion_int_nt_datad.sh '+str(lesions_args)

def individual_profile():
    for lesion in args.lesions:
        tab=pd.read_csv('output_'+str(lesion)+'.csv', sep=" ", index_col=0)

        all_inj = tab.loc['injuries_mm3', ['A4B2_loc', 'M1_loc', 'VAChT_loc', 'D1_loc', 'D2_loc', 'DAT_loc', 'NAT_loc', '5HT1a_loc', '5HT1b_loc', '5HT2a_loc', '5HT4_loc', '5HT6_loc', '5HTT_loc', 'GABAa_loc', 'mGluR5_loc', 'MU_loc', 'H3_loc', 'CB1_loc']]
        all_tot = tab.loc['totals_mm3', ['A4B2_loc', 'M1_loc', 'VAChT_loc', 'D1_loc', 'D2_loc', 'DAT_loc', 'NAT_loc', '5HT1a_loc', '5HT1b_loc', '5HT2a_loc', '5HT4_loc', '5HT6_loc', '5HTT_loc', 'GABAa_loc', 'mGluR5_loc', 'MU_loc', 'H3_loc', 'CB1_loc']]
        all_perc = all_inj/all_tot*100

        all_tract_inj = tab.loc['injuries_mm3', ['A4B2_con', 'M1_con', 'VAChT_con', 'D1_con', 'D2_con', 'DAT_con', 'NAT_con', '5HT1a_con', '5HT1b_con', '5HT2a_con', '5HT4_con', '5HT6_con', '5HTT_con', 'GABAa_con', 'mGluR5_con', 'MU_con', 'H3_con', 'CB1_con']]
        all_tract_tot = tab.loc['totals_mm3', ['A4B2_con', 'M1_con', 'VAChT_con', 'D1_con', 'D2_con', 'DAT_con', 'NAT_con', '5HT1a_con', '5HT1b_con', '5HT2a_con', '5HT4_con', '5HT6_con', '5HTT_con', 'GABAa_con', 'mGluR5_con', 'MU_con', 'H3_con', 'CB1_con']]
        all_tract_perc = all_tract_inj/all_tract_tot*100

        recep_inj = tab.loc['injuries_mm3', ['A4B2_loc', 'M1_loc', 'D1_loc', 'D2_loc', '5HT1a_loc', '5HT1b_loc', '5HT2a_loc', '5HT4_loc', '5HT6_loc']]
        recep_tot = tab.loc['totals_mm3', ['A4B2_loc', 'M1_loc', 'D1_loc', 'D2_loc', '5HT1a_loc', '5HT1b_loc', '5HT2a_loc', '5HT4_loc', '5HT6_loc']]
        recep_perc = recep_inj/recep_tot*100

        trans_inj = tab.loc['injuries_mm3', ['VAChT_loc', 'VAChT_loc', 'DAT_loc', 'DAT_loc', '5HTT_loc', '5HTT_loc', '5HTT_loc', '5HTT_loc', '5HTT_loc']]
        trans_tot = tab.loc['totals_mm3', ['VAChT_loc', 'VAChT_loc', 'DAT_loc', 'DAT_loc', '5HTT_loc', '5HTT_loc', '5HTT_loc', '5HTT_loc', '5HTT_loc']]
        trans_perc = trans_inj/trans_tot*100

        recep_tract_inj = tab.loc['injuries_mm3', ['A4B2_con', 'M1_con', 'D1_con', 'D2_con', '5HT1a_con', '5HT1b_con', '5HT2a_con', '5HT4_con', '5HT6_con']]
        recep_tract_tot = tab.loc['totals_mm3', ['A4B2_con', 'M1_con', 'D1_con', 'D2_con', '5HT1a_con', '5HT1b_con', '5HT2a_con', '5HT4_con', '5HT6_con']]
        recep_tract_perc = recep_tract_inj/recep_tract_tot*100

        trans_tract_inj = tab.loc['injuries_mm3', ['VAChT_con', 'VAChT_con', 'DAT_con', 'DAT_con', '5HTT_con', '5HTT_con', '5HTT_con', '5HTT_con', '5HTT_con']]
        trans_tract_tot = tab.loc['totals_mm3', ['VAChT_con', 'VAChT_con', 'DAT_con', 'DAT_con', '5HTT_con', '5HTT_con', '5HTT_con', '5HTT_con', '5HTT_con']]
        trans_tract_perc = trans_tract_inj/trans_tract_tot*100

        fig = plt.figure(figsize=(16, 12))
        ax1 = fig.add_subplot(221, projection='polar')
        ax2 = fig.add_subplot(223, projection='polar')
        ax3 = fig.add_subplot(122, projection='polar')

        #https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_margins.html
        #sphx-glr-gallery-subplots-axes-and-figures-axes-margins-py

        # Individual systems integrity - location maps injury

        width1 = 2 * np.pi/18 - 2 * np.pi/18 * 0.1
        theta1 = np.arange(0, 2 * np.pi, 2 * np.pi/18)
        colors1 = ["#B7B3D7", "#928CC1", "#6E66AD", "#B7DEDA", "#92CEC8", "#6BBDB5", "#EBA8B1", "#FCFCED", "#FBFAE2", "#F8F8D6", "#F8F6CB", "#F6F4BE", "#F5F2B3", "#6184B1", "#ECC1FF", "#B5C695", "#FCC477", "#ED967C"]
        radii1 = all_perc

        ax1.bar(theta1, radii1, width=width1, bottom=0.0, color=colors1, alpha=1, edgecolor='dimgray')
        ax1.yaxis.set_major_formatter('{x:1.3f}%')
        ax1.set_yticks(np.arange(0, radii1.max(), radii1.max()/5))
        ax1.set_rlabel_position(0)
        ax1.set_xticks(theta1)
        ax1.set_xticklabels(['A4B2R', 'M1R', 'VAChT', 'D1R', 'D2R', 'DAT', 'NAT', '5HT1aR', '5HT1bR', '5HT2aR', '5HT4R', '5HT6R', '5HTT', 'GABAa', 'mGluR5', 'MOR', 'H3R', 'CB1R'])
        ax1.set_title('receptor/transporter lesion')
        ax1.set_theta_offset(np.pi/2)
        ax1.set_theta_direction(-1)


        # Individual systems integrity - tract maps injury

        width2 = 2 * np.pi/18 - 2 * np.pi/18 * 0.1
        theta2 = np.arange(0, 2 * np.pi, 2 * np.pi/18)
        colors2 = ["#B7B3D7", "#928CC1", "#6E66AD", "#B7DEDA", "#92CEC8", "#6BBDB5", "#EBA8B1", "#FCFCED", "#FBFAE2", "#F8F8D6", "#F8F6CB", "#F6F4BE", "#F5F2B3", "#6184B1", "#ECC1FF", "#B5C695", "#FCC477", "#ED967C"]
        radii2 = all_tract_perc


        ax2.bar(theta2, radii2, width=width2, bottom=0.0, color=colors2, alpha=1, edgecolor='dimgray')
        ax2.yaxis.set_major_formatter('{x:1.3f}%')
        ax2.set_yticks(np.arange(0, radii1.max(), radii1.max()/5))
        ax2.set_rlabel_position(0)
        ax2.set_xticks(theta2)
        ax2.set_xticklabels(['A4B2R', 'M1R', 'VAChT', 'D1R', 'D2R', 'DAT', 'NAT', '5HT1aR', '5HT1bR', '5HT2aR', '5HT4R', '5HT6R', '5HTT', 'GABAa', 'mGluR5', 'MOR', 'H3R', 'CB1R'])
        ax2.set_title('receptor/transporter disconnection')
        #ax2.set_yticks(np.arange(5,21,5))
        ax2.set_theta_offset(np.pi/2)
        ax2.set_theta_direction(-1)

        # Pre and postsynaptic ratios

        width3 = 2 * np.pi/12 - 2 * np.pi/12 * 0.1
        theta3 = np.arange(0, 2 * np.pi, 2 * np.pi/12)
        radii3a = []
        for i in range(len(recep_tract_perc)):
            if recep_tract_perc[i] == 0 and recep_perc[i] == 0:
                radii3a.append(max(trans_perc[i], trans_tract_perc[i])/0.1)
            else:
                radii3a.append(max(trans_perc[i], trans_tract_perc[i])/max(recep_perc[i], recep_tract_perc[i]))
        radii3b = []
        for i in range(len(recep_tract_perc)):
            if trans_tract_perc[i] == 0 and trans_perc[i] == 0:
                radii3b.append(max(recep_perc[i], recep_tract_perc[i])/0.1)
            else:
                radii3b.append(max(recep_perc[i], recep_tract_perc[i])/max(trans_perc[i], trans_tract_perc[i]))
        radii3b = [(radii3b[0]+radii3b[1])/2, (radii3b[2]+radii3b[3])/2, (radii3b[4]+radii3b[5]+radii3b[6]+radii3b[7]+radii3b[8])/5]
        radii3 = np.append(radii3a, radii3b)
        colors3 = []
        for i in range(len(radii3)):
            if radii3[i] > 1:
                colors3.append((0.42,0.74,0.71,1))
            else:
                colors3.append((0.96,0.95,0.70,1))

        radii3=np.log(radii3)
        radii3 = np.where(radii3==-np.inf, -1, radii3)
        ax3.bar(theta3, radii3, width=width3, bottom=0.0, color=colors3, edgecolor='dimgray')
        ax3.set_ylim([-1, 1])
        ax3.set_yticks([np.floor(radii3.min()), np.floor(radii3.min())/2, 0, np.ceil(radii3.max())/2, np.ceil(radii3.max())])
        ax3.set_rlabel_position(0)
        ax3.set_xticks(theta3)
        ax3.set_xticklabels(['A4B2 presynaptic', 'M1 presynaptic', 'D1 presynaptic', 'D2 presynaptic', '5HT1a presynaptic', '5HT1b presynaptic', '5HT2a presynaptic', '5HT4 presynaptic', '5HT6 presynaptic', 'VAChT postsynaptic', 'DAT postsynaptic', '5HTT postsynaptic'])
        ax3.set_title('Pre/pos synaptic ratios')
        ax3.set_theta_offset(np.pi/2)
        ax3.set_theta_direction(-1)


        output_les_dis = np.vstack([all_inj, all_perc, all_tract_inj, all_tract_perc])
        output_les_dis = pd.DataFrame(output_les_dis, columns=['A4B2', 'M1', 'VAChT', 'D1', 'D2', 'DAT', 'Nor', '5HT1a', '5HT1b', '5HT2a', '5HT4', '5HT6', '5HTT', 'GABAa', 'mGluR5', 'MU', 'H3', 'CB1'], index=['inj_'+str(lesion), 'perc_'+str(lesion), 'tract_inj_'+str(lesion), 'tract_perc'+str(lesion)])
        output_les_dis.to_csv('output_les_dis_'+str(lesion)+'.csv', sep=" ", header=True, index=True)

        pre_pos_ratio = np.array(radii3)
        pre_pos_ratio = pd.DataFrame(radii3, index=['A4B2 presynaptic', 'M1 presynaptic', 'D1 presynaptic', 'D2 presynaptic', '5HT1a presynaptic', '5HT1b presynaptic', '5HT2a presynaptic', '5HT4 presynaptic', '5HT6 presynaptic', 'VAChT postsynaptic', 'DAT postsynaptic', '5HTT postsynaptic'], columns=['pre_pos_ratio_'+str(lesion)])
        pre_pos_ratio = pre_pos_ratio.transpose()
        pre_pos_ratio.to_csv('pre_pos_ratio_'+str(lesion)+'.csv', sep=" ", header=True, index=True)

        plt.savefig('output_'+str(lesion)+'.png', bbox_inches='tight')
        plt.clf()


subprocess.run(cmd_lesion_int_nt, shell=True)
individual_profile()

