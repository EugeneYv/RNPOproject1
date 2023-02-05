import pandas as pd
import winsound
'''вывод посуточной статистики для GSM. импортный файл - в МАЕ вывести в формате xlsx, потом в экселе переделать в csv'''

sts_df = pd.read_csv("C:/work/CityH_audit/sts/2G/2G_09-30.01.csv", sep=";", header=7)
sts_df['date'] = sts_df['Start Time'].str.split(' ').str[0]
sts_df['hour'] = sts_df['Start Time'].str.split(' ').str[1]

list_1 = ['CH310:Number of Outgoing Internal Inter-Cell Handover Requests (None)' ,'CH313:Number of Successful Outgoing Internal Inter-Cell Handovers (None)',\
          'CH330:Outgoing External Inter-Cell Handover Requests (None)', 'CH333:Successful Outgoing External Inter-Cell Handovers (None)', 'CM30:Call Drops on SDCCH (None)',\
          'CM33:Call Drops on Traffic Channel (None)', 'K3000:SDCCH Seizure Requests (None)', 'K3001:Failed SDCCH Seizures due to Busy SDCCH (None)',\
          'K3003:Successful SDCCH Seizures (None)', 'K3004:Traffic Volume on SDCCH (Erl)', 'K3010A:TCH Seizure Requests (Traffic Channel) (None)',\
          'K3010B:TCH Seizure Requests in TCH Handovers (Traffic Channel) (None)', 'K3011A:Failed TCH Seizures due to Busy TCH (Traffic Channel) (None)',\
          'K3011B:Failed TCH Seizures in TCH Handovers due to Busy TCH (Traffic Channel) (None)', 'K3013A:Successful TCH Seizures (Traffic Channel) (None)',\
          'K3013B:Successful TCH Seizures in TCH handovers (Traffic Channel) (None)', 'K3014:Traffic Volume on TCH (Erl)', 'K3020:TCH Seizure Requests (Signaling Channel) (None)',\
          'K3021:Failed TCH Seizures due to Busy TCH (Signaling Channel) (None)', 'K3023:Successful TCH Seizures (Signaling Channel) (None)',\
          'K3024:Traffic Volume on TCH (Signaling Channel) (Erl)', 'K3034:TCHH Traffic Volume (Erl)', 'S3655:Number of configured TRXs in a cell (None)',\
          'S3656:Number of available TRXs in a cell (None)']

list_2 = ['TRX Availability 2G %', 'TRXs Number', 'TCH traffic 2G, Erl', 'SDCCH taffic, Erl', 'SDCCH Congesstion, %', 'TCH Congestion excluding handover, %',\
          'TCH Congestion including handover, %', 'SDCCH Drop Rate, %', 'TCH Assignment Failure Rate, %', 'TCH traffic HalfRate, Erl', 'TCH Drop Rate, %', \
          'Handover Success Rate, %', 'Immediate assignment SR, %', 'Call completion success rate, %']

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
# Каховка
list_cluster_Kahovka = ['LABEL=UH29813, CellIndex=883, CGI=25094C3507475', \
                'LABEL=UH29812, CellIndex=882, CGI=25094C3507474', \
                'LABEL=UH29811, CellIndex=881, CGI=25094C3507473', \
                'LABEL=UH19473, CellIndex=880, CGI=25094C3504C11', \
                'LABEL=UH19472, CellIndex=879, CGI=25094C3504C10', \
                'LABEL=UH19471, CellIndex=878, CGI=25094C3504C0F', \
                'LABEL=UH08216, CellIndex=259, CGI=25094C3502018', \
                'LABEL=UH08215, CellIndex=258, CGI=25094C3502017', \
                'LABEL=UH08214, CellIndex=257, CGI=25094C3502016', \
                'LABEL=UH09703, CellIndex=306, CGI=25094C35025E7', \
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
                'LABEL=UH39253, CellIndex=312, CGI=25094C3509955']
# фильтрация по скластеру:
sts_df = sts_df[sts_df['GCELL'].isin(list_cluster)]

# обработка daily:
daily_df = sts_df.groupby(['date'])[list_1]. sum().reset_index()

daily_df['TRX Availability 2G %'] = daily_df['S3656:Number of available TRXs in a cell (None)'] / daily_df['S3655:Number of configured TRXs in a cell (None)'] * 100
daily_df['TRXs Number'] = daily_df['S3656:Number of available TRXs in a cell (None)'] / 24
daily_df['TCH traffic 2G, Erl']= daily_df['K3014:Traffic Volume on TCH (Erl)']
daily_df['SDCCH taffic, Erl']= daily_df['K3004:Traffic Volume on SDCCH (Erl)']
daily_df['SDCCH Congesstion, %']= daily_df['K3001:Failed SDCCH Seizures due to Busy SDCCH (None)'] / daily_df['K3003:Successful SDCCH Seizures (None)'] * 100
daily_df['TCH Congestion excluding handover, %']= (daily_df['K3011A:Failed TCH Seizures due to Busy TCH (Traffic Channel) (None)']+ \
                                                   daily_df['K3021:Failed TCH Seizures due to Busy TCH (Signaling Channel) (None)'])/\
                                                  (daily_df['K3020:TCH Seizure Requests (Signaling Channel) (None)'] + daily_df['K3010A:TCH Seizure Requests (Traffic Channel) (None)'])*100
daily_df['TCH Congestion including handover, %']=(daily_df['K3011A:Failed TCH Seizures due to Busy TCH (Traffic Channel) (None)']+ \
                                                   daily_df['K3021:Failed TCH Seizures due to Busy TCH (Signaling Channel) (None)'] + \
                                                  daily_df['K3011B:Failed TCH Seizures in TCH Handovers due to Busy TCH (Traffic Channel) (None)'])/\
                                                  (daily_df['K3020:TCH Seizure Requests (Signaling Channel) (None)'] + \
                                                   daily_df['K3010A:TCH Seizure Requests (Traffic Channel) (None)']+ \
                                                   daily_df['K3010B:TCH Seizure Requests in TCH Handovers (Traffic Channel) (None)'])*100
daily_df['SDCCH Drop Rate, %']= daily_df['CM30:Call Drops on SDCCH (None)'] / daily_df['K3003:Successful SDCCH Seizures (None)'] * 100
daily_df['TCH Assignment Failure Rate, %']= (1 - daily_df['K3013A:Successful TCH Seizures (Traffic Channel) (None)'] / daily_df['K3010A:TCH Seizure Requests (Traffic Channel) (None)'])*100
daily_df['TCH traffic HalfRate, Erl']= daily_df['K3034:TCHH Traffic Volume (Erl)']
daily_df['TCH Drop Rate, %']= daily_df['CM33:Call Drops on Traffic Channel (None)']/ \
                              (daily_df['K3013A:Successful TCH Seizures (Traffic Channel) (None)'] + \
                               daily_df['K3013B:Successful TCH Seizures in TCH handovers (Traffic Channel) (None)'] + \
                               daily_df['K3023:Successful TCH Seizures (Signaling Channel) (None)'])*100
daily_df['Handover Success Rate, %']= (daily_df['CH333:Successful Outgoing External Inter-Cell Handovers (None)']+\
                                       daily_df['CH313:Number of Successful Outgoing Internal Inter-Cell Handovers (None)'])/\
                                      (daily_df['CH310:Number of Outgoing Internal Inter-Cell Handover Requests (None)']+\
                                       daily_df['CH330:Outgoing External Inter-Cell Handover Requests (None)']) * 100
daily_df['Immediate assignment SR, %']= daily_df['K3003:Successful SDCCH Seizures (None)']  / daily_df['K3000:SDCCH Seizure Requests (None)'] *100
daily_df['Call completion success rate, %']= daily_df['Immediate assignment SR, %'] * (100 - daily_df['SDCCH Drop Rate, %']) * (100 - daily_df['TCH Assignment Failure Rate, %'])\
                                             * (100 - daily_df['TCH Drop Rate, %']) / 1000000
daily_df = daily_df.drop(list_1, axis=1)
daily_df = daily_df.transpose()


# обработка hourly
hourly_df = sts_df.groupby(['date', 'hour'])[list_1]. sum().reset_index()
max_index = hourly_df.groupby('date')['K3014:Traffic Volume on TCH (Erl)'].idxmax()
hourly_df = hourly_df.loc[max_index]

hourly_df['TRX Availability 2G %'] = hourly_df['S3656:Number of available TRXs in a cell (None)'] / hourly_df['S3655:Number of configured TRXs in a cell (None)'] * 100
hourly_df['TRXs Number'] = hourly_df['S3656:Number of available TRXs in a cell (None)']
hourly_df['TCH traffic 2G, Erl']= hourly_df['K3014:Traffic Volume on TCH (Erl)']
hourly_df['SDCCH taffic, Erl']= hourly_df['K3004:Traffic Volume on SDCCH (Erl)']
hourly_df['SDCCH Congesstion, %']= hourly_df['K3001:Failed SDCCH Seizures due to Busy SDCCH (None)'] / hourly_df['K3003:Successful SDCCH Seizures (None)'] * 100
hourly_df['TCH Congestion excluding handover, %']= (hourly_df['K3011A:Failed TCH Seizures due to Busy TCH (Traffic Channel) (None)']+ \
                                                   hourly_df['K3021:Failed TCH Seizures due to Busy TCH (Signaling Channel) (None)'])/\
                                                  (hourly_df['K3020:TCH Seizure Requests (Signaling Channel) (None)'] + hourly_df['K3010A:TCH Seizure Requests (Traffic Channel) (None)'])*100
hourly_df['TCH Congestion including handover, %']=(hourly_df['K3011A:Failed TCH Seizures due to Busy TCH (Traffic Channel) (None)']+ \
                                                   hourly_df['K3021:Failed TCH Seizures due to Busy TCH (Signaling Channel) (None)'] + \
                                                  hourly_df['K3011B:Failed TCH Seizures in TCH Handovers due to Busy TCH (Traffic Channel) (None)'])/\
                                                  (hourly_df['K3020:TCH Seizure Requests (Signaling Channel) (None)'] + \
                                                   hourly_df['K3010A:TCH Seizure Requests (Traffic Channel) (None)']+ \
                                                   hourly_df['K3010B:TCH Seizure Requests in TCH Handovers (Traffic Channel) (None)'])*100

hourly_df['SDCCH Drop Rate, %']= hourly_df['CM30:Call Drops on SDCCH (None)'] / hourly_df['K3003:Successful SDCCH Seizures (None)'] * 100
hourly_df['TCH Assignment Failure Rate, %']= (1 - hourly_df['K3013A:Successful TCH Seizures (Traffic Channel) (None)'] / hourly_df['K3010A:TCH Seizure Requests (Traffic Channel) (None)'])*100
hourly_df['TCH traffic HalfRate, Erl']= hourly_df['K3034:TCHH Traffic Volume (Erl)']
hourly_df['TCH Drop Rate, %']= hourly_df['CM33:Call Drops on Traffic Channel (None)']/ \
                              (hourly_df['K3013A:Successful TCH Seizures (Traffic Channel) (None)'] + \
                               hourly_df['K3013B:Successful TCH Seizures in TCH handovers (Traffic Channel) (None)'] + \
                               hourly_df['K3023:Successful TCH Seizures (Signaling Channel) (None)'])*100
hourly_df['Handover Success Rate, %']= (hourly_df['CH333:Successful Outgoing External Inter-Cell Handovers (None)']+\
                                       hourly_df['CH313:Number of Successful Outgoing Internal Inter-Cell Handovers (None)'])/\
                                      (hourly_df['CH310:Number of Outgoing Internal Inter-Cell Handover Requests (None)']+\
                                       hourly_df['CH330:Outgoing External Inter-Cell Handover Requests (None)']) * 100
hourly_df['Immediate assignment SR, %']= hourly_df['K3003:Successful SDCCH Seizures (None)']  / hourly_df['K3000:SDCCH Seizure Requests (None)'] *100
hourly_df['Call completion success rate, %']= hourly_df['Immediate assignment SR, %'] * (100 - hourly_df['SDCCH Drop Rate, %']) * (100 - hourly_df['TCH Assignment Failure Rate, %'])\
                                             * (100 - hourly_df['TCH Drop Rate, %']) / 1000000
hourly_df = hourly_df.drop(list_1, axis=1) # проверка  чнн
hourly_df = hourly_df.transpose()
#daily_df.to_excel("C:/test/sts/9-15.xls", engine='openpyxl', sheet_name='Book1')
#hourly_df.to_excel("C:/test/sts/9-15h.xls", engine='openpyxl', sheet_name='Book2')
with pd.ExcelWriter('C:/work/CityH_audit/sts/2G/2G_09-30.01_output_delete.xls', engine='openpyxl') as writer:
    daily_df.to_excel(writer, sheet_name='daily')
    hourly_df.to_excel(writer, sheet_name='busy_hour')

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
print('готово')