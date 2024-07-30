#binarized lesion
lesions=($@)

# Print a warning message if the list of lesions is empty
if [ -z "$lesions" ]; then
    echo "Please provide lesion names"
fi

# Calculate the proportion of receptor or transporter location density map voxels ('maps_loc') and receptor or transporter white matter projection map voxels (maps_tract) intersected by the lesion
for lesion in ${lesions[@]}; do
	maps_r=(GABAa mGluR5 MU H3 CB1)
	maps_t=(GABAa mGluR5 MU H3 CB1)

	labels=(maps)
	totals=(totals)
	injuries=(injuries)

	for i in ${maps_r[@]}; do
		labels+=( ${i}"_loc" )
		total_mean=$(fslstats ./PET_nifti_images_datad/${i}_median_scale01.nii.gz -M | awk '{print $1}')
		total_voxels=$(fslstats ./PET_nifti_images_datad/${i}_median_scale01.nii.gz -V | awk '{print $1}')
		total=$(echo $total_mean $total_voxels | awk '{printf "%4.3f\n",$1*$2}')
		totals+=(${total})
		fslmaths ./PET_nifti_images_datad/${i}_median_scale01.nii.gz -mas ./lesions/${lesion}.nii.gz ${i}_median_scale01_mas_lesion.nii.gz
		injury_mean=$(fslstats ${i}_median_scale01_mas_lesion.nii.gz -M | awk '{print $1}')
		injury_voxels=$(fslstats ${i}_median_scale01_mas_lesion.nii.gz -V | awk '{print $1}')
		injury=$(echo $injury_mean $injury_voxels | awk '{printf "%4.3f\n",$1*$2}')
		injuries+=($injury)
		rm ${i}_median_scale01_mas_lesion.nii.gz
	done

	for i in ${maps_t[@]}; do
		labels+=( ${i}"_con" )
		total_mean=$(fslstats ./functionnectome_maps_datad/functionnectome_datad_${i}.nii.gz -M | awk '{print $1}')
		total_voxels=$(fslstats ./functionnectome_maps_datad/functionnectome_datad_${i}.nii.gz -V | awk '{print $1}')
		total=$(echo $total_mean $total_voxels | awk '{printf "%4.3f\n",$1*$2}')
		totals+=(${total})
		fslmaths ./functionnectome_maps_datad/functionnectome_datad_${i}.nii.gz -mas ./lesions/${lesion}.nii.gz functionnectome_datad_${i}_mas_lesion.nii.gz
		injury_mean=$(fslstats functionnectome_datad_${i}_mas_lesion.nii.gz -M | awk '{print $1}')
		injury_voxels=$(fslstats functionnectome_datad_${i}_mas_lesion.nii.gz -V | awk '{print $1}')
		injury=$(echo $injury_mean $injury_voxels | awk '{printf "%4.3f\n",$1*$2}')
		injuries+=($injury)
		rm functionnectome_datad_${i}_mas_lesion.nii.gz
	done


	echo ${labels[@]} > output_datad_${lesion}.csv
	echo ${injuries[@]} >> output_datad_${lesion}.csv
	echo ${totals[@]} >> output_datad_${lesion}.csv
done