from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://script:script2015@opsdb.ena.net/ops')

conn = engine.connect()
query = conn.execute("SELECT shortname, ipstr, sitecid, sitename, customercid FROM devicedetail WHERE customercid = %s", (2463,))

output = {}
row = query.fetchone()

while row is not None:
    if len(row) == 5:
        output[row[0]] = {
            'shortame':     row[0],
            'ipstr':        row[1],
            'sitecid':      row[2],
            'sitename':     row[3],
            'customercid':  row[4]
        }
    row = query.fetchone()

print(output)