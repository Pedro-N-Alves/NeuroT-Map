#binarized lesion
lesions=($@)

if [ -z "$lesions" ]; then
    echo "Please provide lesion names"
fi

for lesion in ${lesions[@]}; do
	maps_r=(A4B2 M1 VAChT D1 D2 DAT NAT 5HT1a 5HT1b 5HT2a 5HT4 5HT6 5HTT GABAa mGluR5 MU H3 CB1)
	maps_t=(A4B2 M1 VAChT D1 D2 DAT NAT 5HT1a 5HT1b 5HT2a 5HT4 5HT6 5HTT GABAa mGluR5 MU H3 CB1)

	labels=(maps)
	totals=(totals_mm3)
	injuries=(injuries_mm3)

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


	echo ${labels[@]} > output_${lesion}.csv
	echo ${injuries[@]} >> output_${lesion}.csv
	echo ${totals[@]} >> output_${lesion}.csv
done