from odf.opendocument import OpenDocumentSpreadsheet, load
from odf.table import Table, TableRow, TableCell
from odf.text import P
from datetime import datetime
import os
ODSFILE = "Kassenwerte.ods"

def export_logs_to_ods(logfile_path: str):
    #ODS öffnen oder erstllen
    if os.path.exists(ODSFILE):
        doc = load(ODSFILE)
    else:
        doc = OpenDocumentSpreadsheet()

    # Tabbelennamen mit Datum + Uhrzeit
    run_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    table = Table(name=f"Run_{run_time}")

    header = TableRow()
    for title in ("Zeit", "Stand in €", "Operation"):
        cell = TableCell()
        cell.addElement(P(text=title))
        header.addElement(cell)
    table.addElement(header)

    with open("kassenstandspeicher.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Split: Zeit | Rest
            zeit, rest = line.split(":", 1)
            rest = rest.strip()

            # Wert | Kommentar
            parts = rest.split(" ", 1)
            wert = parts[0]
            kommentar = parts[1] if len(parts) > 1 else ""

            row = TableRow()

            for value in (zeit, wert, kommentar):
                cell = TableCell()
                cell.addElement(P(text=value))
                row.addElement(cell)
            table.addElement(row)

    doc.spreadsheet.addElement(table)
    doc.save(ODSFILE)