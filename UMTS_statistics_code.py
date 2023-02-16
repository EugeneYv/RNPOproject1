import pandas as pd
import winsound
''' количество активных сот 538!!! - используется для расчёта скорости HSDPA HSUPA,  для CityK 43
вывод посуточной статистики для UMTS. импортный файл - в МАЕ вывести в формате xlsx два файла, потом в экселе переделать в csv
'''
active_cell_number = 538  # количество активных сот !!!!

directory = 'C:/work/Herson_audit/sts/3G/'
csv_name1 = '3G_counters1_opt(2023-02-13_09'
csv_name2 = '3G_counters2(2023-02-13_09'
output_comment = '_output'  # что добавится в конце к названию файла


sts1_df = pd.read_csv(f"{directory}{csv_name1}.csv", sep=";", header=7, na_values='NIL')
sts1_df['date'] = sts1_df['Start Time'].str.split(' ').str[0]
sts1_df['hour'] = sts1_df['Start Time'].str.split(' ').str[1]
sts1_df['date'] = pd.to_datetime(sts1_df['date'])
sts1_df['week'] = sts1_df['date'].dt.isocalendar().week

sts2_df = pd.read_csv(f"{directory}{csv_name2}.csv", sep=";", header=7, na_values='NIL')
sts_df = pd.merge(sts1_df, sts2_df, how="left")

list_1 = ['RRC.AttConnEstab.EmgCall (None)','RRC.AttConnEstab.OrgConvCall (None)','RRC.AttConnEstab.TmConvCall (None)',\
          'RRC.SuccConnEstab.EmgCall (None)','RRC.SuccConnEstab.OrgConvCall (None)','RRC.SuccConnEstab.TmConvCall (None)',\
          'VS.AttCellUpdt.EmgCall.PCH (None)','VS.AttCellUpdt.OrgConvCall.PCH (None)',\
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
list_2 = ['CS traffic 3G, Erl','PS traffic 3G UL+DL, GB','CS RAB Drop Rate (%)','PS Blocking Rate (%)','PS RAB Drop Rate (%)','PS HS- Drop Rate (%)',\
          'HSDPA Throughput, kbps','HSUPA Throughput, kbps','Soft Handover Success rate, %','Hard Handover Success rate, %','CS W2G Inter-RAT Handover Out SR',\
          'RRC Assignment SucessRate (CS BH), %','RRC Assignment SucessRate (PS BH), %','RRC Drop Rate (CS BH), %','RRC Drop Rate (PS BH), %',\
          'RAB Assignment Success Rate (CS), %','RAB Assignment Success Rate (PS), %','CCSR CS,%','CCSR PS,%']

# кластер К:
list_cluster_K = ['Label=UH0881_U94, CellID=48814, LogicRNCID=501', \
                        'Label=UH0881_U96, CellID=48816, LogicRNCID=501', \
                        'Label=UH0881_U95, CellID=48815, LogicRNCID=501', \
                        'Label=UH0821_U96, CellID=48216, LogicRNCID=501', \
                        'Label=UH0821_U95, CellID=48215, LogicRNCID=501', \
                        'Label=UH0821_U94, CellID=48214, LogicRNCID=501', \
                        'Label=UH2981_U4, CellID=29814, LogicRNCID=501', \
                        'Label=UH2981_U3, CellID=29813, LogicRNCID=501', \
                        'Label=UH2981_U2, CellID=29812, LogicRNCID=501', \
                        'Label=UH2981_U6, CellID=29816, LogicRNCID=501', \
                        'Label=UH2981_U5, CellID=29815, LogicRNCID=501', \
                        'Label=UH1947_U3, CellID=19473, LogicRNCID=501', \
                        'Label=UH1947_U2, CellID=19472, LogicRNCID=501', \
                        'Label=UH2981_U1, CellID=29811, LogicRNCID=501', \
                        'Label=UH1947_U6, CellID=19476, LogicRNCID=501', \
                        'Label=UH1947_U5, CellID=19475, LogicRNCID=501', \
                        'Label=UH1947_U4, CellID=19474, LogicRNCID=501', \
                        'Label=UH1947_U1, CellID=19471, LogicRNCID=501', \
                        'Label=UH3925_U1, CellID=39251, LogicRNCID=501', \
                        'Label=UH3925_U6, CellID=39256, LogicRNCID=501', \
                        'Label=UH3925_U5, CellID=39255, LogicRNCID=501', \
                        'Label=UH3925_U4, CellID=39254, LogicRNCID=501', \
                        'Label=UH3925_U3, CellID=39253, LogicRNCID=501', \
                        'Label=UH3925_U2, CellID=39252, LogicRNCID=501', \
                        'Label=UH0970_U3, CellID=9703, LogicRNCID=501', \
                        'Label=UH0970_U6, CellID=9706, LogicRNCID=501', \
                        'Label=UH0970_U5, CellID=9705, LogicRNCID=501', \
                        'Label=UH0970_U4, CellID=9704, LogicRNCID=501', \
                        'Label=UH0881_U3, CellID=8813, LogicRNCID=501', \
                        'Label=UH0970_U2, CellID=9702, LogicRNCID=501', \
                        'Label=UH0970_U1, CellID=9701, LogicRNCID=501', \
                        'Label=UH0881_U6, CellID=8816, LogicRNCID=501', \
                        'Label=UH0881_U5, CellID=8815, LogicRNCID=501', \
                        'Label=UH0821_U4, CellID=8214, LogicRNCID=501', \
                        'Label=UH0821_U2, CellID=8212, LogicRNCID=501', \
                        'Label=UH0821_U1, CellID=8211, LogicRNCID=501', \
                        'Label=UH0881_U4, CellID=8814, LogicRNCID=501', \
                        'Label=UH0821_U3, CellID=8213, LogicRNCID=501', \
                        'Label=UH0881_U2, CellID=8812, LogicRNCID=501', \
                        'Label=UH0881_U1, CellID=8811, LogicRNCID=501', \
                        'Label=UH0821_U6, CellID=8216, LogicRNCID=501', \
                        'Label=UH0821_U5, CellID=8215, LogicRNCID=501', \
                        'Label=UH0881_U97, CellID=48817, LogicRNCID=501', \
                        'Label=UH0821_U98, CellID=48218, LogicRNCID=501', \
                        'Label=UH0821_U97, CellID=48217, LogicRNCID=501', \
                        'Label=UH0821_U99, CellID=48219, LogicRNCID=501']

# G cluster
list_cluster_G = ['Label=UH0881_U94, CellID=48814, LogicRNCID=501', \
                'Label=UH0881_U96, CellID=48816, LogicRNCID=501', \
                'Label=UH0881_U95, CellID=48815, LogicRNCID=501', \
                'Label=UH0821_U96, CellID=48216, LogicRNCID=501', \
                'Label=UH0821_U95, CellID=48215, LogicRNCID=501', \
                'Label=UH0821_U94, CellID=48214, LogicRNCID=501', \
                'Label=UH2981_U4, CellID=29814, LogicRNCID=501', \
                'Label=UH2981_U3, CellID=29813, LogicRNCID=501', \
                'Label=UH2981_U2, CellID=29812, LogicRNCID=501', \
                'Label=UH2981_U6, CellID=29816, LogicRNCID=501', \
                'Label=UH2981_U5, CellID=29815, LogicRNCID=501', \
                'Label=UH1947_U3, CellID=19473, LogicRNCID=501', \
                'Label=UH1947_U2, CellID=19472, LogicRNCID=501', \
                'Label=UH2981_U1, CellID=29811, LogicRNCID=501', \
                'Label=UH1947_U6, CellID=19476, LogicRNCID=501', \
                'Label=UH1947_U5, CellID=19475, LogicRNCID=501', \
                'Label=UH1947_U4, CellID=19474, LogicRNCID=501', \
                'Label=UH1947_U1, CellID=19471, LogicRNCID=501', \
                'Label=UH3925_U1, CellID=39251, LogicRNCID=501', \
                'Label=UH3925_U6, CellID=39256, LogicRNCID=501', \
                'Label=UH3925_U5, CellID=39255, LogicRNCID=501', \
                'Label=UH3925_U4, CellID=39254, LogicRNCID=501', \
                'Label=UH3925_U3, CellID=39253, LogicRNCID=501', \
                'Label=UH3925_U2, CellID=39252, LogicRNCID=501', \
                'Label=UH0970_U3, CellID=9703, LogicRNCID=501', \
                'Label=UH0970_U6, CellID=9706, LogicRNCID=501', \
                'Label=UH0970_U5, CellID=9705, LogicRNCID=501', \
                'Label=UH0970_U4, CellID=9704, LogicRNCID=501', \
                'Label=UH0881_U3, CellID=8813, LogicRNCID=501', \
                'Label=UH0970_U2, CellID=9702, LogicRNCID=501', \
                'Label=UH0970_U1, CellID=9701, LogicRNCID=501', \
                'Label=UH0881_U6, CellID=8816, LogicRNCID=501', \
                'Label=UH0881_U5, CellID=8815, LogicRNCID=501', \
                'Label=UH0821_U4, CellID=8214, LogicRNCID=501', \
                'Label=UH0821_U2, CellID=8212, LogicRNCID=501', \
                'Label=UH0821_U1, CellID=8211, LogicRNCID=501', \
                'Label=UH0881_U4, CellID=8814, LogicRNCID=501', \
                'Label=UH0821_U3, CellID=8213, LogicRNCID=501', \
                'Label=UH0881_U2, CellID=8812, LogicRNCID=501', \
                'Label=UH0881_U1, CellID=8811, LogicRNCID=501', \
                'Label=UH0821_U6, CellID=8216, LogicRNCID=501', \
                'Label=UH0821_U5, CellID=8215, LogicRNCID=501', \
                'Label=UH0881_U97, CellID=48817, LogicRNCID=501', \
                'Label=UH0821_U98, CellID=48218, LogicRNCID=501', \
                'Label=UH0821_U97, CellID=48217, LogicRNCID=501', \
                'Label=UH0821_U99, CellID=48219, LogicRNCID=501']

# !!! фильтрация по скластеру !!!:
#sts_df = sts_df[sts_df['GCELL'].isin(list_cluster)]

# обработка weekly:
weekly_df = sts_df.groupby(['week'])[list_1]. sum().reset_index()

weekly_df['CS traffic 3G, Erl'] = weekly_df['CS Voice Traffic Volume (Erl)']
weekly_df['PS traffic 3G UL+DL, GB'] = (weekly_df['VS.HSUPA.MeanChThroughput.TotalBytes (byte)'] + weekly_df['VS.PS.Bkg.DL.8.Traffic (bit)'] + weekly_df['VS.PS.Bkg.DL.16.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Bkg.DL.32.Traffic (bit)'] + weekly_df['VS.PS.Bkg.DL.64.Traffic (bit)'] + weekly_df['VS.PS.Bkg.DL.128.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Bkg.DL.144.Traffic (bit)'] + weekly_df['VS.PS.Bkg.DL.256.Traffic (bit)'] + weekly_df['VS.PS.Bkg.DL.384.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Bkg.UL.8.Traffic (bit)'] + weekly_df['VS.PS.Bkg.UL.16.Traffic (bit)'] + weekly_df['VS.PS.Bkg.UL.32.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Bkg.UL.64.Traffic (bit)'] + weekly_df['VS.PS.Bkg.UL.128.Traffic (bit)'] + weekly_df['VS.PS.Bkg.UL.144.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Bkg.UL.256.Traffic (bit)'] + weekly_df['VS.PS.Bkg.UL.384.Traffic (bit)'] + weekly_df['VS.PS.Int.DL.8.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Int.DL.16.Traffic (bit)'] + weekly_df['VS.PS.Int.DL.32.Traffic (bit)'] + weekly_df['VS.PS.Int.DL.64.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Int.DL.128.Traffic (bit)'] + weekly_df['VS.PS.Int.DL.144.Traffic (bit)'] + weekly_df['VS.PS.Int.DL.256.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Int.DL.384.Traffic (bit)'] + weekly_df['VS.PS.Int.UL.8.Traffic (bit)'] + weekly_df['VS.PS.Int.UL.16.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Int.UL.32.Traffic (bit)'] + weekly_df['VS.PS.Int.UL.64.Traffic (bit)'] + weekly_df['VS.PS.Int.UL.128.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Int.UL.144.Traffic (bit)'] + weekly_df['VS.PS.Int.UL.256.Traffic (bit)'] + weekly_df['VS.PS.Int.UL.384.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Str.DL.32.Traffic (bit)'] + weekly_df['VS.PS.Str.DL.64.Traffic (bit)'] + weekly_df['VS.PS.Str.DL.128.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Str.DL.144.Traffic (bit)'] + weekly_df['VS.PS.Str.UL.16.Traffic (bit)'] + weekly_df['VS.PS.Str.UL.32.Traffic (bit)'] + \
                                      weekly_df['VS.PS.Str.UL.64.Traffic (bit)'] + weekly_df['VS.HSDPA.MeanChThroughput.TotalBytes (byte)']) / 1000000
weekly_df['CS RAB Drop Rate (%)'] = weekly_df['VS.RAB.AbnormRel.CS (None)'] / (weekly_df['VS.RAB.AbnormRel.CS (None)'] + weekly_df['VS.RAB.NormRel.CS (None)']) * 100
weekly_df['PS Blocking Rate (%)'] = (weekly_df['VS.RAB.FailEstabPS.DLIUBBand.Cong (None)'] + weekly_df['VS.RAB.FailEstabPS.ULIUBBand.Cong (None)'] + weekly_df['VS.RAB.FailEstabPS.ULCE.Cong (None)'] + \
                                    weekly_df['VS.RAB.FailEstabPS.DLCE.Cong (None)'] + weekly_df['VS.RAB.FailEstabPS.Code.Cong (None)'] + weekly_df['VS.RAB.FailEstabPS.ULPower.Cong (None)'] + \
                                    weekly_df['VS.RAB.FailEstabPS.DLPower.Cong (None)'] + weekly_df['VS.RAB.FailEstabPS.HSDPAUser.Cong (None)'] + weekly_df['VS.RAB.FailEstabPS.HSUPAUser.Cong (None)']) / \
                                    (weekly_df['VS.RAB.AttEstabPS.Str (None)'] + weekly_df['VS.RAB.AttEstabPS.Int (None)'] + weekly_df['VS.RAB.AttEstabPS.Bkg (None)']) *100

weekly_df['PS RAB Drop Rate (%)'] = (weekly_df['VS.RAB.AbnormRel.PS (None)'] + weekly_df['VS.RAB.AbnormRel.PS.PCH (None)'] + weekly_df['VS.RAB.AbnormRel.PS.D2P (None)'] + \
                                    weekly_df['VS.RAB.AbnormRel.PS.F2P (None)']) / \
                                   (weekly_df['VS.RAB.AbnormRel.PS (None)'] + weekly_df['VS.RAB.NormRel.PS (None)'] + weekly_df['VS.RAB.AbnormRel.PS.PCH (None)'] + \
                                    weekly_df['VS.RAB.NormRel.PS.PCH (None)']) * 100
weekly_df['PS HS- Drop Rate (%)'] =  weekly_df['VS.HSDPA.RAB.AbnormRel (None)'] / (weekly_df['VS.HSDPA.RAB.AbnormRel (None)'] + weekly_df['VS.HSDPA.RAB.NormRel (None)'] + weekly_df['VS.HSDPA.H2D.Succ (None)'] + weekly_df['VS.HSDPA.H2F.Succ (None)'] +weekly_df['VS.HSDPA.HHO.H2D.SuccOutIntraFreq (None)'] + weekly_df['VS.HSDPA.HHO.H2D.SuccOutInterFreq (None)']) * 100
weekly_df['HSDPA Throughput, kbps'] = weekly_df['VS.HSDPA.MeanChThroughput (kbit/s)'] / active_cell_number / 24 / 7 # количество сот
weekly_df['HSUPA Throughput, kbps'] = weekly_df['VS.HSUPA.MeanChThroughput (kbit/s)'] / active_cell_number / 24 / 7 # количество сот
weekly_df['Soft Handover Success rate, %'] = (weekly_df['VS.SHO.SuccRLAdd (None)'] + weekly_df['VS.SHO.SuccRLDel (None)']) / (weekly_df['VS.SHO.AttRLAdd (None)'] + weekly_df['VS.SHO.AttRLDel (None)']) * 100
weekly_df['Hard Handover Success rate, %'] = weekly_df['VS.HHO.SuccInterFreqOut (None)'] / weekly_df['VS.HHO.AttInterFreqOut (None)'] * 100
weekly_df['CS W2G Inter-RAT Handover Out SR'] = weekly_df['IRATHO.SuccOutCS (None)'] / (weekly_df['IRATHO.AttOutCS (None)'] - weekly_df['VS.IRATHOCS.Cancel.ReEstab (None)']) * 100
weekly_df['RRC Assignment SucessRate (CS BH), %'] = weekly_df['RRC.SuccConnEstab.sum (None)'] / weekly_df['VS.RRC.AttConnEstab.Sum (None)'] * 100
weekly_df['RRC Assignment SucessRate (PS BH), %'] = weekly_df['RRC.SuccConnEstab.sum (None)'] / weekly_df['VS.RRC.AttConnEstab.Sum (None)'] * 100
weekly_df['RRC Drop Rate (CS BH), %'] = (weekly_df['RRC.AttConnRelCCCH.Cong (None)'] + weekly_df['RRC.AttConnRelCCCH.Preempt (None)'] + weekly_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                             weekly_df['RRC.AttConnRelCCCH.Unspec (None)'] + weekly_df['RRC.AttConnRelDCCH.Cong (None)'] + weekly_df['RRC.AttConnRelDCCH.Preempt (None)'] + \
                                             weekly_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + weekly_df['RRC.AttConnRelDCCH.Unspec (None)'] + weekly_df['VS.RRC.ConnRel.CellUpd (None)']) \
                                        / (weekly_df['RRC.AttConnRelDCCH.Cong (None)'] + weekly_df['RRC.AttConnRelDCCH.Preempt (None)'] + weekly_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + \
                                           weekly_df['RRC.AttConnRelDCCH.DSCR (None)'] + weekly_df['RRC.AttConnRelDCCH.UsrInact (None)'] + weekly_df['RRC.AttConnRelDCCH.Unspec (None)'] + \
                                           weekly_df['RRC.AttConnRelCCCH.Cong (None)'] + weekly_df['RRC.AttConnRelCCCH.Preempt (None)'] + weekly_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                           weekly_df['RRC.AttConnRelCCCH.DSCR (None)'] + weekly_df['RRC.AttConnRelDCCH.Norm (None)'] + weekly_df['RRC.AttConnRelCCCH.Norm (None)'] + \
                                           weekly_df['RRC.AttConnRelCCCH.UsrInact (None)'] + weekly_df['RRC.AttConnRelCCCH.Unspec (None)'] + weekly_df['VS.RRC.ConnRel.CellUpd (None)'] + \
                                           weekly_df['VS.DCCC.Succ.F2P (None)'] + weekly_df['IRATHO.SuccOutCS (None)'] + weekly_df['IRATHO.SuccOutPSUTRAN (None)'] + weekly_df['VS.DCCC.Succ.F2U (None)'] + \
                                           weekly_df['VS.DCCC.Succ.D2U (None)']) * 100
weekly_df['RRC Drop Rate (PS BH), %'] = (weekly_df['RRC.AttConnRelCCCH.Cong (None)'] + weekly_df['RRC.AttConnRelCCCH.Preempt (None)'] + weekly_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                             weekly_df['RRC.AttConnRelCCCH.Unspec (None)'] + weekly_df['RRC.AttConnRelDCCH.Cong (None)'] + weekly_df['RRC.AttConnRelDCCH.Preempt (None)'] + \
                                             weekly_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + weekly_df['RRC.AttConnRelDCCH.Unspec (None)'] + weekly_df['VS.RRC.ConnRel.CellUpd (None)']) \
                                        / (weekly_df['RRC.AttConnRelDCCH.Cong (None)'] + weekly_df['RRC.AttConnRelDCCH.Preempt (None)'] + weekly_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + \
                                           weekly_df['RRC.AttConnRelDCCH.DSCR (None)'] + weekly_df['RRC.AttConnRelDCCH.UsrInact (None)'] + weekly_df['RRC.AttConnRelDCCH.Unspec (None)'] + \
                                           weekly_df['RRC.AttConnRelCCCH.Cong (None)'] + weekly_df['RRC.AttConnRelCCCH.Preempt (None)'] + weekly_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                           weekly_df['RRC.AttConnRelCCCH.DSCR (None)'] + weekly_df['RRC.AttConnRelDCCH.Norm (None)'] + weekly_df['RRC.AttConnRelCCCH.Norm (None)'] + \
                                           weekly_df['RRC.AttConnRelCCCH.UsrInact (None)'] + weekly_df['RRC.AttConnRelCCCH.Unspec (None)'] + weekly_df['VS.RRC.ConnRel.CellUpd (None)'] + \
                                           weekly_df['VS.DCCC.Succ.F2P (None)'] + weekly_df['IRATHO.SuccOutCS (None)'] + weekly_df['IRATHO.SuccOutPSUTRAN (None)'] + weekly_df['VS.DCCC.Succ.F2U (None)'] + \
                                           weekly_df['VS.DCCC.Succ.D2U (None)']) * 100
weekly_df['RAB Assignment Success Rate (CS), %'] = weekly_df['VS.RAB.SuccEstabCS.AMR (None)'] / weekly_df['VS.RAB.AttEstab.AMR (None)'] * 100
weekly_df['RAB Assignment Success Rate (PS), %'] = (weekly_df['VS.RAB.SuccEstabPS.Conv (None)'] + weekly_df['VS.RAB.SuccEstabPS.Bkg (None)'] + weekly_df['VS.RAB.SuccEstabPS.Int (None)'] + \
                                                   weekly_df['VS.RAB.SuccEstabPS.Str (None)']) / \
                                                  (weekly_df['VS.RAB.AttEstabPS.Bkg (None)'] + weekly_df['VS.RAB.AttEstabPS.Int (None)'] + weekly_df['VS.RAB.AttEstabPS.Str (None)'] + \
                                                   weekly_df['VS.RAB.AttEstabPS.Conv (None)']) * 100
weekly_df['CCSR3G, %'] = weekly_df['RRC Assignment SucessRate (CS BH), %'] * (100 - weekly_df['RRC Drop Rate (CS BH), %']) * weekly_df['RAB Assignment Success Rate (CS), %'] * (100 - weekly_df['CS RAB Drop Rate (%)'])/ 1000000
weekly_df['DCSR3G, %'] = weekly_df['RRC Assignment SucessRate (PS BH), %'] * (100 - weekly_df['RRC Drop Rate (PS BH), %']) * weekly_df['RAB Assignment Success Rate (PS), %'] * (100 - weekly_df['PS RAB Drop Rate (%)'])/ 1000000
weekly_df = weekly_df.drop(list_1, axis=1)
weekly_df = weekly_df.transpose()


# обработка daily:
daily_df = sts_df.groupby(['date'])[list_1]. sum().reset_index()

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
daily_df['CCSR3G, %'] = daily_df['RRC Assignment SucessRate (CS BH), %'] * (100 - daily_df['RRC Drop Rate (CS BH), %']) * daily_df['RAB Assignment Success Rate (CS), %'] * (100 - daily_df['CS RAB Drop Rate (%)'])/ 1000000
daily_df['DCSR3G, %'] = daily_df['RRC Assignment SucessRate (PS BH), %'] * (100 - daily_df['RRC Drop Rate (PS BH), %']) * daily_df['RAB Assignment Success Rate (PS), %'] * (100 - daily_df['PS RAB Drop Rate (%)'])/ 1000000
daily_df = daily_df.drop(list_1, axis=1)
daily_df = daily_df.transpose()

# обработка часовая
hourly_df = sts_df.groupby(['date', 'hour'])[list_1].sum().reset_index()

hourly_df['CS traffic 3G, Erl'] = hourly_df['CS Voice Traffic Volume (Erl)']
hourly_df['PS traffic 3G UL+DL, GB'] = (hourly_df['VS.HSUPA.MeanChThroughput.TotalBytes (byte)'] + hourly_df['VS.PS.Bkg.DL.8.Traffic (bit)'] + hourly_df['VS.PS.Bkg.DL.16.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Bkg.DL.32.Traffic (bit)'] + hourly_df['VS.PS.Bkg.DL.64.Traffic (bit)'] + hourly_df['VS.PS.Bkg.DL.128.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Bkg.DL.144.Traffic (bit)'] + hourly_df['VS.PS.Bkg.DL.256.Traffic (bit)'] + hourly_df['VS.PS.Bkg.DL.384.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Bkg.UL.8.Traffic (bit)'] + hourly_df['VS.PS.Bkg.UL.16.Traffic (bit)'] + hourly_df['VS.PS.Bkg.UL.32.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Bkg.UL.64.Traffic (bit)'] + hourly_df['VS.PS.Bkg.UL.128.Traffic (bit)'] + hourly_df['VS.PS.Bkg.UL.144.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Bkg.UL.256.Traffic (bit)'] + hourly_df['VS.PS.Bkg.UL.384.Traffic (bit)'] + hourly_df['VS.PS.Int.DL.8.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Int.DL.16.Traffic (bit)'] + hourly_df['VS.PS.Int.DL.32.Traffic (bit)'] + hourly_df['VS.PS.Int.DL.64.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Int.DL.128.Traffic (bit)'] + hourly_df['VS.PS.Int.DL.144.Traffic (bit)'] + hourly_df['VS.PS.Int.DL.256.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Int.DL.384.Traffic (bit)'] + hourly_df['VS.PS.Int.UL.8.Traffic (bit)'] + hourly_df['VS.PS.Int.UL.16.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Int.UL.32.Traffic (bit)'] + hourly_df['VS.PS.Int.UL.64.Traffic (bit)'] + hourly_df['VS.PS.Int.UL.128.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Int.UL.144.Traffic (bit)'] + hourly_df['VS.PS.Int.UL.256.Traffic (bit)'] + hourly_df['VS.PS.Int.UL.384.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Str.DL.32.Traffic (bit)'] + hourly_df['VS.PS.Str.DL.64.Traffic (bit)'] + hourly_df['VS.PS.Str.DL.128.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Str.DL.144.Traffic (bit)'] + hourly_df['VS.PS.Str.UL.16.Traffic (bit)'] + hourly_df['VS.PS.Str.UL.32.Traffic (bit)'] + \
                                      hourly_df['VS.PS.Str.UL.64.Traffic (bit)'] + hourly_df['VS.HSDPA.MeanChThroughput.TotalBytes (byte)']) / 1000000
hourly_df['CS RAB Drop Rate (%)'] = hourly_df['VS.RAB.AbnormRel.CS (None)'] / (hourly_df['VS.RAB.AbnormRel.CS (None)'] + hourly_df['VS.RAB.NormRel.CS (None)']) * 100
hourly_df['PS Blocking Rate (%)'] = (hourly_df['VS.RAB.FailEstabPS.DLIUBBand.Cong (None)'] + hourly_df['VS.RAB.FailEstabPS.ULIUBBand.Cong (None)'] + hourly_df['VS.RAB.FailEstabPS.ULCE.Cong (None)'] + \
                                    hourly_df['VS.RAB.FailEstabPS.DLCE.Cong (None)'] + hourly_df['VS.RAB.FailEstabPS.Code.Cong (None)'] + hourly_df['VS.RAB.FailEstabPS.ULPower.Cong (None)'] + \
                                    hourly_df['VS.RAB.FailEstabPS.DLPower.Cong (None)'] + hourly_df['VS.RAB.FailEstabPS.HSDPAUser.Cong (None)'] + hourly_df['VS.RAB.FailEstabPS.HSUPAUser.Cong (None)']) / \
                                    (hourly_df['VS.RAB.AttEstabPS.Str (None)'] + hourly_df['VS.RAB.AttEstabPS.Int (None)'] + hourly_df['VS.RAB.AttEstabPS.Bkg (None)']) *100

hourly_df['PS RAB Drop Rate (%)'] = (hourly_df['VS.RAB.AbnormRel.PS (None)'] + hourly_df['VS.RAB.AbnormRel.PS.PCH (None)'] + hourly_df['VS.RAB.AbnormRel.PS.D2P (None)'] + \
                                    hourly_df['VS.RAB.AbnormRel.PS.F2P (None)']) / \
                                   (hourly_df['VS.RAB.AbnormRel.PS (None)'] + hourly_df['VS.RAB.NormRel.PS (None)'] + hourly_df['VS.RAB.AbnormRel.PS.PCH (None)'] + \
                                    hourly_df['VS.RAB.NormRel.PS.PCH (None)']) * 100
hourly_df['PS HS- Drop Rate (%)'] =  hourly_df['VS.HSDPA.RAB.AbnormRel (None)'] / (hourly_df['VS.HSDPA.RAB.AbnormRel (None)'] + hourly_df['VS.HSDPA.RAB.NormRel (None)'] + hourly_df['VS.HSDPA.H2D.Succ (None)'] + hourly_df['VS.HSDPA.H2F.Succ (None)'] +hourly_df['VS.HSDPA.HHO.H2D.SuccOutIntraFreq (None)'] + hourly_df['VS.HSDPA.HHO.H2D.SuccOutInterFreq (None)']) * 100
hourly_df['HSDPA Throughput, kbps'] = hourly_df['VS.HSDPA.MeanChThroughput (kbit/s)'] / active_cell_number # количество сот
hourly_df['HSUPA Throughput, kbps'] = hourly_df['VS.HSUPA.MeanChThroughput (kbit/s)'] / active_cell_number # количество сот
hourly_df['Soft Handover Success rate, %'] = (hourly_df['VS.SHO.SuccRLAdd (None)'] + hourly_df['VS.SHO.SuccRLDel (None)']) / (hourly_df['VS.SHO.AttRLAdd (None)'] + hourly_df['VS.SHO.AttRLDel (None)']) * 100
hourly_df['Hard Handover Success rate, %'] = hourly_df['VS.HHO.SuccInterFreqOut (None)'] / hourly_df['VS.HHO.AttInterFreqOut (None)'] * 100
hourly_df['CS W2G Inter-RAT Handover Out SR'] = hourly_df['IRATHO.SuccOutCS (None)'] / (hourly_df['IRATHO.AttOutCS (None)'] - hourly_df['VS.IRATHOCS.Cancel.ReEstab (None)']) * 100
hourly_df['RRC Assignment SucessRate (CS BH), %'] = hourly_df['RRC.SuccConnEstab.sum (None)'] / hourly_df['VS.RRC.AttConnEstab.Sum (None)'] * 100
hourly_df['RRC Assignment SucessRate (PS BH), %'] = hourly_df['RRC.SuccConnEstab.sum (None)'] / hourly_df['VS.RRC.AttConnEstab.Sum (None)'] * 100
hourly_df['RRC Drop Rate (CS BH), %'] = (hourly_df['RRC.AttConnRelCCCH.Cong (None)'] + hourly_df['RRC.AttConnRelCCCH.Preempt (None)'] + hourly_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                             hourly_df['RRC.AttConnRelCCCH.Unspec (None)'] + hourly_df['RRC.AttConnRelDCCH.Cong (None)'] + hourly_df['RRC.AttConnRelDCCH.Preempt (None)'] + \
                                             hourly_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + hourly_df['RRC.AttConnRelDCCH.Unspec (None)'] + hourly_df['VS.RRC.ConnRel.CellUpd (None)']) \
                                        / (hourly_df['RRC.AttConnRelDCCH.Cong (None)'] + hourly_df['RRC.AttConnRelDCCH.Preempt (None)'] + hourly_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + \
                                           hourly_df['RRC.AttConnRelDCCH.DSCR (None)'] + hourly_df['RRC.AttConnRelDCCH.UsrInact (None)'] + hourly_df['RRC.AttConnRelDCCH.Unspec (None)'] + \
                                           hourly_df['RRC.AttConnRelCCCH.Cong (None)'] + hourly_df['RRC.AttConnRelCCCH.Preempt (None)'] + hourly_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                           hourly_df['RRC.AttConnRelCCCH.DSCR (None)'] + hourly_df['RRC.AttConnRelDCCH.Norm (None)'] + hourly_df['RRC.AttConnRelCCCH.Norm (None)'] + \
                                           hourly_df['RRC.AttConnRelCCCH.UsrInact (None)'] + hourly_df['RRC.AttConnRelCCCH.Unspec (None)'] + hourly_df['VS.RRC.ConnRel.CellUpd (None)'] + \
                                           hourly_df['VS.DCCC.Succ.F2P (None)'] + hourly_df['IRATHO.SuccOutCS (None)'] + hourly_df['IRATHO.SuccOutPSUTRAN (None)'] + hourly_df['VS.DCCC.Succ.F2U (None)'] + \
                                           hourly_df['VS.DCCC.Succ.D2U (None)']) * 100
hourly_df['RRC Drop Rate (PS BH), %'] = (hourly_df['RRC.AttConnRelCCCH.Cong (None)'] + hourly_df['RRC.AttConnRelCCCH.Preempt (None)'] + hourly_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                             hourly_df['RRC.AttConnRelCCCH.Unspec (None)'] + hourly_df['RRC.AttConnRelDCCH.Cong (None)'] + hourly_df['RRC.AttConnRelDCCH.Preempt (None)'] + \
                                             hourly_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + hourly_df['RRC.AttConnRelDCCH.Unspec (None)'] + hourly_df['VS.RRC.ConnRel.CellUpd (None)']) \
                                        / (hourly_df['RRC.AttConnRelDCCH.Cong (None)'] + hourly_df['RRC.AttConnRelDCCH.Preempt (None)'] + hourly_df['RRC.AttConnRelDCCH.ReEstRej (None)'] + \
                                           hourly_df['RRC.AttConnRelDCCH.DSCR (None)'] + hourly_df['RRC.AttConnRelDCCH.UsrInact (None)'] + hourly_df['RRC.AttConnRelDCCH.Unspec (None)'] + \
                                           hourly_df['RRC.AttConnRelCCCH.Cong (None)'] + hourly_df['RRC.AttConnRelCCCH.Preempt (None)'] + hourly_df['RRC.AttConnRelCCCH.ReEstRej (None)'] + \
                                           hourly_df['RRC.AttConnRelCCCH.DSCR (None)'] + hourly_df['RRC.AttConnRelDCCH.Norm (None)'] + hourly_df['RRC.AttConnRelCCCH.Norm (None)'] + \
                                           hourly_df['RRC.AttConnRelCCCH.UsrInact (None)'] + hourly_df['RRC.AttConnRelCCCH.Unspec (None)'] + hourly_df['VS.RRC.ConnRel.CellUpd (None)'] + \
                                           hourly_df['VS.DCCC.Succ.F2P (None)'] + hourly_df['IRATHO.SuccOutCS (None)'] + hourly_df['IRATHO.SuccOutPSUTRAN (None)'] + hourly_df['VS.DCCC.Succ.F2U (None)'] + \
                                           hourly_df['VS.DCCC.Succ.D2U (None)']) * 100
hourly_df['RAB Assignment Success Rate (CS), %'] = hourly_df['VS.RAB.SuccEstabCS.AMR (None)'] / hourly_df['VS.RAB.AttEstab.AMR (None)'] * 100
hourly_df['RAB Assignment Success Rate (PS), %'] = (hourly_df['VS.RAB.SuccEstabPS.Conv (None)'] + hourly_df['VS.RAB.SuccEstabPS.Bkg (None)'] + hourly_df['VS.RAB.SuccEstabPS.Int (None)'] + \
                                                   hourly_df['VS.RAB.SuccEstabPS.Str (None)']) / \
                                                  (hourly_df['VS.RAB.AttEstabPS.Bkg (None)'] + hourly_df['VS.RAB.AttEstabPS.Int (None)'] + hourly_df['VS.RAB.AttEstabPS.Str (None)'] + \
                                                   hourly_df['VS.RAB.AttEstabPS.Conv (None)']) * 100
hourly_df['CCSR3G, %'] = hourly_df['RRC Assignment SucessRate (CS BH), %'] * (100 - hourly_df['RRC Drop Rate (CS BH), %']) * hourly_df['RAB Assignment Success Rate (CS), %'] * (100 - hourly_df['CS RAB Drop Rate (%)'])/ 1000000
hourly_df['DCSR3G, %'] = hourly_df['RRC Assignment SucessRate (PS BH), %'] * (100 - hourly_df['RRC Drop Rate (PS BH), %']) * hourly_df['RAB Assignment Success Rate (PS), %'] * (100 - hourly_df['PS RAB Drop Rate (%)'])/ 1000000

hourly_df = hourly_df.drop(list_1, axis=1)
hourly_df = hourly_df.transpose()


#####
# обработка busy hour
hourly1_df = sts_df.groupby(['date', 'hour'])[list_1].sum().reset_index()
max_index_PS = hourly1_df.groupby('date')['VS.HSDPA.MeanChThroughput.TotalBytes (byte)'].idxmax()
hourlyPS_df = hourly1_df.loc[max_index_PS]
max_index_CS = hourly1_df.groupby('date')['CS Voice Traffic Volume (Erl)'].idxmax()
hourlyCS_df = hourly1_df.loc[max_index_CS]

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
hourlyCS_df['CCSR3G, %'] = hourlyCS_df['RRC Assignment SucessRate (CS BH), %'] * (100 - hourlyCS_df['RRC Drop Rate (CS BH), %']) * hourlyCS_df['RAB Assignment Success Rate (CS), %'] * (100 - hourlyCS_df['CS RAB Drop Rate (%)'])/ 1000000
hourlyPS_df['DCSR3G, %'] = hourlyPS_df['RRC Assignment SucessRate (PS BH), %'] * (100 - hourlyPS_df['RRC Drop Rate (PS BH), %']) * hourlyPS_df['RAB Assignment Success Rate (PS), %'] * (100 - hourlyPS_df['PS RAB Drop Rate (%)'])/ 1000000

hourlyCS_df = hourlyCS_df.drop(list_1, axis=1)
hourlyCS_df = hourlyCS_df.transpose()
hourlyPS_df = hourlyPS_df.drop(list_1, axis=1)
hourlyPS_df = hourlyPS_df.transpose()


#daily_df.to_excel("C:/test/sts3G/daily_df.xls", engine='openpyxl', sheet_name='Book2')
#hourlyCS_df.to_excel("C:/test/sts3G/hourly_df.xls", engine='openpyxl', sheet_name='Book2')

with pd.ExcelWriter(f"{directory}{csv_name1}{output_comment}.xls", engine='openpyxl') as writer:
    weekly_df.to_excel(writer, sheet_name='weekly')
    daily_df.to_excel(writer, sheet_name='daily')
    hourly_df.to_excel(writer, sheet_name='hourly')
    hourlyCS_df.to_excel(writer, sheet_name='busy_hourCS')
    hourlyPS_df.to_excel(writer, sheet_name='busy_hourPS')






print('готово')
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
winsound.Beep(frequency, duration)