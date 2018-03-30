\copy compassrace_bgs_2016(id,pop_13,pop_14,ptwhnl_13,ptwhnl_14,ptblknl_13,ptblknl_14,ptasnl_13,ptasnl_14,ptothnl_13,ptothnl_14,ptlat_13,ptlat_14) FROM '/home/jmcmanus/code_for_durham/affordable_housing/virtual/development/datahub-dw/durham_propbgs/compass_race_2016.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;
