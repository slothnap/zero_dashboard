import DbConfig as dbConf
import multiprocessing as mp
import math
import dw_collect_data as getData


if __name__ == '__main__':
    # MDM DB 연결
    mdmDb = dbConf.DbConfig()
    mdmDb.opendb()

    sql = ("SELECT	db.extn_db_sno\n"
           "		, db.srvr_ip_adrs as host\n"
           "        , db.srvr_nm as db\n"
           "        , db.user_nm as user\n"
           "		, cast(aes_decrypt(unhex(db.user_pwd), 'jasonmdm' ) as char) as password\n"
           "		, tab.trgt_tab_nm\n"
           "		, replace(clct_sql, '[interval]', \n"
           "			case clct_cond_col_nm \n"
           "				when 'clct_perd_mins' then clct_perd_mins\n"
           "				when 'clct_pk_val'    then clct_pk_val\n"
           "				else ''\n"
           "		end) clct_sql\n"
           "		, befr_sql\n"
           "		, aftr_sql\n"
           "		, finl_clct_dtm, tab.tab_sno, tab.pk_col_nm, tab.eai_stus_nm\n"
           "FROM	extn_db db, dw_tab_list tab\n"
           "WHERE	db.extn_db_sno = tab.sorc_db_sno\n"
           "AND		tab.clct_yn = 'Y'\n"
           "AND		tab.eai_stus_nm not in ('진행중', '임시_진행중', '임시_보류')\n and tab_sno = 21 limit 1")

    # 수집 대상 DB정보 및 테이블, 쿼리 조회
    source = mdmDb.select(sql)

    # 병렬처리 진행 전처리
    num_cores = mp.cpu_count()  # cpu의 코어 수를 반환

    # 조회 대상 테이블을 cpu 코어수 만큼 분할
    unit_num = math.ceil(len(source) / num_cores)
    # multiArr = [source[i * unit_num:(i + 1) * unit_num] for i in range((len(source) + unit_num - 1) // unit_num)]

    procs = []
    for i in range(num_cores):
        if i == len(source):
            break
        # print(source[i * unit_num: (i + 1) * unit_num])
        proc = mp.Process(target=getData.getdata, args=(source[i * unit_num: (i + 1) * unit_num],))
        procs.append(proc)
        proc.start()

    # 조회 대상 항목들에 대하여 상태값 변경
    sql = """update dw_tab_list
               set eai_stus_nm = "전송 대기중"
             where clct_yn = 'Y'
               and eai_stus_nm = '변경완료'"""
    mdmDb.update(sql)
    mdmDb.closedb()
    for proc in procs:
        proc.join()

    print('전체 작업 완료')
