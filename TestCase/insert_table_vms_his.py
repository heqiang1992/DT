#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pymysql
import uuid

db = pymysql.connect("localhost", "root", "daemon", "hyhive")
cursor = db.cursor()

print("Connect db OK")
for i in range(1, 100):
    try:
        sql = '''insert into dh_nodes_history(nodeid, cpu, mem_total, mem_used, disk_read_rate, disk_write_rate,disk_write_req_rate,disk_read_req_rate,\
        net_in_packets_rate,net_out_packets_rate,disks,net_in_rate,net_out_rate,ovs_infos,\
        time) values('6','13.3','2147480000','10000','3687390',\
        '436039','24.0011','139.506','884.44','1005.96','{"/var/lib/ceph/osd/ceph-25": {"disk_usage": 3839557632.0, "disk_total": 2000397795328.0, "mount_point": "/var/lib/ceph/osd/ceph-25"}, "/var/lib/ceph/osd/ceph-24": {"disk_usage": 9687597056.0, "disk_total": 6001172414464.0, "mount_point": "/var/lib/ceph/osd/ceph-24"}, "/var/lib/ceph/osd/ceph-27": {"disk_usage": 3489202176.0, "disk_total": 2000397795328.0, "mount_point": "/var/lib/ceph/osd/ceph-27"}, "/var/lib/ceph/osd/ceph-26": {"disk_usage": 6583353344.0, "disk_total": 4000783007744.0, "mount_point": "/var/lib/ceph/osd/ceph-26"}, "/var/lib/ceph/osd/ceph-21": {"disk_usage": 4333961216.0, "disk_total": 2000397795328.0, "mount_point": "/var/lib/ceph/osd/ceph-21"}, "/var/lib/ceph/osd/ceph-20": {"disk_usage": 8775729152.0, "disk_total": 6001172414464.0, "mount_point": "/var/lib/ceph/osd/ceph-20"}, "/var/lib/ceph/osd/ceph-23": {"disk_usage": 6798442496.0, "disk_total": 4000783007744.0, "mount_point": "/var/lib/ceph/osd/ceph-23"}, "/var/lib/ceph/osd/ceph-22": {"disk_usage": 6749159424.0, "disk_total": 4000783007744.0, "mount_point": "/var/lib/ceph/osd/ceph-22"}, "/media": {"disk_total": 329230336, "mount_point": "/media", "disk_used": 329230336}, "/var/lib/ceph/osd/ceph-18": {"disk_usage": 6836256768.0, "disk_total": 4000783007744.0, "mount_point": "/var/lib/ceph/osd/ceph-18"}, "/var/lib/ceph/osd/ceph-19": {"disk_usage": 10297868288.0, "disk_total": 6001172414464.0, "mount_point": "/var/lib/ceph/osd/ceph-19"}, "/var/lib/ceph/osd/ceph-14": {"disk_usage": 6463684608.0, "disk_total": 4000783007744.0, "mount_point": "/var/lib/ceph/osd/ceph-14"}, "/var/lib/ceph/osd/ceph-15": {"disk_usage": 8823177216.0, "disk_total": 6001172414464.0, "mount_point": "/var/lib/ceph/osd/ceph-15"}, "/boot": {"disk_total": 491499520, "mount_point": "/boot", "disk_used": 172679168}, "/var/lib/ceph/osd/ceph-17": {"disk_usage": 10474684416.0, "disk_total": 6001172414464.0, "mount_point": "/var/lib/ceph/osd/ceph-17"}, "/": {"disk_total": 108172783616, "mount_point": "/", "disk_used": 8172732416}, "/var/lib/ceph/osd/ceph-16": {"disk_usage": 7411269632.0, "disk_total": 4000783007744.0, "mount_point": "/var/lib/ceph/osd/ceph-16"}}',\
        '577384','785541','{"br-int": {"patch-tun": {"rx-bytes": 0.0, "tx-pkts": 0.0, "rx-pkts": 0.0, "tx-bytes": 0.0}, "tx-pkts": 0.0, "rx-bytes": 0.0, "int-br-ex": {"rx-bytes": 0.0, "tx-pkts": 0.0, "rx-pkts": 0.0, "tx-bytes": 0.0}, "tx-bytes": 0.0, "rx-pkts": 0.0}, "br-ex": {"rx-bytes": 0.0, "tx-pkts": 0.0, "rx-pkts": 0.0, "tx-bytes": 0.0, "phy-br-ex": {"rx-bytes": 0.0, "tx-pkts": 0.0, "rx-pkts": 0.0, "tx-bytes": 0.0}}}','2019-05-15 17:00:32')
        '''
        cursor.execute(sql)
    except:
        continue
db.commit()
cursor.close()
db.close()
