# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"9315","system":"gprdproduct"},{"code":"5251","system":"gprdproduct"},{"code":"5009","system":"gprdproduct"},{"code":"5278","system":"gprdproduct"},{"code":"420","system":"gprdproduct"},{"code":"31658","system":"gprdproduct"},{"code":"4961","system":"gprdproduct"},{"code":"9316","system":"gprdproduct"},{"code":"18442","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('statins-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["statins-400microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["statins-400microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["statins-400microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
