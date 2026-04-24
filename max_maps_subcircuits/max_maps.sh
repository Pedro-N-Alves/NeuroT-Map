maps_max=(A4B2_basalforebrain M1_basalforebrain VAChT_basalforebrain A4B2_pontomesencephalic M1_pontomesencephalic VAChT_pontomesencephalic D1_mesocorticolimbic D2_mesocorticolimbic DAT_mesocorticolimbic D1_nigrostriatal D2_nigrostriatal DAT_nigrostriatal)

for i in ${maps_max[@]}; do
	fslmerge -t ${i}_anat_AAL3plusnuclei_max_map.nii.gz ../PET_nifti_images_subcircuits/${i}_median_scale01_mas_AAL3plusnuclei.nii.gz ../functionnectome_maps_subcircuits/functionnectome_anat_${i}_from_AAL3plusnuclei.nii.gz
	fslmaths ${i}_anat_AAL3plusnuclei_max_map.nii.gz -Tmax ${i}_anat_AAL3plusnuclei_max_map.nii.gz
done
