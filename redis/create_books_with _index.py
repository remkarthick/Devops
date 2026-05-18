import csv

input_file = "books.csv"
output_file = "books_with_index.csv"

with open(input_file, newline="", encoding="utf-8", errors="replace") as f_in, \
     open(output_file, "w", newline="", encoding="utf-8") as f_out:

    reader = csv.reader(f_in, delimiter=';')
    writer = csv.writer(f_out, delimiter=';', quoting=csv.QUOTE_ALL)

    header = next(reader)
    writer.writerow(["Index"] + header)

    for i, row in enumerate(reader, start=1):
        if not row:
            continue
        writer.writerow([str(i)] + row)
