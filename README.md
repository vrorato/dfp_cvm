# Overview

  In order to carry out an excellent valuation of companies using dcf (discounted-cash-flow), the first and most important step is to obtain information on public companies from reliable sources.
  With this in mind, I created a code in Python that will search for information on Brazilian public companies directly on the website of the market regulatory body - CVM (Securities Commission).
  The CVM is an agency linked to the Ministry of Finance responsible for disciplining, supervising and developing the securities market in Brazil.
  Every quarter, companies must disclose their standardized financial statements (DFP) to investors through their Balance Sheet (BP), Income Statement (DRE) and Cash Flow Statement (DFC). This information is sent to CVM, which stores everything on its website via the url: https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/.

## Code

  Given this need to collect reliable information, the code is responsible for performing webscrapping on the CVM website and searching for all DFP available between the years 2018 and 2022. Once on the website, the code will automatically download and extract the data to folders created by him.
  Finally, with the documents extracted, it combines all files from all years according to the nature of the document, which may be:
  - Consolidated DRE
  - Consolidated Asset Balance Sheet
  - Consolidated Liabilities Balance Sheet
  - Consolidated Cash Flow Statement

  With the .csv data contained in these documents, it is possible to analyze the financial health of any company listed on the Brazilian stock exchange and thus carry out a quality valuation from a reliable source.

## Output

The output of this code will be 4 csv files:
  - dfp_cia_aberta_BPA_con_2018-2022
  - dfp_cia_aberta_BPA_con_2018-2022
  - dfp_cia_aberta_DRE_con_2018-2022
  - dfp_cia_aberta_DFC_MI_con_2018-2022

## Disclosure

  It is important to highlight that this work aims only to show how the use of Python can be fundamental when searching for information on the internet.
