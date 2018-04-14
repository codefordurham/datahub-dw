\copy acsrent_bgs_2016(geoid00,gr,mgr,agr,agr_us,agr_mir,b_gr,gr_phi,mgr_phi,ah_gr_phi,hi_gr_phi,algr) FROM 'acs_rent_2016.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;
