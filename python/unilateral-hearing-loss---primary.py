# Cardoso V.,Nirantharakumar K.,Gkoutos G, 2024.

import sys, csv, re

codes = [{"code":"F592100","system":"readv2"},{"code":"F590500","system":"readv2"},{"code":"1C13100","system":"readv2"},{"code":"F591600","system":"readv2"},{"code":"1C13300","system":"readv2"},{"code":"H90.0","system":"readv2"},{"code":"H90.6","system":"readv2"},{"code":"H90.3","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hearing-loss-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["unilateral-hearing-loss---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["unilateral-hearing-loss---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["unilateral-hearing-loss---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
