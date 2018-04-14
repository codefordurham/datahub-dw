\copy datahub_be_app_decrace_bgs_00(id,pop_00,ptwhnl_00,ptblknl_00,ptnanl_00,ptasnl_00,ptpanl_00,ptothnl_00,pt2mnl_00,ptlat_00) FROM 'dec_race_2000.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;
