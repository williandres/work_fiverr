
import pandas as pd

# Lista de columnas proporcionadas
columns = [
    'Artikelname', 'Handelssprache', 'Lokaler Artikelname', 'Artikelnummer', 'Vertriebsweg', 
    'Verkaufspreis', 'Wâ€°hrung', 'Exportpreise gÂ¸ltig ab', 'Verkauf ab', 'Einheit', 
    'Matchcode', 'Artikel ist aktiv', 'Warengruppen-Name', 'Warengruppen-Beschreibung', 
    'Steuersatz', 'Kurztext 1', 'Handelssprache', 'Lokalisierte Kurztext 1', 'Kurztext 2', 
    'Handelssprache', 'Lokalisierte Kurztext 2', 'Artikelbeschreibung', 'Handelssprache', 
    'Lokalisierte Artikelbeschreibung', 'Interner Hinweis', 'Handelssprache', 
    'Lokalisierter interner Hinweis', 'Artikel-Langbeschreibung', 'Handelssprache', 
    'Lokalisierte lange Artikelbeschreibung', 'EAN-Nummer', 'Hersteller', 'Systemcode', 
    'Katalogcode', 'Verkauf von', 'Verkauf bis', 'Support bis', 'MPN-Nummer', 'Ursprungsland', 
    'Bruttogewicht Artikel', 'Nettogewicht Artikel', 'Zolltarifnummer', 'Zollbeschreibung', 
    'Lâ€°nge Artikel', 'Breite Artikel', 'HË†he Artikel', 'Herstellertyp', 'EinfÂ¸hrungsdatum', 
    'Sicherheitstage', 'Mindestlagerbestand', 'Zielbestand', 'Wiederbeschaffungstage', 
    'Durchschnittliche Lieferzeit', 'Mindestbestellmenge', 'Fixe Bestellmenge', 
    'Margen-Kalkulations-Preis-Typ', 'Ignorieren in Preiskalkulation', 
    'Standard-Kalkulationspreis fÂ¸r die Preiskalkulation', 'Interner Verrechnungspreis', 
    'Preis-Eintritt Verrechnungspreis', 'UVP netto', 'Preis-Eintritt UVP netto', 'UVP brutto', 
    'Preis-Eintritt UVP brutto', 'Auf Lieferschein', 'Artikeltyp', 'Zu produzieren', 
    'Chargennummer erforderlich', 'Seriennummer erforderlich', 'Ladehilfsmittel bestandsfÂ¸hrend', 
    'ABC-Klassifizierung', 'Aktuelle Herstellkosten', 'Verkaufsartikel', 
    'StÂ¸cklistenteillieferung mË†glich', 'Unterpositionen mit Preisen fÂ¸r Verkauf', 
    'Unterpositionen mit Preisen fÂ¸r Einkauf', 'In Produktionsauftrâ€°gen auflË†sen', 
    'Verfallstage', 'Verfallsdatum von Produktionsauftrags-Positionen berÂ¸cksichtigen', 
    'Nur aktivierte Vertriebswege im Verkauf erlauben', 'Artikelkennzeichen', 'Kostenstelle Verkauf', 
    'Kostenstelle Einkauf', 'Kostenart', 'ErlË†skonto', 'Aufwandskonto', 'Skontoabzugsfâ€°hig', 
    'Geplante Arbeitszeit pro Einheit', 'Abrechnungsart', 'Belegposition Gruppenname'
]


df = pd.DataFrame(columns=columns)

excel_data1 = pd.read_excel('sources/output.xlsx', usecols=[0], skiprows=1)
excel_data2 = pd.read_excel('sources/output.xlsx', usecols=[1], skiprows=1)
excel_data3 = pd.read_excel('sources/output.xlsx', usecols=[2], skiprows=1)
excel_data4 = pd.read_excel('sources/output.xlsx', usecols=[3], skiprows=1)

df['Artikelname'] = excel_data1.iloc[:, 0].values
df['Artikelnummer'] = excel_data2.iloc[:, 0].values
df['Vertriebsweg'] = 'NET1'
df['Verkaufspreis'] = excel_data3.iloc[:, 0].values
df['Wâ€°hrung'] = 'EUR'
df['Einheit'] = 'Stk.'
df['Artikel ist aktiv'] = 'yes'
df['Steuersatz'] = 'REDUCED'
df['Artikelbeschreibung'] = excel_data4.iloc[:, 0].values
df['Artikeltyp'] = 'STORABLE'
df['Ladehilfsmittel bestandsfÂ¸hrend'] = 'no'

# Mostrar el DataFrame para verificar
print(df)
df.to_excel('final_version.xlsx', index=False)