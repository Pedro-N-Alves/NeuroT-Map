# List of binarized lesions
lesions=($@)

# Print a warning message if the list of lesions is empty
if [ -z "$lesions" ]; then
    echo "Please provide lesion names"
fi

# Calculate the proportion of receptor or transporter location density map voxels ('maps_loc') and receptor or transporter white matter projection map voxels (maps_tract) intersected by the lesion
for lesion in ${lesions[@]}; do
	maps_loc=(A4B2_basalforebrain M1_basalforebrain VAChT_basalforebrain A4B2_pontomesencephalic M1_pontomesencephalic VAChT_pontomesencephalic D1_mesocorticolimbic D2_mesocorticolimbic DAT_mesocorticolimbic D1_nigrostriatal D2_nigrostriatal DAT_nigrostriatal)
	maps_tract=(A4B2_basalforebrain M1_basalforebrain VAChT_basalforebrain A4B2_pontomesencephalic M1_pontomesencephalic VAChT_pontomesencephalic D1_mesocorticolimbic D2_mesocorticolimbic DAT_mesocorticolimbic D1_nigrostriatal D2_nigrostriatal DAT_nigrostriatal)
	maps_max=(A4B2_basalforebrain M1_basalforebrain VAChT_basalforebrain A4B2_pontomesencephalic M1_pontomesencephalic VAChT_pontomesencephalic D1_mesocorticolimbic D2_mesocorticolimbic DAT_mesocorticolimbic D1_nigrostriatal D2_nigrostriatal DAT_nigrostriatal)

	labels=(maps)
	totals=(totals)
	injuries=(injuries)

	for i in ${maps_loc[@]}; do
		labels+=( ${i}"_loc" )
		total_mean=$(fslstats ./PET_nifti_images_subcircuits/${i}_median_scale01_mas_AAL3plusnuclei.nii.gz -M | awk '{print $1}')
		total_voxels=$(fslstats ./PET_nifti_images_subcircuits/${i}_median_scale01_mas_AAL3plusnuclei.nii.gz -V | awk '{print $1}')
		total=$(echo $total_mean $total_voxels | awk '{printf "%4.3f\n",$1*$2}')
		totals+=(${total})
		fslmaths ./PET_nifti_images_subcircuits/${i}_median_scale01_mas_AAL3plusnuclei.nii.gz -mas ./lesions/${lesion}.nii.gz ${i}_median_scale01_mas_AAL3plusnuclei_mas_lesion.nii.gz
		injury_mean=$(fslstats ${i}_median_scale01_mas_AAL3plusnuclei_mas_lesion.nii.gz -M | awk '{print $1}')
		injury_voxels=$(fslstats ${i}_median_scale01_mas_AAL3plusnuclei_mas_lesion.nii.gz -V | awk '{print $1}')
		injury=$(echo $injury_mean $injury_voxels | awk '{printf "%4.3f\n",$1*$2}')
		injuries+=($injury)
		rm ${i}_median_scale01_mas_AAL3plusnuclei_mas_lesion.nii.gz
	done

	for i in ${maps_tract[@]}; do
		labels+=( ${i}"_con" )
		total_mean=$(fslstats ./functionnectome_maps_subcircuits/functionnectome_anat_${i}_from_AAL3plusnuclei.nii.gz -M | awk '{print $1}')
		total_voxels=$(fslstats ./functionnectome_maps_subcircuits/functionnectome_anat_${i}_from_AAL3plusnuclei.nii.gz -V | awk '{print $1}')
		total=$(echo $total_mean $total_voxels | awk '{printf "%4.3f\n",$1*$2}')
		totals+=(${total})
		fslmaths ./functionnectome_maps_subcircuits/functionnectome_anat_${i}_from_AAL3plusnuclei.nii.gz -mas ./lesions/${lesion}.nii.gz functionnectome_anat_${i}_from_AAL3plusnuclei_mas_lesion.nii.gz
		injury_mean=$(fslstats functionnectome_anat_${i}_from_AAL3plusnuclei_mas_lesion.nii.gz -M | awk '{print $1}')
		injury_voxels=$(fslstats functionnectome_anat_${i}_from_AAL3plusnuclei_mas_lesion.nii.gz -V | awk '{print $1}')
		injury=$(echo $injury_mean $injury_voxels | awk '{printf "%4.3f\n",$1*$2}')
		injuries+=($injury)
		rm functionnectome_anat_${i}_from_AAL3plusnuclei_mas_lesion.nii.gz
	done
	
	for i in ${maps_max[@]}; do
		labels+=( ${i}"_max" )
		total_mean=$(fslstats ./max_maps_subcircuits/${i}_anat_AAL3plusnuclei_max_map.nii.gz -M | awk '{print $1}')
		total_voxels=$(fslstats ./max_maps_subcircuits/${i}_anat_AAL3plusnuclei_max_map.nii.gz -V | awk '{print $1}')
		total=$(echo $total_mean $total_voxels | awk '{printf "%4.3f\n",$1*$2}')
		totals+=(${total})
		fslmaths ./max_maps_subcircuits/${i}_anat_AAL3plusnuclei_max_map.nii.gz -mas ./lesions/${lesion}.nii.gz ${i}_anat_AAL3plusnuclei_max_map_mas_lesion.nii.gz
		injury_mean=$(fslstats ${i}_anat_AAL3plusnuclei_max_map_mas_lesion.nii.gz -M | awk '{print $1}')
		injury_voxels=$(fslstats ${i}_anat_AAL3plusnuclei_max_map_mas_lesion.nii.gz -V | awk '{print $1}')
		injury=$(echo $injury_mean $injury_voxels | awk '{printf "%4.3f\n",$1*$2}')
		injuries+=($injury)
		rm ${i}_anat_AAL3plusnuclei_max_map_mas_lesion.nii.gz
	done


	echo ${labels[@]} > output_subcircuits_${lesion}.csv
	echo ${injuries[@]} >> output_subcircuits_${lesion}.csv
	echo ${totals[@]} >> output_subcircuits_${lesion}.csv
done