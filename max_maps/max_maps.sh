maps_max=(A4B2 M1 VAChT D1 D2 DAT NAT 5HT1a 5HT1b 5HT2a 5HT4 5HT6 5HTT)

for i in ${maps_max[@]}; do
	fslmerge -t ${i}_anat_AAL3plusnuclei_max_map.nii.gz ../PET_nifti_images/${i}_median_scale01_mas_AAL3plusnuclei.nii.gz ../functionnectome_maps/functionnectome_anat_${i}_from_AAL3plusnuclei.nii.gz
	fslmaths ${i}_anat_AAL3plusnuclei_max_map.nii.gz -Tmax ${i}_anat_AAL3plusnuclei_max_map.nii.gz
done
