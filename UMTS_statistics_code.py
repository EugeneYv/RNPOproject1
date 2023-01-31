import pandas as pd
import winsound
''' количество активных сот 538!!! - используется для расчёта скорости HSDPA HSUPA,  для CityK 43
вывод посуточной статистики для UMTS. импортный файл - в МАЕ вывести в формате xlsx два файла, потом в экселе сложить слева на право и переделать в csv
'''
active_cell_number = 538  # количество активных сот !!!!


#sts1 = pd.read_csv("C:/test/3G_counters1(2023-01-09.csv", sep=";", header=7, na_values='NIL') # вариант импорта 1
#sts2 = pd.read_csv("C:/test/3G_counters2(2023-01-09_.csv", sep=";", header=7, na_values='NIL') # вариант импорта 1
#sts_df = pd.merge(sts1, sts2, how="left", on="Start Time") # вариант импорта 1
#sts_df = pd.read_csv("C:/test/sts3G/3G_counters1_9_15.csv", sep=";", header=7, na_values='NIL') #  вариант импорта 2
sts_df = pd.read_csv("C:/work/CityH_audit/sts/3G/3G_09-30.01.csv", sep=";", header=7, na_values='NIL') #  вариант импорта для CityK
sts_df['date'] = sts_df['Start Time'].str.split(' ').str[0]
sts_df['hour'] = sts_df['Start Time'].str.split(' ').str[1]
sts_df.to_excel("C:/test/sts3G/sts_df.xls", engine='openpyxl', sheet_name='Book2')
list_1 = ['RRC.AttConnEstab.EmgCall (None)','RRC.AttConnEstab.OrgConvCall (None)','RRC.AttConnEstab.TmConvCall (None)',\
          'RRC.SuccConnEstab.EmgCall (None)','RRC.SuccConnEstab.OrgConvCall (None)','RRC.SuccConnEstab.TmConvCall (None)',\
          '{Upgrade}Soft Handover Success Ratio (%)','VS.AttCellUpdt.EmgCall.PCH (None)','VS.AttCellUpdt.OrgConvCall.PCH (None)',\
          'VS.AttCellUpdt.TmConvCall.PCH (None)','VS.DCCC.D2P.Succ (None)','VS.DCCC.Succ.D2U (None)','VS.DCCC.Succ.F2P (None)',\
          'VS.DCCC.Succ.F2U (None)','VS.HSDPA.H2D.Succ (None)','VS.HSDPA.H2F.Succ (None)','VS.HSDPA.HHO.H2D.SuccOutInterFreq (None)',\
          'VS.HSDPA.HHO.H2D.SuccOutIntraFreq (None)','VS.HSDPA.MeanChThroughput (kbit/s)','VS.HSDPA.MeanChThroughput.TotalBytes (byte)',\
          'VS.HSDPA.RAB.AbnormRel (None)','VS.HSDPA.RAB.NormRel (None)','VS.HSUPA.MeanChThroughput (kbit/s)','VS.HSUPA.MeanChThroughput.TotalBytes (byte)',\
          'VS.PS.Bkg.DL.8.Traffic (bit)','VS.PS.Bkg.DL.16.Traffic (bit)','VS.PS.Bkg.DL.32.Traffic (bit)','VS.PS.Bkg.DL.64.Traffic (bit)',\
          'VS.PS.Bkg.DL.128.Traffic (bit)','VS.PS.Bkg.DL.144.Traffic (bit)','VS.PS.Bkg.DL.256.Traffic (bit)','VS.PS.Bkg.DL.384.Traffic (bit)',\
          'VS.PS.Bkg.UL.8.Traffic (bit)','VS.PS.Bkg.UL.16.Traffic (bit)','VS.PS.Bkg.UL.32.Traffic (bit)','VS.PS.Bkg.UL.64.Traffic (bit)',\
          'VS.PS.Bkg.UL.128.Traffic (bit)','VS.PS.Bkg.UL.144.Traffic (bit)','VS.PS.Bkg.UL.256.Traffic (bit)','VS.PS.Bkg.UL.384.Traffic (bit)',\
          'VS.PS.Int.DL.8.Traffic (bit)','VS.PS.Int.DL.16.Traffic (bit)','VS.PS.Int.DL.32.Traffic (bit)','VS.PS.Int.DL.64.Traffic (bit)',\
          'VS.PS.Int.DL.128.Traffic (bit)','VS.PS.Int.DL.144.Traffic (bit)','VS.PS.Int.DL.256.Traffic (bit)','VS.PS.Int.DL.384.Traffic (bit)',\
          'VS.PS.Int.UL.8.Traffic (bit)','VS.PS.Int.UL.16.Traffic (bit)','VS.PS.Int.UL.32.Traffic (bit)','VS.PS.Int.UL.64.Traffic (bit)',\
          'VS.PS.Int.UL.128.Traffic (bit)','VS.PS.Int.UL.144.Traffic (bit)','VS.PS.Int.UL.256.Traffic (bit)','VS.PS.Int.UL.384.Traffic (bit)',\
          'VS.PS.Str.DL.32.Traffic (bit)','VS.PS.Str.DL.64.Traffic (bit)','VS.PS.Str.DL.128.Traffic (bit)','VS.PS.Str.DL.144.Traffic (bit)',\
          'VS.PS.Str.UL.16.Traffic (bit)','VS.PS.Str.UL.32.Traffic (bit)','VS.PS.Str.UL.64.Traffic (bit)','VS.RAB.AbnormRel.CS (None)',\
          'VS.RAB.AbnormRel.PS (None)','VS.RAB.AbnormRel.PS.D2P (None)','VS.RAB.AbnormRel.PS.F2P (None)','VS.RAB.AbnormRel.PS.PCH (None)',\
          'VS.RAB.NormRel.CS (None)','VS.RAB.NormRel.PS (None)','VS.RAB.NormRel.PS.PCH (None)','VS.SuccCellUpdt.EmgCall.PCH (None)',\
          'VS.SuccCellUpdt.OrgConvCall.PCH (None)','VS.SuccCellUpdt.TmConvCall.PCH (None)','CS Voice Traffic Volume (Erl)',\
          'VS.RAB.AttEstabPS.Bkg (None)','VS.RAB.AttEstabPS.Int (None)','VS.RAB.AttEstabPS.Str (None)','VS.RAB.FailEstabPS.Code.Cong (None)',\
          'VS.RAB.FailEstabPS.DLCE.Cong (None)','VS.RAB.FailEstabPS.DLIUBBand.Cong (None)','VS.RAB.FailEstabPS.DLPower.Cong (None)',\
          'VS.RAB.FailEstabPS.HSDPAUser.Cong (None)','VS.RAB.FailEstabPS.HSUPAUser.Cong (None)','VS.RAB.FailEstabPS.ULCE.Cong (None)',\
          'VS.RAB.FailEstabPS.ULIUBBand.Cong (None)','VS.RAB.FailEstabPS.ULPower.Cong (None)','VS.SHO.AttRLAdd (None)','VS.SHO.AttRLDel (None)',\
          'VS.SHO.SuccRLAdd (None)','VS.SHO.SuccRLDel (None)','VS.HHO.AttInterFreqOut (None)','VS.HHO.SuccInterFreqOut (None)','VS.IRATHOCS.Cancel.ReEstab (None)',\
          'VS.IRATHOPS.Cancel.ReEstab (None)','IRATHO.SuccOutCS (None)','IRATHO.AttOutCS (None)','IRATHO.SuccOutPSUTRAN (None)','IRATHO.AttOutPSUTRAN (None)',\
          'VS.RAB.AttEstab.AMR (None)','VS.RAB.SuccEstabCS.AMR (None)','VS.RAB.AttEstabPS.Conv (None)','VS.RAB.SuccEstabPS.Conv (None)','VS.RAB.SuccEstabPS.Bkg (None)',\
          'VS.RAB.SuccEstabPS.Int (None)','VS.RAB.SuccEstabPS.Str (None)','RRC.SuccConnEstab.sum (None)','VS.RRC.AttConnEstab.Sum (None)','RRC.AttConnRelCCCH.Cong (None)',\
          'RRC.AttConnRelCCCH.Preempt (None)','RRC.AttConnRelCCCH.ReEstRej (None)','RRC.AttConnRelCCCH.Unspec (None)','RRC.AttConnRelDCCH.Cong (None)',\
          'RRC.AttConnRelDCCH.Preempt (None)','RRC.AttConnRelDCCH.ReEstRej (None)','RRC.AttConnRelDCCH.Unspec (None)','VS.RRC.ConnRel.CellUpd (None)',\
          'RRC.AttConnRelDCCH.DSCR (None)','RRC.AttConnRelDCCH.UsrInact (None)','RRC.AttConnRelCCCH.DSCR (None)','RRC.AttConnRelDCCH.Norm (None)',\
          'RRC.AttConnRelCCCH.Norm (None)','RRC.AttConnRelCCCH.UsrInact (None)']

# обработка daily:
daily_df = sts_df.groupby(['date'])[list_1]. sum().reset_index()
list_2 = ['CS traffic 3G, Erl','PS traffic 3G UL+DL, GB','CS RAB Drop Rate (%)','PS Blocking Rate (%)','PS RAB Drop Rate (%)','PS HS- Drop Rate (%)',\
          'HSDPA Throughput, kbps','HSUPA Throughput, kbps','Soft Handover Success rate, %','Hard Handover Success rate, %','CS W2G Inter-RAT Handover Out SR',\
          'RRC Assignment SucessRate (CS BH), %','RRC Assignment SucessRate (PS BH), %','RRC Drop Rate (CS BH), %','RRC Drop Rate (PS BH), %',\
          'RAB Assignment Success Rate (CS), %','RAB Assignment Success Rate (PS), %','CCSR CS,%','CCSR PS,%'] # пока не нужен
daily_df['CS traffic 3G, Erl'] = daily_df['CS Voice Traffic Volume (Erl)']
daily_df['PS traffic 3G UL+DL, GB'] = (daily_df['VS.HSUPA.MeanChThroughput.TotalBytes (byte)'] + daily_df['VS.PS.Bkg.DL.8.Traffic (bit)'] + daily_df['VS.PS.Bkg.DL.16.Traffic (bit)'] + \
                                      daily_df['VS.PS.Bkg.DL.32.Traffic (bit)'] + daily_df['VS.PS.Bkg.DL.64.Traffic (bit)'] + daily_df['VS.PS.Bkg.DL.128.Traffic (bit)'] + \
                                      daily_df['VS.PS.Bkg.DL.144.Traffic (bit)'] + daily_df['VS.PS.Bkg.DL.256.Traffic (bit)'] + daily_df['VS.PS.Bkg.DL.384.Traffic (bit)'] + \
                                      daily_df['VS.PS.Bkg.UL.8.Traffic (bit)'] + daily_df['VS.PS.Bkg.UL.16.Traffic (bit)'] + daily_df['VS.PS.Bkg.UL.32.Traffic (bit)'] + \
                                      daily_df['VS.PS.Bkg.UL.64.Traffic (bit)'] + daily_df['VS.PS.Bkg.UL.128.Traffic (bit)'] + daily_df['VS.PS.Bkg.UL.144.Traffic (bit)'] + \
                                      daily_df['VS.PS.Bkg.UL.256.Traffic (bit)'] + daily_df['VS.PS.Bkg.UL.384.Traffic (bit)'] + daily_df['VS.PS.Int.DL.8.Traffic (bit)'] + \
                                      daily_df['VS.PS.Int.DL.16.Traffic (bit)'] + daily_df['VS.PS.Int.DL.32.Traffic (bit)'] + daily_df['VS.PS.Int.DL.64.Traffic (bit)'] + \
                                      daily_df['VS.PS.Int.DL.128.Traffic (bit)'] + daily_df['VS.PS.Int.DL.144.Traffic (bit)'] + daily_df['VS.PS.Int.DL.256.Traffic (bit)'] + \
                                      daily_df['VS.PS.Int.DL.384.Traffic (bit)'] + daily_df['VS.PS.Int.UL.8.Traffic (bit)'] + daily_df['VS.PS.Int.UL.16.Traffic (bit)'] + \
                                      daily_df['VS.PS.Int.UL.32.Traffic (bit)'] + daily_df['VS.PS.Int.UL.64.Traffic (bit)'] + daily_df['VS.PS.Int.UL.128.Traffic (bit)'] + \
                                      daily_df['VS.PS.Int.UL.144.Traffic (bit)'] + daily_df['VS.PS.Int.UL.256.Traffic (bit)'] + daily_df['VS.PS.Int.UL.384.Traffic (bit)'] + \
                                      daily_df['VS.PS.Str.DL.32.Traffic (bit)'] + daily_df['VS.PS.Str.DL.64.Traffic (bit)'] + daily_df['VS.PS.Str.DL.128.Traffic (bit)'] + \
                                      daily_df['VS.PS.Str.DL.144.Traffic (bit)'] + daily_df['VS.PS.Str.UL.16.Traffic (bit)'] + daily_df['VS.PS.Str.UL.32.Traffic (bit)'] + \
                                      daily_df['VS.PS.Str.UL.64.Traffic (bit)'] + daily_df['VS.HSDPA.MeanChThroughput.TotalBytes (byte)']) / 1000000
daily_df['CS RAB Drop Rate (%)'] = daily_df['VS.RAB.AbnormRel.CS (None)'] / (daily_df['VS.RAB.AbnormRel.CS (None)'] + daily_df['VS.RAB.NormRel.CS (None)']) * 100
daily_df['PS Blocking Rate (%)'] = (daily_df['VS.RAB.FailEstabPS.DLIUBBand.Cong (None)'] + daily_df['VS.RAB.FailEstabPS.ULIUBBand.Cong (None)'] + daily_df['VS.RAB.FailEstabPS.ULCE.Cong (None)'] + \
                                    daily_df['VS.RAB.FailEstabPS.DLCE.Cong (None)'] + daily_df['VS.RAB.FailEstabPS.Code.Cong (None)'] + daily_df['VS.RAB.FailEstabPS.ULPower.Cong (None)'] + \
                                    daily_df['VS.RAB.FailEstabPS.DLPower.Cong (None)'] + daily_df['VS.RAB.FailEstabPS.HSDPAUser.Cong (None)'] + daily_df['VS.RAB.FailEstabPS.HSUPAUser.Cong (None)']) / \
                                    (daily_df['VS.RAB.AttEstabPS.Str (None)'] + daily_df['VS.RAB.AttEstabPS.Int (None)'] + daily_df['VS.RAB.AttEstabPS.Bkg (None)']) *100

daily_df['PS RAB Drop Rate (%)'] = (daily_df['VS.RAB.AbnormRel.PS (None)'] + daily_df['VS.RAB.AbnormRel.PS.PCH (None)'] + daily_df['VS.RAB.AbnormRel.PS.D2P (None)'] + \
                                    daily_df['VS.RAB.AbnormRel.PS.F2P (None)']) / \
                                   (daily_df['VS.RAB.AbnormRel.PS (None)'] + daily_df['VS.RAB.NormRel.PS (None)'] + daily_df['VS.RAB.AbnormRel.PS.PCH (None)'] + \
                                    daily_df['VS.RAB.NormRel.PS.PCH (None)']) * 100
daily_df['PS HS- Drop Rate (%)'] =  daily_df['VS.HSDPA.RAB.AbnormRel (None)'] / (daily_df['VS.HSDPA.RAB.AbnormRel (None)'] + daily_df['VS.HSDPA.RAB.NormRel (None)'] + daily_df['VS.HSDPA.H2D.Succ (None)'] + daily_df['VS.HSDPA.H2F.Succ (None)'] +daily_df['VS.HSDPA.HHO.H2D.SuccOutIntraFreq (None)'] + daily_df['VS.HSDPA.HHO.H2D.SuccOutInterFreq (None)']) * 100
daily_df['HSDPA Throughput, kbps'] = daily_df['VS.HSDPA.MeanChThroughput (kbit/s)'] / active_cell_number / 24 # количество сот
daily_df['HSUPA Throughput, kbps'] = daily_df['VS.HSUPA.MeanChThroughput (kbit/s)'] / active_cell_number / 24# количество сот
daily_df['Soft Handover Success rate, %'] = (daily_df['VS.SHO.SuccRLAdd (None)'] + daily_df['VS.SHO.SuccRLDel (None)']) / (daily_df['VS.SHO.AttRLAdd (None)'] + daily_df['VS.SHO.AttRLDel (None)']) * 100
daily_df['Hard Handover Success rate, %'] = daily_df['VS.HHO.SuccInterFreqOut (None)'] / daily_df['VS.HHO.AttInterFreqOut (None)'] * 100
daily_df['CS W2G Inter-RAT Handover Out SR'] = daily_df['IRATHO.SuccOutCS (None)'] / (daily_df['IRATHO.AttOutCS (None)'] - daily_df['VS.IRATHOCS.Cancel.ReEstab (None)']) * 100
daily_df['RRC Assignment SucessRate (CS BH), %'] = daily_df['RRC.SuccConnEstab.sum (None)'] / daily_df['VS.RRC.AttConnEstab.Sum (None)'] * 100
daily_df['RRC Assignment SucessRate (PS BH), %'] = daily_df['RRC.SuccConnEstab.sum (None)'] / daily_df['VS.RRC.AttConnEstab.Sum (None)'] * 100
daily_df['RRC Drop Rate (CS BH), %'] = (daily_df['RRC.AttConnRelCCCH.Cong (None)'] + daily_df['RRC.AttConnRelCCCH.Preempt (None)'] + daily_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                             daily_df['RRC.AttConnRelCCCH.Unspec (None)'] + daily_df['RRC.AttConnRelDCCH.Cong (None)'] + daily_df['RRC.AttConnRelDCCH.Preempt (None)'] + \
                                             daily_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + daily_df['RRC.AttConnRelDCCH.Unspec (None)'] + daily_df['VS.RRC.ConnRel.CellUpd (None)']) \
                                        / (daily_df['RRC.AttConnRelDCCH.Cong (None)'] + daily_df['RRC.AttConnRelDCCH.Preempt (None)'] + daily_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + \
                                           daily_df['RRC.AttConnRelDCCH.DSCR (None)'] + daily_df['RRC.AttConnRelDCCH.UsrInact (None)'] + daily_df['RRC.AttConnRelDCCH.Unspec (None)'] + \
                                           daily_df['RRC.AttConnRelCCCH.Cong (None)'] + daily_df['RRC.AttConnRelCCCH.Preempt (None)'] + daily_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                           daily_df['RRC.AttConnRelCCCH.DSCR (None)'] + daily_df['RRC.AttConnRelDCCH.Norm (None)'] + daily_df['RRC.AttConnRelCCCH.Norm (None)'] + \
                                           daily_df['RRC.AttConnRelCCCH.UsrInact (None)'] + daily_df['RRC.AttConnRelCCCH.Unspec (None)'] + daily_df['VS.RRC.ConnRel.CellUpd (None)'] + \
                                           daily_df['VS.DCCC.Succ.F2P (None)'] + daily_df['IRATHO.SuccOutCS (None)'] + daily_df['IRATHO.SuccOutPSUTRAN (None)'] + daily_df['VS.DCCC.Succ.F2U (None)'] + \
                                           daily_df['VS.DCCC.Succ.D2U (None)']) * 100
daily_df['RRC Drop Rate (PS BH), %'] = (daily_df['RRC.AttConnRelCCCH.Cong (None)'] + daily_df['RRC.AttConnRelCCCH.Preempt (None)'] + daily_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                             daily_df['RRC.AttConnRelCCCH.Unspec (None)'] + daily_df['RRC.AttConnRelDCCH.Cong (None)'] + daily_df['RRC.AttConnRelDCCH.Preempt (None)'] + \
                                             daily_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + daily_df['RRC.AttConnRelDCCH.Unspec (None)'] + daily_df['VS.RRC.ConnRel.CellUpd (None)']) \
                                        / (daily_df['RRC.AttConnRelDCCH.Cong (None)'] + daily_df['RRC.AttConnRelDCCH.Preempt (None)'] + daily_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + \
                                           daily_df['RRC.AttConnRelDCCH.DSCR (None)'] + daily_df['RRC.AttConnRelDCCH.UsrInact (None)'] + daily_df['RRC.AttConnRelDCCH.Unspec (None)'] + \
                                           daily_df['RRC.AttConnRelCCCH.Cong (None)'] + daily_df['RRC.AttConnRelCCCH.Preempt (None)'] + daily_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                           daily_df['RRC.AttConnRelCCCH.DSCR (None)'] + daily_df['RRC.AttConnRelDCCH.Norm (None)'] + daily_df['RRC.AttConnRelCCCH.Norm (None)'] + \
                                           daily_df['RRC.AttConnRelCCCH.UsrInact (None)'] + daily_df['RRC.AttConnRelCCCH.Unspec (None)'] + daily_df['VS.RRC.ConnRel.CellUpd (None)'] + \
                                           daily_df['VS.DCCC.Succ.F2P (None)'] + daily_df['IRATHO.SuccOutCS (None)'] + daily_df['IRATHO.SuccOutPSUTRAN (None)'] + daily_df['VS.DCCC.Succ.F2U (None)'] + \
                                           daily_df['VS.DCCC.Succ.D2U (None)']) * 100
daily_df['RAB Assignment Success Rate (CS), %'] = daily_df['VS.RAB.SuccEstabCS.AMR (None)'] / daily_df['VS.RAB.AttEstab.AMR (None)'] * 100
daily_df['RAB Assignment Success Rate (PS), %'] = (daily_df['VS.RAB.SuccEstabPS.Conv (None)'] + daily_df['VS.RAB.SuccEstabPS.Bkg (None)'] + daily_df['VS.RAB.SuccEstabPS.Int (None)'] + \
                                                   daily_df['VS.RAB.SuccEstabPS.Str (None)']) / \
                                                  (daily_df['VS.RAB.AttEstabPS.Bkg (None)'] + daily_df['VS.RAB.AttEstabPS.Int (None)'] + daily_df['VS.RAB.AttEstabPS.Str (None)'] + \
                                                   daily_df['VS.RAB.AttEstabPS.Conv (None)']) * 100
daily_df['CCSR CS,%'] = daily_df['RRC Assignment SucessRate (CS BH), %'] * (100 - daily_df['RRC Drop Rate (CS BH), %']) * daily_df['RAB Assignment Success Rate (CS), %'] * (100 - daily_df['CS RAB Drop Rate (%)'])/ 1000000
daily_df['CCSR PS,%'] = daily_df['RRC Assignment SucessRate (PS BH), %'] * (100 - daily_df['RRC Drop Rate (PS BH), %']) * daily_df['RAB Assignment Success Rate (PS), %'] * (100 - daily_df['PS RAB Drop Rate (%)'])/ 1000000
daily_df = daily_df.drop(list_1, axis=1)
daily_df = daily_df.transpose()

# обработка hourly
hourly_df = sts_df.groupby(['date', 'hour'])[list_1].sum().reset_index()
max_index_PS = hourly_df.groupby('date')['VS.HSDPA.MeanChThroughput.TotalBytes (byte)'].idxmax()
hourlyPS_df = hourly_df.loc[max_index_PS]
max_index_CS = hourly_df.groupby('date')['CS Voice Traffic Volume (Erl)'].idxmax()
hourlyCS_df = hourly_df.loc[max_index_CS]

hourlyCS_df['CS traffic 3G, Erl'] = hourlyCS_df['CS Voice Traffic Volume (Erl)']
hourlyPS_df['PS traffic 3G UL+DL, GB'] = (hourlyPS_df['VS.HSUPA.MeanChThroughput.TotalBytes (byte)'] + hourlyPS_df['VS.PS.Bkg.DL.8.Traffic (bit)'] + hourlyPS_df['VS.PS.Bkg.DL.16.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Bkg.DL.32.Traffic (bit)'] + hourlyPS_df['VS.PS.Bkg.DL.64.Traffic (bit)'] + hourlyPS_df['VS.PS.Bkg.DL.128.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Bkg.DL.144.Traffic (bit)'] + hourlyPS_df['VS.PS.Bkg.DL.256.Traffic (bit)'] + hourlyPS_df['VS.PS.Bkg.DL.384.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Bkg.UL.8.Traffic (bit)'] + hourlyPS_df['VS.PS.Bkg.UL.16.Traffic (bit)'] + hourlyPS_df['VS.PS.Bkg.UL.32.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Bkg.UL.64.Traffic (bit)'] + hourlyPS_df['VS.PS.Bkg.UL.128.Traffic (bit)'] + hourlyPS_df['VS.PS.Bkg.UL.144.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Bkg.UL.256.Traffic (bit)'] + hourlyPS_df['VS.PS.Bkg.UL.384.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.DL.8.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Int.DL.16.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.DL.32.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.DL.64.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Int.DL.128.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.DL.144.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.DL.256.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Int.DL.384.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.UL.8.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.UL.16.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Int.UL.32.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.UL.64.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.UL.128.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Int.UL.144.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.UL.256.Traffic (bit)'] + hourlyPS_df['VS.PS.Int.UL.384.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Str.DL.32.Traffic (bit)'] + hourlyPS_df['VS.PS.Str.DL.64.Traffic (bit)'] + hourlyPS_df['VS.PS.Str.DL.128.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Str.DL.144.Traffic (bit)'] + hourlyPS_df['VS.PS.Str.UL.16.Traffic (bit)'] + hourlyPS_df['VS.PS.Str.UL.32.Traffic (bit)'] + \
                                      hourlyPS_df['VS.PS.Str.UL.64.Traffic (bit)'] + hourlyPS_df['VS.HSDPA.MeanChThroughput.TotalBytes (byte)']) / 1000000
hourlyCS_df['CS RAB Drop Rate (%)'] = hourlyCS_df['VS.RAB.AbnormRel.CS (None)'] / (hourlyCS_df['VS.RAB.AbnormRel.CS (None)'] + hourlyCS_df['VS.RAB.NormRel.CS (None)']) * 100
hourlyPS_df['PS Blocking Rate (%)'] = (hourlyPS_df['VS.RAB.FailEstabPS.DLIUBBand.Cong (None)'] + hourlyPS_df['VS.RAB.FailEstabPS.ULIUBBand.Cong (None)'] + hourlyPS_df['VS.RAB.FailEstabPS.ULCE.Cong (None)'] + \
                                    hourlyPS_df['VS.RAB.FailEstabPS.DLCE.Cong (None)'] + hourlyPS_df['VS.RAB.FailEstabPS.Code.Cong (None)'] + hourlyPS_df['VS.RAB.FailEstabPS.ULPower.Cong (None)'] + \
                                    hourlyPS_df['VS.RAB.FailEstabPS.DLPower.Cong (None)'] + hourlyPS_df['VS.RAB.FailEstabPS.HSDPAUser.Cong (None)'] + hourlyPS_df['VS.RAB.FailEstabPS.HSUPAUser.Cong (None)']) / \
                                    (hourlyPS_df['VS.RAB.AttEstabPS.Str (None)'] + hourlyPS_df['VS.RAB.AttEstabPS.Int (None)'] + hourlyPS_df['VS.RAB.AttEstabPS.Bkg (None)']) *100

hourlyPS_df['PS RAB Drop Rate (%)'] = (hourlyPS_df['VS.RAB.AbnormRel.PS (None)'] + hourlyPS_df['VS.RAB.AbnormRel.PS.PCH (None)'] + hourlyPS_df['VS.RAB.AbnormRel.PS.D2P (None)'] + \
                                    hourlyPS_df['VS.RAB.AbnormRel.PS.F2P (None)']) / \
                                   (hourlyPS_df['VS.RAB.AbnormRel.PS (None)'] + hourlyPS_df['VS.RAB.NormRel.PS (None)'] + hourlyPS_df['VS.RAB.AbnormRel.PS.PCH (None)'] + \
                                    hourlyPS_df['VS.RAB.NormRel.PS.PCH (None)']) * 100
hourlyPS_df['PS HS- Drop Rate (%)'] =  hourlyPS_df['VS.HSDPA.RAB.AbnormRel (None)'] / (hourlyPS_df['VS.HSDPA.RAB.AbnormRel (None)'] + hourlyPS_df['VS.HSDPA.RAB.NormRel (None)'] + hourlyPS_df['VS.HSDPA.H2D.Succ (None)'] + hourlyPS_df['VS.HSDPA.H2F.Succ (None)'] +hourlyPS_df['VS.HSDPA.HHO.H2D.SuccOutIntraFreq (None)'] + hourlyPS_df['VS.HSDPA.HHO.H2D.SuccOutInterFreq (None)']) * 100
hourlyPS_df['HSDPA Throughput, kbps'] = hourlyPS_df['VS.HSDPA.MeanChThroughput (kbit/s)'] / active_cell_number # количество сот
hourlyPS_df['HSUPA Throughput, kbps'] = hourlyPS_df['VS.HSUPA.MeanChThroughput (kbit/s)'] / active_cell_number # количество сот
hourlyCS_df['Soft Handover Success rate, %'] = (hourlyCS_df['VS.SHO.SuccRLAdd (None)'] + hourlyCS_df['VS.SHO.SuccRLDel (None)']) / (hourlyCS_df['VS.SHO.AttRLAdd (None)'] + hourlyCS_df['VS.SHO.AttRLDel (None)']) * 100
hourlyCS_df['Hard Handover Success rate, %'] = hourlyCS_df['VS.HHO.SuccInterFreqOut (None)'] / hourlyCS_df['VS.HHO.AttInterFreqOut (None)'] * 100
hourlyCS_df['CS W2G Inter-RAT Handover Out SR'] = hourlyCS_df['IRATHO.SuccOutCS (None)'] / (hourlyCS_df['IRATHO.AttOutCS (None)'] - hourlyCS_df['VS.IRATHOCS.Cancel.ReEstab (None)']) * 100
hourlyCS_df['RRC Assignment SucessRate (CS BH), %'] = hourlyCS_df['RRC.SuccConnEstab.sum (None)'] / hourlyCS_df['VS.RRC.AttConnEstab.Sum (None)'] * 100
hourlyPS_df['RRC Assignment SucessRate (PS BH), %'] = hourlyPS_df['RRC.SuccConnEstab.sum (None)'] / hourlyPS_df['VS.RRC.AttConnEstab.Sum (None)'] * 100
hourlyCS_df['RRC Drop Rate (CS BH), %'] = (hourlyCS_df['RRC.AttConnRelCCCH.Cong (None)'] + hourlyCS_df['RRC.AttConnRelCCCH.Preempt (None)'] + hourlyCS_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                             hourlyCS_df['RRC.AttConnRelCCCH.Unspec (None)'] + hourlyCS_df['RRC.AttConnRelDCCH.Cong (None)'] + hourlyCS_df['RRC.AttConnRelDCCH.Preempt (None)'] + \
                                             hourlyCS_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + hourlyCS_df['RRC.AttConnRelDCCH.Unspec (None)'] + hourlyCS_df['VS.RRC.ConnRel.CellUpd (None)']) \
                                        / (hourlyCS_df['RRC.AttConnRelDCCH.Cong (None)'] + hourlyCS_df['RRC.AttConnRelDCCH.Preempt (None)'] + hourlyCS_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + \
                                           hourlyCS_df['RRC.AttConnRelDCCH.DSCR (None)'] + hourlyCS_df['RRC.AttConnRelDCCH.UsrInact (None)'] + hourlyCS_df['RRC.AttConnRelDCCH.Unspec (None)'] + \
                                           hourlyCS_df['RRC.AttConnRelCCCH.Cong (None)'] + hourlyCS_df['RRC.AttConnRelCCCH.Preempt (None)'] + hourlyCS_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                           hourlyCS_df['RRC.AttConnRelCCCH.DSCR (None)'] + hourlyCS_df['RRC.AttConnRelDCCH.Norm (None)'] + hourlyCS_df['RRC.AttConnRelCCCH.Norm (None)'] + \
                                           hourlyCS_df['RRC.AttConnRelCCCH.UsrInact (None)'] + hourlyCS_df['RRC.AttConnRelCCCH.Unspec (None)'] + hourlyCS_df['VS.RRC.ConnRel.CellUpd (None)'] + \
                                           hourlyCS_df['VS.DCCC.Succ.F2P (None)'] + hourlyCS_df['IRATHO.SuccOutCS (None)'] + hourlyCS_df['IRATHO.SuccOutPSUTRAN (None)'] + hourlyCS_df['VS.DCCC.Succ.F2U (None)'] + \
                                           hourlyCS_df['VS.DCCC.Succ.D2U (None)']) * 100
hourlyPS_df['RRC Drop Rate (PS BH), %'] = (hourlyPS_df['RRC.AttConnRelCCCH.Cong (None)'] + hourlyPS_df['RRC.AttConnRelCCCH.Preempt (None)'] + hourlyPS_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                             hourlyPS_df['RRC.AttConnRelCCCH.Unspec (None)'] + hourlyPS_df['RRC.AttConnRelDCCH.Cong (None)'] + hourlyPS_df['RRC.AttConnRelDCCH.Preempt (None)'] + \
                                             hourlyPS_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + hourlyPS_df['RRC.AttConnRelDCCH.Unspec (None)'] + hourlyPS_df['VS.RRC.ConnRel.CellUpd (None)']) \
                                        / (hourlyPS_df['RRC.AttConnRelDCCH.Cong (None)'] + hourlyPS_df['RRC.AttConnRelDCCH.Preempt (None)'] + hourlyPS_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + \
                                           hourlyPS_df['RRC.AttConnRelDCCH.DSCR (None)'] + hourlyPS_df['RRC.AttConnRelDCCH.UsrInact (None)'] + hourlyPS_df['RRC.AttConnRelDCCH.Unspec (None)'] + \
                                           hourlyPS_df['RRC.AttConnRelCCCH.Cong (None)'] + hourlyPS_df['RRC.AttConnRelCCCH.Preempt (None)'] + hourlyPS_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                           hourlyPS_df['RRC.AttConnRelCCCH.DSCR (None)'] + hourlyPS_df['RRC.AttConnRelDCCH.Norm (None)'] + hourlyPS_df['RRC.AttConnRelCCCH.Norm (None)'] + \
                                           hourlyPS_df['RRC.AttConnRelCCCH.UsrInact (None)'] + hourlyPS_df['RRC.AttConnRelCCCH.Unspec (None)'] + hourlyPS_df['VS.RRC.ConnRel.CellUpd (None)'] + \
                                           hourlyPS_df['VS.DCCC.Succ.F2P (None)'] + hourlyPS_df['IRATHO.SuccOutCS (None)'] + hourlyPS_df['IRATHO.SuccOutPSUTRAN (None)'] + hourlyPS_df['VS.DCCC.Succ.F2U (None)'] + \
                                           hourlyPS_df['VS.DCCC.Succ.D2U (None)']) * 100
hourlyCS_df['RAB Assignment Success Rate (CS), %'] = hourlyCS_df['VS.RAB.SuccEstabCS.AMR (None)'] / hourlyCS_df['VS.RAB.AttEstab.AMR (None)'] * 100
hourlyPS_df['RAB Assignment Success Rate (PS), %'] = (hourlyPS_df['VS.RAB.SuccEstabPS.Conv (None)'] + hourlyPS_df['VS.RAB.SuccEstabPS.Bkg (None)'] + hourlyPS_df['VS.RAB.SuccEstabPS.Int (None)'] + \
                                                   hourlyPS_df['VS.RAB.SuccEstabPS.Str (None)']) / \
                                                  (hourlyPS_df['VS.RAB.AttEstabPS.Bkg (None)'] + hourlyPS_df['VS.RAB.AttEstabPS.Int (None)'] + hourlyPS_df['VS.RAB.AttEstabPS.Str (None)'] + \
                                                   hourlyPS_df['VS.RAB.AttEstabPS.Conv (None)']) * 100
hourlyCS_df['CCSR CS,%'] = hourlyCS_df['RRC Assignment SucessRate (CS BH), %'] * (100 - hourlyCS_df['RRC Drop Rate (CS BH), %']) * hourlyCS_df['RAB Assignment Success Rate (CS), %'] * (100 - hourlyCS_df['CS RAB Drop Rate (%)'])/ 1000000
hourlyPS_df['CCSR PS,%'] = hourlyPS_df['RRC Assignment SucessRate (PS BH), %'] * (100 - hourlyPS_df['RRC Drop Rate (PS BH), %']) * hourlyPS_df['RAB Assignment Success Rate (PS), %'] * (100 - hourlyPS_df['PS RAB Drop Rate (%)'])/ 1000000

hourlyCS_df = hourlyCS_df.drop(list_1, axis=1)
hourlyCS_df = hourlyCS_df.transpose()
hourlyPS_df = hourlyPS_df.drop(list_1, axis=1)
hourlyPS_df = hourlyPS_df.transpose()


#daily_df.to_excel("C:/test/sts3G/daily_df.xls", engine='openpyxl', sheet_name='Book2')
#hourlyCS_df.to_excel("C:/test/sts3G/hourly_df.xls", engine='openpyxl', sheet_name='Book2')

with pd.ExcelWriter('C:/work/CityH_audit/sts/3G/3G_01-30.01_output.xls', engine='openpyxl') as writer: # C:/work/CityH_audit/sts/3G/Kahovka/3G_Kahovka_1_09_30.xls C:/test/sts3G/19-15_bh_newupd.xls
    daily_df.to_excel(writer, sheet_name='daily')
    hourlyCS_df.to_excel(writer, sheet_name='busy_hourCS')
    hourlyPS_df.to_excel(writer, sheet_name='busy_hourPS')






print('готово')
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
winsound.Beep(frequency, duration)