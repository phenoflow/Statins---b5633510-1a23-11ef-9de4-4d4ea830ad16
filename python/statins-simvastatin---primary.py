# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"47948","system":"gprdproduct"},{"code":"34366","system":"gprdproduct"},{"code":"34312","system":"gprdproduct"},{"code":"5148","system":"gprdproduct"},{"code":"46878","system":"gprdproduct"},{"code":"34353","system":"gprdproduct"},{"code":"40340","system":"gprdproduct"},{"code":"45219","system":"gprdproduct"},{"code":"34381","system":"gprdproduct"},{"code":"34376","system":"gprdproduct"},{"code":"34891","system":"gprdproduct"},{"code":"42","system":"gprdproduct"},{"code":"48051","system":"gprdproduct"},{"code":"34316","system":"gprdproduct"},{"code":"25","system":"gprdproduct"},{"code":"34535","system":"gprdproduct"},{"code":"41657","system":"gprdproduct"},{"code":"51","system":"gprdproduct"},{"code":"34481","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('statins-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["statins-simvastatin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["statins-simvastatin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["statins-simvastatin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
