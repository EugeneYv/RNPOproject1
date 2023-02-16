import pandas as pd
import winsound
'''вывод посуточной статистики для LTE. импортный файл - в МАЕ вывести в формате xlsx, потом в экселе переделать в csv'''

active_cell_number = 398  # ввести количество активных сот !!!!  19    398

directory = 'C:/work/Herson_audit/sts/4G/' # ввести директорию где лежит файл
csv_name = '4G_counters(2023-02-12'  # ввести имя файла
output_comment = '_output'  # что добавится в конце к названию файла

sts_df = pd.read_csv(f"{directory}{csv_name}.csv", sep=";", header=7, na_values='NIL')
#sts_df = pd.read_csv("C:/work/Herson_audit/sts/4G/Kahovka/4G_Kahovka_24-02.02.csv", sep=";", header=7, na_values='NIL')
#sts_df = pd.read_csv("C:/test/sts4G/4G_counters(2023-01-09.csv", sep=";", header=7, na_values='NIL')

sts_df['date'] = sts_df['Start Time'].str.split(' ').str[0]
sts_df['hour'] = sts_df['Start Time'].str.split(' ').str[1]

sts_df['date'] = pd.to_datetime(sts_df['date'])
sts_df['week'] = sts_df['date'].dt.isocalendar().week

list_1 = [ 'L.Cell.Avail.Dur (s)', 'L.ChMeas.PRB.DL.Avail (None)', 'L.ChMeas.PRB.DL.Used.Avg (None)', 'L.ChMeas.PRB.UL.Avail (None)', 'L.ChMeas.PRB.UL.Used.Avg (None)',\
           'L.CSFB.E2G (None)', 'L.CSFB.E2W (None)', 'L.E-RAB.AbnormRel (None)', 'L.E-RAB.AttEst (None)', 'L.E-RAB.FailEst.X2AP (None)', 'L.E-RAB.NormRel (None)', \
           'L.E-RAB.NormRel.IRatHOOut (None)', 'L.E-RAB.SuccEst (None)', 'L.HHO.IntereNB.InterFreq.ExecAttOut (None)', 'L.HHO.IntereNB.InterFreq.ExecSuccOut (None)', \
           'L.HHO.IntereNB.IntraFreq.ExecAttOut (None)', 'L.HHO.IntereNB.IntraFreq.ExecSuccOut (None)', 'L.HHO.IntraeNB.InterFreq.ExecAttOut (None)', \
           'L.HHO.IntraeNB.InterFreq.ExecSuccOut (None)', 'L.HHO.IntraeNB.IntraFreq.ExecAttOut (None)', 'L.HHO.IntraeNB.IntraFreq.ExecSuccOut (None)', 'L.Thrp.bits.DL (bit)', \
           'L.Thrp.bits.DL.LastTTI (bit)', 'L.Thrp.bits.DL.QCI.1 (bit)', 'L.Thrp.bits.DL.QCI.2 (bit)', 'L.Thrp.bits.DL.QCI.3 (bit)', 'L.Thrp.bits.DL.QCI.4 (bit)', \
           'L.Thrp.bits.DL.QCI.5 (bit)', 'L.Thrp.bits.DL.QCI.6 (bit)', 'L.Thrp.bits.DL.QCI.7 (bit)', 'L.Thrp.bits.DL.QCI.8 (bit)', 'L.Thrp.bits.DL.QCI.9 (bit)', \
           'L.Thrp.bits.DL.QCI.65 (bit)', 'L.Thrp.bits.DL.QCI.66 (bit)', 'L.Thrp.bits.DL.QCI.69 (bit)', 'L.Thrp.bits.DL.QCI.70 (bit)', 'L.Thrp.bits.UE.UL.LastTTI (bit)', \
           'L.Thrp.bits.UL (bit)', 'L.Thrp.bits.UL.QCI.1 (bit)', 'L.Thrp.bits.UL.QCI.2 (bit)', 'L.Thrp.bits.UL.QCI.3 (bit)', 'L.Thrp.bits.UL.QCI.4 (bit)', 'L.Thrp.bits.UL.QCI.5 (bit)', \
           'L.Thrp.bits.UL.QCI.6 (bit)', 'L.Thrp.bits.UL.QCI.7 (bit)', 'L.Thrp.bits.UL.QCI.8 (bit)', 'L.Thrp.bits.UL.QCI.9 (bit)', 'L.Thrp.bits.UL.QCI.65 (bit)', \
           'L.Thrp.bits.UL.QCI.66 (bit)', 'L.Thrp.bits.UL.QCI.69 (bit)', 'L.Thrp.bits.UL.QCI.70 (bit)', 'L.Thrp.Time.DL.RmvLastTTI (ms)', 'L.Thrp.Time.UE.UL.RmvLastTTI (ms)', \
           'L.RRC.ConnReq.Att (None)', 'L.RRC.ConnReq.Succ (None)']
list_2 = [ 'PS traffic 4G, GB', 'Cell Availability 4G, %', 'Total LTE Cells Number', 'Downlink PRB UR,%', 'Uplink PRB UR,%', 'UE Downlink Av Thrp', \
           'UE Uplink Av Thrp', 'E-RAB Setup SR, %', 'E-RAB Drop Rate', 'Inter-Freq HO Out SR,%', 'Intra-Freq HO Out SR,%', \
           'CSFB to WCDMA', 'CSFB to GERAN', 'RRS setup SR,%', 'CCSR, %']

# Genicheck cluster
list_cluster = ['LABEL=UH29813, CellIndex=883, CGI=25094C3507475', 'LABEL=UH29812, CellIndex=882, CGI=25094C3507474', \
                'LABEL=UH29811, CellIndex=881, CGI=25094C3507473', 'LABEL=UH19473, CellIndex=880, CGI=25094C3504C11', \
                'LABEL=UH19472, CellIndex=879, CGI=25094C3504C10', 'LABEL=UH19471, CellIndex=878, CGI=25094C3504C0F', \
                'LABEL=UH08216, CellIndex=259, CGI=25094C3502018', 'LABEL=UH08215, CellIndex=258, CGI=25094C3502017', \
                'LABEL=UH08214, CellIndex=257, CGI=25094C3502016', 'LABEL=UH09703, CellIndex=306, CGI=25094C35025E7', \
                'LABEL=UH09702, CellIndex=305, CGI=25094C35025E6', \
                'LABEL=UH08815, CellIndex=270, CGI=25094C350226F', \
                'LABEL=UH08812, CellIndex=267, CGI=25094C350226C', \
                'LABEL=UH09701, CellIndex=304, CGI=25094C35025E5', \
                'LABEL=UH08811, CellIndex=266, CGI=25094C350226B', \
                'LABEL=UH39252, CellIndex=311, CGI=25094C3509954', \
                'LABEL=UH39251, CellIndex=310, CGI=25094C3509953', \
                'LABEL=UH08816, CellIndex=271, CGI=25094C3502270', \
                'LABEL=UH08814, CellIndex=269, CGI=25094C350226E', \
                'LABEL=UH08213, CellIndex=256, CGI=25094C3502015', \
                'LABEL=UH08813, CellIndex=268, CGI=25094C350226D', \
                'LABEL=UH08212, CellIndex=255, CGI=25094C3502014', \
                'LABEL=UH08211, CellIndex=254, CGI=25094C3502013', \
                'LABEL=UH39253, CellIndex=312, CGI=25094C3509955', ]
# фильтрация по кластеру:
#sts_df = sts_df[sts_df['GCELL'].isin(list_cluster)]

# обработка weekly:
weekly_df = sts_df.groupby(['week'])[list_1]. sum().reset_index()
weekly_df['PS traffic 4G, GB'] =(weekly_df['L.Thrp.bits.DL (bit)'] + weekly_df['L.Thrp.bits.UL (bit)'])/8/1024/1024/1024
weekly_df['Cell Availability 4G,%'] = 100 * weekly_df['L.Cell.Avail.Dur (s)'] / active_cell_number / 24 / 3600  # количество сот 9426
weekly_df['Total LTE Cells Number'] = active_cell_number # количество сот
weekly_df['Downlink PRB UR,%'] = weekly_df['L.ChMeas.PRB.DL.Used.Avg (None)'] / weekly_df['L.ChMeas.PRB.DL.Avail (None)'] * 100
weekly_df['Uplink PRB UR,%'] = weekly_df['L.ChMeas.PRB.UL.Used.Avg (None)'] /  weekly_df['L.ChMeas.PRB.UL.Avail (None)'] * 100
weekly_df['UE Downlink Av Thrp'] = (weekly_df['L.Thrp.bits.DL (bit)'] - weekly_df['L.Thrp.bits.DL.LastTTI (bit)']) / weekly_df['L.Thrp.Time.DL.RmvLastTTI (ms)']
weekly_df['UE Uplink Av Thrp'] = (weekly_df['L.Thrp.bits.UL (bit)'] - weekly_df['L.Thrp.bits.UE.UL.LastTTI (bit)']) / weekly_df['L.Thrp.Time.UE.UL.RmvLastTTI (ms)']
weekly_df['E-RAB Setup SR, %'] = weekly_df['L.E-RAB.SuccEst (None)'] / (weekly_df['L.E-RAB.AttEst (None)'] - weekly_df['L.E-RAB.FailEst.X2AP (None)']) * 100
weekly_df['E-RAB Drop Rate, %'] = weekly_df['L.E-RAB.AbnormRel (None)'] / (weekly_df['L.E-RAB.AbnormRel (None)'] + weekly_df['L.E-RAB.NormRel (None)'] + weekly_df['L.E-RAB.NormRel.IRatHOOut (None)'])*100
weekly_df['Inter-Freq HO Out SR,%'] = (weekly_df['L.HHO.IntraeNB.InterFreq.ExecSuccOut (None)'] + weekly_df['L.HHO.IntereNB.InterFreq.ExecSuccOut (None)']) / \
                                                        (weekly_df['L.HHO.IntraeNB.InterFreq.ExecAttOut (None)'] + weekly_df['L.HHO.IntereNB.InterFreq.ExecAttOut (None)']) * 100
weekly_df['Intra-Freq HO Out SR,%'] = (weekly_df['L.HHO.IntraeNB.IntraFreq.ExecSuccOut (None)'] + weekly_df['L.HHO.IntereNB.IntraFreq.ExecSuccOut (None)']) / \
                                                        (weekly_df['L.HHO.IntraeNB.IntraFreq.ExecAttOut (None)'] + weekly_df['L.HHO.IntereNB.IntraFreq.ExecAttOut (None)']) * 100
weekly_df['CSFB to WCDMA'] = weekly_df['L.CSFB.E2W (None)']
weekly_df['CSFB to GERAN'] = weekly_df['L.CSFB.E2G (None)']
weekly_df['RRS setup SR,%'] = weekly_df['L.RRC.ConnReq.Succ (None)'] / weekly_df['L.RRC.ConnReq.Att (None)'] * 100
weekly_df['DCSR4G, %'] = weekly_df['RRS setup SR,%'] * weekly_df['E-RAB Setup SR, %'] * (100 - weekly_df['E-RAB Drop Rate, %']) / 10000

weekly_df = weekly_df.drop(list_1, axis=1)
weekly_df = weekly_df.transpose()


# обработка daily:
daily_df = sts_df.groupby(['date'])[list_1]. sum().reset_index()
daily_df['PS traffic 4G, GB'] =(daily_df['L.Thrp.bits.DL (bit)'] + daily_df['L.Thrp.bits.UL (bit)'])/8/1024/1024/1024
daily_df['Cell Availability 4G,%'] = 100 * daily_df['L.Cell.Avail.Dur (s)'] / active_cell_number / 24 / 3600  # количество сот 9426
daily_df['Total LTE Cells Number'] = active_cell_number # количество сот
daily_df['Downlink PRB UR,%'] = daily_df['L.ChMeas.PRB.DL.Used.Avg (None)'] / daily_df['L.ChMeas.PRB.DL.Avail (None)'] * 100
daily_df['Uplink PRB UR,%'] = daily_df['L.ChMeas.PRB.UL.Used.Avg (None)'] /  daily_df['L.ChMeas.PRB.UL.Avail (None)'] * 100
daily_df['UE Downlink Av Thrp'] = (daily_df['L.Thrp.bits.DL (bit)'] - daily_df['L.Thrp.bits.DL.LastTTI (bit)']) / daily_df['L.Thrp.Time.DL.RmvLastTTI (ms)']
daily_df['UE Uplink Av Thrp'] = (daily_df['L.Thrp.bits.UL (bit)'] - daily_df['L.Thrp.bits.UE.UL.LastTTI (bit)']) / daily_df['L.Thrp.Time.UE.UL.RmvLastTTI (ms)']
daily_df['E-RAB Setup SR, %'] = daily_df['L.E-RAB.SuccEst (None)'] / (daily_df['L.E-RAB.AttEst (None)'] - daily_df['L.E-RAB.FailEst.X2AP (None)']) * 100
daily_df['E-RAB Drop Rate, %'] = daily_df['L.E-RAB.AbnormRel (None)'] / (daily_df['L.E-RAB.AbnormRel (None)'] + daily_df['L.E-RAB.NormRel (None)'] + daily_df['L.E-RAB.NormRel.IRatHOOut (None)'])*100
daily_df['Inter-Freq HO Out SR,%'] = (daily_df['L.HHO.IntraeNB.InterFreq.ExecSuccOut (None)'] + daily_df['L.HHO.IntereNB.InterFreq.ExecSuccOut (None)']) / \
                                                        (daily_df['L.HHO.IntraeNB.InterFreq.ExecAttOut (None)'] + daily_df['L.HHO.IntereNB.InterFreq.ExecAttOut (None)']) * 100
daily_df['Intra-Freq HO Out SR,%'] = (daily_df['L.HHO.IntraeNB.IntraFreq.ExecSuccOut (None)'] + daily_df['L.HHO.IntereNB.IntraFreq.ExecSuccOut (None)']) / \
                                                        (daily_df['L.HHO.IntraeNB.IntraFreq.ExecAttOut (None)'] + daily_df['L.HHO.IntereNB.IntraFreq.ExecAttOut (None)']) * 100
daily_df['CSFB to WCDMA'] = daily_df['L.CSFB.E2W (None)']
daily_df['CSFB to GERAN'] = daily_df['L.CSFB.E2G (None)']
daily_df['RRS setup SR,%'] = daily_df['L.RRC.ConnReq.Succ (None)'] / daily_df['L.RRC.ConnReq.Att (None)'] * 100
daily_df['DCSR4G, %'] = daily_df['RRS setup SR,%'] * daily_df['E-RAB Setup SR, %'] * (100 - daily_df['E-RAB Drop Rate, %']) / 10000

daily_df = daily_df.drop(list_1, axis=1)
daily_df = daily_df.transpose()


# обработка часовая
hourly_df = sts_df.groupby(['date', 'hour'])[list_1].sum().reset_index()
hourly_df['PS traffic 4G, GB'] =(hourly_df['L.Thrp.bits.DL (bit)'] + hourly_df['L.Thrp.bits.UL (bit)'])/8/1024/1024/1024
hourly_df['Cell Availability 4G, %'] = 100 * hourly_df['L.Cell.Avail.Dur (s)'] / active_cell_number / 3600  # количество сот
hourly_df['Total LTE Cells Number'] = active_cell_number # количество сот
hourly_df['Downlink PRB UR,%'] = hourly_df['L.ChMeas.PRB.DL.Used.Avg (None)'] / hourly_df['L.ChMeas.PRB.DL.Avail (None)'] * 100
hourly_df['Uplink PRB UR,%'] = hourly_df['L.ChMeas.PRB.UL.Used.Avg (None)'] /  hourly_df['L.ChMeas.PRB.UL.Avail (None)'] * 100
hourly_df['UE Downlink Av Thrp'] = (hourly_df['L.Thrp.bits.DL (bit)'] - hourly_df['L.Thrp.bits.DL.LastTTI (bit)']) / hourly_df['L.Thrp.Time.DL.RmvLastTTI (ms)']
hourly_df['UE Uplink Av Thrp'] = (hourly_df['L.Thrp.bits.UL (bit)'] - hourly_df['L.Thrp.bits.UE.UL.LastTTI (bit)']) / hourly_df['L.Thrp.Time.UE.UL.RmvLastTTI (ms)']
hourly_df['E-RAB Setup SR,%'] = hourly_df['L.E-RAB.SuccEst (None)'] / (hourly_df['L.E-RAB.AttEst (None)'] - hourly_df['L.E-RAB.FailEst.X2AP (None)']) * 100
hourly_df['E-RAB Drop Rate'] = hourly_df['L.E-RAB.AbnormRel (None)'] / (hourly_df['L.E-RAB.AbnormRel (None)'] + hourly_df['L.E-RAB.NormRel (None)'] + hourly_df['L.E-RAB.NormRel.IRatHOOut (None)'])*100
hourly_df['Inter-Freq HO Out SR,%'] = (hourly_df['L.HHO.IntraeNB.InterFreq.ExecSuccOut (None)'] + hourly_df['L.HHO.IntereNB.InterFreq.ExecSuccOut (None)']) / \
                                                        (hourly_df['L.HHO.IntraeNB.InterFreq.ExecAttOut (None)'] + hourly_df['L.HHO.IntereNB.InterFreq.ExecAttOut (None)']) * 100
hourly_df['Intra-Freq HO Out SR,%'] = (hourly_df['L.HHO.IntraeNB.IntraFreq.ExecSuccOut (None)'] + hourly_df['L.HHO.IntereNB.IntraFreq.ExecSuccOut (None)']) / \
                                                        (hourly_df['L.HHO.IntraeNB.IntraFreq.ExecAttOut (None)'] + hourly_df['L.HHO.IntereNB.IntraFreq.ExecAttOut (None)']) * 100
hourly_df['CSFB to WCDMA'] = hourly_df['L.CSFB.E2W (None)']
hourly_df['CSFB to GERAN'] = hourly_df['L.CSFB.E2G (None)']
hourly_df['RRS setup SR,%'] = hourly_df['L.RRC.ConnReq.Succ (None)'] / hourly_df['L.RRC.ConnReq.Att (None)'] * 100
hourly_df['DCSR4G, %'] = hourly_df['RRS setup SR,%'] * hourly_df['E-RAB Setup SR,%'] * (100 - hourly_df['E-RAB Drop Rate']) / 10000

hourly_df = hourly_df.drop(list_1, axis=1)
hourly_df = hourly_df.transpose()

######
# обработка busy hour
hourlyBH_df = sts_df.groupby(['date', 'hour'])[list_1].sum().reset_index()
max_index = hourlyBH_df.groupby('date')['L.Thrp.bits.DL (bit)'].idxmax()
hourlyBH_df = hourlyBH_df.loc[max_index]

hourlyBH_df['PS traffic 4G, GB'] =(hourlyBH_df['L.Thrp.bits.DL (bit)'] + hourlyBH_df['L.Thrp.bits.UL (bit)'])/8/1024/1024/1024
hourlyBH_df['Cell Availability 4G, %'] = 100 * hourlyBH_df['L.Cell.Avail.Dur (s)'] / active_cell_number / 3600  # количество сот
hourlyBH_df['Total LTE Cells Number'] = active_cell_number # количество сот
hourlyBH_df['Downlink PRB UR,%'] = hourlyBH_df['L.ChMeas.PRB.DL.Used.Avg (None)'] / hourlyBH_df['L.ChMeas.PRB.DL.Avail (None)'] * 100
hourlyBH_df['Uplink PRB UR,%'] = hourlyBH_df['L.ChMeas.PRB.UL.Used.Avg (None)'] /  hourlyBH_df['L.ChMeas.PRB.UL.Avail (None)'] * 100
hourlyBH_df['UE Downlink Av Thrp'] = (hourlyBH_df['L.Thrp.bits.DL (bit)'] - hourlyBH_df['L.Thrp.bits.DL.LastTTI (bit)']) / hourlyBH_df['L.Thrp.Time.DL.RmvLastTTI (ms)']
hourlyBH_df['UE Uplink Av Thrp'] = (hourlyBH_df['L.Thrp.bits.UL (bit)'] - hourlyBH_df['L.Thrp.bits.UE.UL.LastTTI (bit)']) / hourlyBH_df['L.Thrp.Time.UE.UL.RmvLastTTI (ms)']
hourlyBH_df['E-RAB Setup SR,%'] = hourlyBH_df['L.E-RAB.SuccEst (None)'] / (hourlyBH_df['L.E-RAB.AttEst (None)'] - hourlyBH_df['L.E-RAB.FailEst.X2AP (None)']) * 100
hourlyBH_df['E-RAB Drop Rate'] = hourlyBH_df['L.E-RAB.AbnormRel (None)'] / (hourlyBH_df['L.E-RAB.AbnormRel (None)'] + hourlyBH_df['L.E-RAB.NormRel (None)'] + hourlyBH_df['L.E-RAB.NormRel.IRatHOOut (None)'])*100
hourlyBH_df['Inter-Freq HO Out SR,%'] = (hourlyBH_df['L.HHO.IntraeNB.InterFreq.ExecSuccOut (None)'] + hourlyBH_df['L.HHO.IntereNB.InterFreq.ExecSuccOut (None)']) / \
                                                        (hourlyBH_df['L.HHO.IntraeNB.InterFreq.ExecAttOut (None)'] + hourlyBH_df['L.HHO.IntereNB.InterFreq.ExecAttOut (None)']) * 100
hourlyBH_df['Intra-Freq HO Out SR,%'] = (hourlyBH_df['L.HHO.IntraeNB.IntraFreq.ExecSuccOut (None)'] + hourlyBH_df['L.HHO.IntereNB.IntraFreq.ExecSuccOut (None)']) / \
                                                        (hourlyBH_df['L.HHO.IntraeNB.IntraFreq.ExecAttOut (None)'] + hourlyBH_df['L.HHO.IntereNB.IntraFreq.ExecAttOut (None)']) * 100
hourlyBH_df['CSFB to WCDMA'] = hourlyBH_df['L.CSFB.E2W (None)']
hourlyBH_df['CSFB to GERAN'] = hourlyBH_df['L.CSFB.E2G (None)']
hourlyBH_df['RRS setup SR,%'] = hourlyBH_df['L.RRC.ConnReq.Succ (None)'] / hourlyBH_df['L.RRC.ConnReq.Att (None)'] * 100
hourlyBH_df['DCSR4G, %'] = hourlyBH_df['RRS setup SR,%'] * hourlyBH_df['E-RAB Setup SR,%'] * (100 - hourlyBH_df['E-RAB Drop Rate']) / 10000

hourlyBH_df = hourlyBH_df.drop(list_1, axis=1)
hourlyBH_df = hourlyBH_df.transpose()

with pd.ExcelWriter(f"{directory}{csv_name}{output_comment}.xls", engine='openpyxl') as writer:
    weekly_df.to_excel(writer, sheet_name='weekly')
    daily_df.to_excel(writer, sheet_name='daily')
    hourly_df.to_excel(writer, sheet_name='hour')
    hourlyBH_df.to_excel(writer, sheet_name='busy_hour')

#daily_df.to_excel("C:/test/sts4G/daily.xls", engine='openpyxl', sheet_name='Book1')
print('готово')
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)


#hourly_df['PS traffic 4G, GB'] =(hourly_df['L.Thrp.bits.DL (bit)'] + hourly_df['L.Thrp.bits.DL.QCI.1 (bit)'] + hourly_df['L.Thrp.bits.DL.QCI.2 (bit)'] + hourly_df['L.Thrp.bits.DL.QCI.3 (bit)']+\
#                                hourly_df['L.Thrp.bits.DL.QCI.4 (bit)'] + hourly_df['L.Thrp.bits.DL.QCI.5 (bit)'] + hourly_df['L.Thrp.bits.DL.QCI.6 (bit)'] + hourly_df['L.Thrp.bits.DL.QCI.7 (bit)']+\
#                                hourly_df['L.Thrp.bits.DL.QCI.8 (bit)'] + hourly_df['L.Thrp.bits.DL.QCI.9 (bit)'] + hourly_df['L.Thrp.bits.DL.QCI.65 (bit)'] + hourly_df['L.Thrp.bits.DL.QCI.66 (bit)']+ \
#                                hourly_df['L.Thrp.bits.DL.QCI.69 (bit)'] +hourly_df['L.Thrp.bits.DL.QCI.70 (bit)'] + hourly_df['L.Thrp.bits.UL (bit)']+\
#                                hourly_df['L.Thrp.bits.UL.QCI.1 (bit)'] + hourly_df['L.Thrp.bits.UL.QCI.2 (bit)'] + hourly_df['L.Thrp.bits.UL.QCI.3 (bit)'] + hourly_df['L.Thrp.bits.UL.QCI.4 (bit)']+\
#                                hourly_df['L.Thrp.bits.UL.QCI.5 (bit)'] + hourly_df['L.Thrp.bits.UL.QCI.6 (bit)'] + hourly_df['L.Thrp.bits.UL.QCI.7 (bit)'] + hourly_df['L.Thrp.bits.UL.QCI.8 (bit)']+\
#                                hourly_df['L.Thrp.bits.UL.QCI.9 (bit)'] + hourly_df['L.Thrp.bits.UL.QCI.65 (bit)'] + hourly_df['L.Thrp.bits.UL.QCI.66 (bit)'] + hourly_df['L.Thrp.bits.UL.QCI.69 (bit)']+\
#                                hourly_df['L.Thrp.bits.UL.QCI.70 (bit)'])/8/1024/1024/1024