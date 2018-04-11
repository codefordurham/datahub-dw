\copy decrent_bgs_2000(geoid00,gr,mgr,agr,agr_mir,agr_us,b_gr,gr_phi99,mgr_phi99,ah_gr_phi99,ui_gr_phi99,hi_gr_phi99,igr,crgr00) FROM '/home/jmcmanus/code_for_durham/affordable_housing/virtual/development/datahub-dw/durham_propbgs/dec_rent_2000.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;
