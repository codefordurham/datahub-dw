\copy decincome_bgs_2000(geoid00,mgr_phi99,mmoc_phi99,mhi99,mhi99_ah,mfh99,mnhi99,mhi99_w,mhi99_b,mhi99_n,mhi99_a,mhi99_h,mhi99_o,mhi_99_t,mhi99_wnh,mfi99_w,mfi99_b,mfi99_n,mfi99_a,mfi99_h,mfi99_o,mfi99_t,mfi99_wnh,mnfh99) FROM '/home/jmcmanus/code_for_durham/affordable_housing/virtual/development/datahub-dw/durham_propbgs/dec_income_2000.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;
