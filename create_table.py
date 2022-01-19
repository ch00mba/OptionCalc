#!/usr/bin/python

import psycopg2
from sqlalchemy import create_engine



#pip3 install psycopg2-binary

#pip3 install sqlalchemy

# def create_tables():

commands = (
        """        
        CREATE TABLE ss_dataframe_final1 (
                index BIGSERIAL PRIMARY KEY,
                file_extension text,
                timestamp timestamp,
                local text,
                peer text,
                skmem text,
                cong_alg text,
                ts text,
                sack text,
                ecn text,
                ecnseen text,
                fastopen text,
                wscale text,
                rto text,
                rtt text,
                ato text,
                mss text,
                pmtu text,
                rcvmss text,
                advmss text,
                cwnd text,
                ssthresh text,
                bytes_acked text,
                bytes_received text,
                segs_out text,
                segs_in text,
                data_segs_out text,
                data_segs_in text,
                send text,
                lastsnd text,
                lastrcv text,
                lastack text,
                pacing_rate text,
                rcv_rtt text,
                delivery_rate text,
                busy text,
                unacked text,
                retrans text,
                rcv_space text,
                rcv_ssthresh text,
                notsent text,
                minrtt text,
                state text, 
                recv_q text,
                send_q text,
                users text
        );
        
        """)
   
try:
    
   # http://3.86.81.140
    statsEngine = create_engine('postgresql+psycopg2://postgres:example@172.17.0.1:5432/mydb')
    postgreSQLConnection = statsEngine.raw_connection()
    cur = postgreSQLConnection.cursor()
    # create table one by one
    #for command in commands:
    cur.execute(commands)
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    postgreSQLConnection.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if postgreSQLConnection is not None:
        postgreSQLConnection.close()



